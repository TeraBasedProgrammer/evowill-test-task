import typer
from rich.console import Console

from src.db import ActivityNotFountException
from src.wrapper import Wrapper

wrapper = Wrapper()
app = typer.Typer()


@app.command()
def list() -> None:
    """CLI command that displays 5 last activities from the database"""
    wrapper.get_last_activities()


@app.command()
def new(
    type: str = typer.Option(default=""),
    participants: str = typer.Option(default=""),
    price_min: str = typer.Option(default=""),
    price_max: str = typer.Option(default=""),
    accessibility_min: str = typer.Option(default=""),
    accessibility_max: str = typer.Option(default=""),
) -> None:
    """CLI command that displays random activity and saves it in the database

    Args:
        type (str, optional): activity type. Defaults to typer.Option(default="").
        participants (str, optional): number of participants. Defaults to typer.Option(default="").
        price_min (str, optional): minimum price. Defaults to typer.Option(default="").
        price_max (str, optional): maximum price. Defaults to typer.Option(default="").
        accessibility_min (str, optional): minimum accessibility. Defaults to typer.Option(default="").
        accessibility_max (str, optional): maximum accessibility. Defaults to typer.Option(default="").
    """
    try:
        wrapper.get_random_activity(
            type=type,
            participants=participants,
            minprice=price_min,
            maxprice=price_max,
            minaccessibility=accessibility_min,
            maxaccessibility=accessibility_max,
        )
    except ActivityNotFountException:
        console = Console()
        console.print("Error: ", end="", style="red")
        console.print("No activity found with the specified parameters")


if __name__ == "__main__":
    app()
