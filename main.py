import requests

cookies = {
    "AEC": "Ackid1Q3PSojKEJwJzxQTrW57WiRDJSJrkw6BZ_HEILl3UH3l4ETNVfrZDU",
    "1P_JAR": "2023-11-08-19",
    "NID": "511=t2Gb_LUG8eGZ2pFJ92jLimP-S5z1J2YgqtsfxlcwTBRqvNZkk2uXKg_BXyO3L9rhjkCFCxA6hD8wLSGi4lCQwZiLM4lHBq-JT_SHFTLSZiPTMw65fVia3urJO_c46OdoX0qJRr1yDptKDDhZD-BljzFwWEYjEBEZnTdYEgKkCccSCahhXPdM_GhMdw",
    "OTZ": "7286129_44_44_123780_40_436260",
}

headers = {
    "authority": "lens.google.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "priority": "u=0, i",
    "referer": "https://www.google.com/",
    "sec-ch-ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-arch": '""',
    "sec-ch-ua-bitness": '""',
    "sec-ch-ua-full-version": '""',
    "sec-ch-ua-full-version-list": "",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"macOS"',
    "sec-ch-ua-platform-version": '""',
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.105 Safari/537.36",
    "x-client-data": "CIeFywE=",
}

params = {
    "url": "https://img.freepik.com/free-photo/adorable-looking-kitten-with-yarn_23-2150886292.jpg",
    "hl": "en-RU",
    "re": "df",
    "st": "1699471812677",
    "cd": "CPa3uyI",
    "vpw": "1200",
    "vph": "413",
    "ep": "gsbubu",
}

response = requests.get(
    "https://lens.google.com/uploadbyurl",
    params=params,
    cookies=cookies,
    headers=headers,
).text


with open("bs.html", "w") as f:
    f.write(response)
