import requests
from rich.console import Console
from rich.table import Table

from db import DataLayer


class Wrapper:
    def __init__(self) -> None:
        self.base_link = "http://www.boredapi.com/api/activity/"
        self.db = DataLayer()

    def prettify_data(self, data: list[dict]) -> None:
        """Displays given activities data using Rich table

        Args:
            data (list[dict]): activities data
        """
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
                str(activity["key"]),
                activity["activity"],
                activity["type"],
                str(activity["participants"]),
                str(activity["price"]),
                activity["link"],
                str(activity["accessibility"]),
                style="bright_green",
            )
        console = Console()
        console.print(table)

    def get_random_activity(
        self,
        type: str = "",
        participants: int | str = "",
        minprice: float | str = "",
        maxprice: float | str = "",
        minaccessibility: float | str = "",
        maxaccessibility: float | str = "",
    ) -> None:
        """Gets random activity from bored API

        Args:
            type (str, optional): activity type. Defaults to "".
            participants (int | str, optional): number of participants. Defaults to "".
            minprice (float | str, optional): minimum price. Defaults to "".
            maxprice (float | str, optional): maximum price. Defaults to "".
            minaccessibility (float | str, optional): minimum accessibility. Defaults to "".
            maxaccessibility (float | str, optional): maximum accessibility. Defaults to "".
        """    
        response = requests.get(
            f"{self.base_link}?type={type}&participants={participants}&minprice={minprice}&maxprice={maxprice}&minaccessibility={minaccessibility}&maxaccessibility={maxaccessibility}"
        )
        self.db.insert_activity(response.json())
        self.prettify_data([response.json()])

    def get_last_activities(self) -> None:
        """Returns 5 last activities from the database
        """ 
        data = self.db.get_activities()
        self.prettify_data(data)
