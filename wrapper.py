from typing import Optional

import requests
from rich.console import Console
from rich.table import Table

from db import DataLayer


class Wrapper:
    def __init__(self) -> None:
        self.base_link = "http://www.boredapi.com/api/activity/"
        self.db = DataLayer()

    def prettify_data(self, data: list[dict]) -> None:
        table = Table(title="Activities")

        columns = [
            "Key",
            "Title",
            "Type",
            "Participants",
            "Price",
            "Link",
            "Acccessibility",
        ]
        for column in columns:
            table.add_column(column)

        for activity in data:
            table.add_row(
                *[
                    str(activity["key"]),
                    activity["activity"],
                    activity["type"],
                    str(activity["participants"]),
                    str(activity["price"]),
                    activity["link"],
                    str(activity["accessibility"]),
                ],
                style="bright_green",
            )
        console = Console()
        console.print(table)

    def get_activity(
        self,
        type: Optional[str] = "",
        participants: Optional[int] = "",
        minprice: Optional[float] = "",
        maxprice: Optional[float] = "",
        minaccessibility: Optional[float] = "",
        maxaccessibility: Optional[float] = "",
    ) -> None:
        response = requests.get(
            f"{self.base_link}?type={type}&participants={participants}&minprice={minprice}&maxprice={maxprice}&minaccessibility={minaccessibility}&maxaccessibility={maxaccessibility}"
        )
        self.db.insert_activity(response.json())
        self.prettify_data([response.json()])

    def get_last_activities(self) -> None:
        data = self.db.get_activities()
        self.prettify_data(data)
