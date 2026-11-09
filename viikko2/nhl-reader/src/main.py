
"""Main module for displaying NHL player statistics."""

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


AVAILABLE_SEASONS = [ #laiskasti tehty, tiedän, sori
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26"
]

unique_teams = []
def ask_settings():
    """Ask the user to select a season and nationality."""
    print("\nAvailable seasons:")
    print(", ".join(AVAILABLE_SEASONS))

    season = Prompt.ask("Season", default="2024-25")
    nationality = Prompt.ask("Nationality", default="FIN").upper()

    return season, nationality


def build_table(players, season, nationality):
    """Build a table displaying the top scorers."""
    table = Table(title=f"Top scorers of {nationality} {season}")
    table.add_column("Name", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="green")

    for p in players:
        table.add_row(
            p.name,
            p.team,
            str(p.goals),
            str(p.assists),
            str(p.points)
        )

    return table


def main():
    """Run the NHL statistics application."""

    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    stats = PlayerStats(PlayerReader(url))


    print("Available nationalities:")
    print(", ".join(stats.get_nationalities()))

    season, nationality = ask_settings()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    players = stats.top_scorers_by_nationality(nationality)

    Console().print(build_table(players, season, nationality))


if __name__ == "__main__":
    main()
