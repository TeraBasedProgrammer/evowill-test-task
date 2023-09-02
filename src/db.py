import sqlite3

from rich.console import Console


# Custom exception to handle bored API response error
class ActivityNotFountException(Exception):
    pass


class DataLayer:
    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)

        with self.conn as conn:
            conn.execute(
                """CREATE TABLE IF NOT EXISTS activities(id INT PRIMARY KEY, title TEXT, type VARCHAR(50), participants INT, price REAL, link TEXT NULL, accessibility REAL);"""
            )

    def insert_activity(self, activity_data: dict) -> None:
        """Inserts given activity into the database

        Args:
            activity_data (dict): json data received from bored API

        Raises:
            ActivityNotFountException: raised if json response contains error
        """

        if activity_data.get("error") is not None:
            raise ActivityNotFountException()

        with self.conn as conn:
            try:
                conn.execute(
                    """INSERT INTO activities VALUES (?, ?, ?, ?, ?, ?, ?);""",
                    (
                        activity_data["key"],
                        activity_data["activity"],
                        activity_data["type"],
                        activity_data["participants"],
                        activity_data["price"],
                        activity_data["link"],
                        activity_data["accessibility"],
                    ),
                )
            except sqlite3.IntegrityError:
                console = Console()
                console.print("Warning: ", style="yellow", end="")
                console.print("This activitity has already been added to the database")

    def get_activities(self) -> list[dict]:
        """Returns 5 last activities from the database

        Returns:
            list[dict]: db rows converted into dictionaries
        """
        with self.conn as conn:
            cur = conn.cursor()
            data = cur.execute(
                """SELECT * FROM activities ORDER BY ROWID DESC LIMIT 5;"""
            )

            result_data = []
            for row in data.fetchall():
                row_dict = {
                    "key": row[0],
                    "activity": row[1],
                    "type": row[2],
                    "participants": row[3],
                    "price": row[4],
                    "link": row[5],
                    "accessibility": row[6],
                }
                result_data.append(row_dict)

            return result_data
