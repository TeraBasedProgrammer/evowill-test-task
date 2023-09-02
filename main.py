from typing import Optional

import typer
from rich.console import Console

from db import ActivityNotFountException
from wrapper import Wrapper

wrapper = Wrapper()
app = typer.Typer()


@app.command()
def list() -> None:
    """CLI command that displays 5 last activities from the database
    """    
    wrapper.get_last_activities()


@app.command()
def new(
    type: Optional[str] = typer.Option(default=""),
    participants: Optional[int] = typer.Option(default=""),
    price_min: Optional[float] = typer.Option(default=""),
    price_max: Optional[float] = typer.Option(default=""),
    accessibility_min: Optional[float] = typer.Option(default=""),
    accessibility_max: Optional[float] = typer.Option(default=""),
) -> None:
    """CLI command that displays random activity and saves it in the database

    Args:
        type (Optional[str], optional): activity type. Defaults to typer.Option(default="").
        participants (Optional[int], optional): number of participants. Defaults to typer.Option(default="").
        price_min (Optional[float], optional): minimum price. Defaults to typer.Option(default="").
        price_max (Optional[float], optional): maximum price. Defaults to typer.Option(default="").
        accessibility_min (Optional[float], optional): minimum accessibility. Defaults to typer.Option(default="").
        accessibility_max (Optional[float], optional): maximum accessibility. Defaults to typer.Option(default="").
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
