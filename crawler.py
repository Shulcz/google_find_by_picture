import requests
import time
import re

from PIL import Image
from io import BytesIO


class GoogleImageSearch:
    HEADERS = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-GB,en;q=0.9",
        "sec-ch-ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.105 Safari/537.36",
    }
    BASE_URL = "https://www.google.com/"
    GOOGLE_LENS_URL = "https://lens.google.com/"

    def __init__(
        self,
    ) -> None:
        self.proxy = {}
        self.create_session()

    def create_session(
        self,
    ) -> None:
        self.proxy = self.get_proxy()
        self.session_requests = requests.Session()
        # self.session_requests.proxies.update(self.proxy)

    def get_proxy(
        self,
    ) -> dict[str, str]:
        return {}

    def auth(
        self,
    ) -> None:
        headers = self.HEADERS
        headers["priority"] = "u=0, i"

        self.session_requests.get(
            self.BASE_URL,
            headers=headers,
        )

    def search_by_image(
        self,
        url: str,
    ) -> list:
        self.auth()

        size = self.get_image_size(url)

        headers = self.HEADERS
        headers["authority"] = self.GOOGLE_LENS_URL[8:-1]
        headers["priority"] = "u=0, i"
        headers["referer"] = self.BASE_URL

        params = {
            "url": url,
            "hl": "en-RU",
            "re": "df",
            "st": self.time_now(),
            "vpw": str(size[0]),
            "vph": str(size[1]),
            "ep": "gsbubu",
        }

        response = self.session_requests.get(
            self.GOOGLE_LENS_URL + "uploadbyurl",
            params=params,
            headers=headers,
        ).text

        images = re.findall('(?<=data-thumbnail-url=")[^"]+', response)

        return images

    def time_now(
        self,
    ) -> str:
        tm = str(time.time())
        tm = tm.split(".")
        tm = tm[0] + tm[1][:3]

    def get_image_size(
        self,
        url: str,
    ) -> tuple:
        response = requests.get(url)

        img = Image.open(BytesIO(response.content))
        width, height = img.size

        return width, height
