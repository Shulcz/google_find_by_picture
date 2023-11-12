if __name__ == "__main__":
    from crawler import GoogleImageSearch

    image_url = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQOnYYxb7yui8nTUP3x4RsDFAE5AS2PER6I5--nHeX-FkSheg6T"

    print(GoogleImageSearch().search_by_image(image_url))
