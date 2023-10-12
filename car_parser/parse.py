import asyncio
import httpx as httpx
from bs4 import BeautifulSoup
from database.models import Car
from database.engine import get_db
from car_parser.formats import data_validation


class CollectCar:
    def __init__(self) -> None:
        self.url = "https://auto.ria.com/uk/car/used/"

    async def start_collect_links(self) -> None:
        while True:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.url)
                page = response.content
                soup = BeautifulSoup(page, "html.parser")
                await self.collect_car_pages(soup)

                try:
                    self.url = soup.select_one(".js-next")["href"]
                except Exception:
                    break

    async def collect_car_pages(self, soup) -> None:
        async with httpx.AsyncClient() as client:
            tasks = [self._create_car(link["href"], client) for link in soup.select(".address")]
            cars = await asyncio.gather(*tasks)

            self.save_car_to_database(cars)

    @staticmethod
    async def _create_car(url_detail_car: str, client: httpx) -> Car:
        response = await client.get(url_detail_car)
        response.raise_for_status()
        detail_car = response.content
        soup = BeautifulSoup(detail_car, "html.parser")

        data = await data_validation(url_detail_car, soup)

        return Car(
            url=data.get("url", None),
            title=data.get("title", None),
            price_usd=data.get("price_usd", None),
            odometer=data.get("odometer", None),
            username=data.get("username", None),
            phone_number=data.get("phone_number", None),
            image_url=data.get("image_url", None),
            images_count=data.get("images_count", None),
            car_number=data.get("car_number", None),
            car_vin=data.get("car_vin", None),
        )

    @staticmethod
    def save_car_to_database(cars: list[Car]) -> None:
        db = get_db()
        for car in cars:
            db.add(car)
            db.commit()
        db.close()
