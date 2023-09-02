import typer
from rich.console import Console

from wrapper import Wrapper

from db import ActivityNotFountException


wrapper = Wrapper()
app = typer.Typer()


@app.command()
def list():
    wrapper.get_last_activities()


@app.command()
def new(
    type: str = typer.Option(default=""),
    participants=typer.Option(default=""),
    price_min=typer.Option(default=""),
    price_max=typer.Option(default=""),
    accessibility_min=typer.Option(default=""),
    accessibility_max=typer.Option(default=""),
) -> None:
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
