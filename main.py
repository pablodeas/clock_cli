import click
import time
from datetime import datetime
from playsound import playsound

# > Author:     Pablo Andrade
# > Created:    06/10/2024
# > Version:    0.1

@click.group()
def cli():
    """> A Clock in Terminal."""
    pass

@cli.command(help="> Get the Current Time.")
def now():
    try:
        now_f = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
        click.echo(f"> {now_f}")
    except Exception as e:
        click.echo(f"> {e}")

@cli.command(help="> Counts the Time and makes a Sound at the end.")
@click.argument("seconds", type=int)
def timer(seconds):
    for x in range(seconds):
        click.echo(f"> {x}")
        time.sleep(1)
    playsound("ship_horn.mp3")

if __name__ == "__main__":
    cli()