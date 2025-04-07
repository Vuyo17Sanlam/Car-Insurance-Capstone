import webbrowser
import xml.etree.ElementTree as ET

import requests


def get_car_image(make, model, year=None):
    search_term = f"{make} {model} {year}" if year else f"{make} {model}"
    url = f"http://www.carimagery.com/api.asmx/GetImageUrl?searchTerm={search_term.replace(' ', '+')}"

    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        image_url = root.text
        return image_url
    else:
        return "failed to return the image"


get_car_image("Polo", "TSI", "2020")
