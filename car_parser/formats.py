import json
import re

import httpx
from bs4 import BeautifulSoup


async def format_change_number(soup: BeautifulSoup) -> int:
    hash_number = soup.select_one('script[data-hash]')['data-hash']

    id_user = soup.find("link", rel="canonical")["href"]
    id_user = id_user.split(".")[-2].split("_")[-1]

    url = f'https://auto.ria.com/users/phones/{id_user}?hash={hash_number}&e'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = json.loads(response.text)
        phone_number = data.get("phones", [])[0].get("phoneFormatted", None)

    return int("38" + phone_number.replace("(", "").replace(")", "").replace(" ", ""))


def format_image_url(soup: BeautifulSoup) -> str:
    try:
        image_url = soup.find_all("source")[1]["srcset"]
    except Exception:
        image_url = None
    return image_url


def format_set_number(soup: BeautifulSoup) -> str:
    try:
        number = soup.select_one(".state-num").text
        number = "".join(number.split(" ")[:3])
    except AttributeError:
        number = None
    return number


def format_car_vin(soup: BeautifulSoup) -> str:
    try:
        vin_number = soup.select_one(".label-vin").text
    except AttributeError:
        vin_number = None
    return vin_number


def format_images_count(soup: BeautifulSoup) -> int:
    try:
        images_count = int(re.search(r"\d+", soup.select_one(".show-all").text).group())
    except Exception:
        images_count = None

    return images_count


def format_username(soup: BeautifulSoup) -> str:
    try:
        username = soup.select_one(".seller_info_name").text
    except Exception:
        username = None

    return username


async def data_validation(url_detail_car: str, soup: BeautifulSoup) -> dict:

    car_vin = format_car_vin(soup)
    car_number = format_set_number(soup)
    phone_number = await format_change_number(soup)
    image_url = format_image_url(soup)
    images_count = format_images_count(soup)
    username = format_username(soup)

    return {
        "url": url_detail_car,
        "title": soup.select_one(".heading .head")["title"],
        "price_usd": int(soup.select_one(".price_value > strong").text[:-2].replace(" ", "")),
        "odometer": int(soup.select_one(".base-information > span").text + "000"),
        "username": username,
        "phone_number": phone_number,
        "image_url": image_url,
        "images_count": images_count,
        "car_number": car_number,
        "car_vin": car_vin

    }
