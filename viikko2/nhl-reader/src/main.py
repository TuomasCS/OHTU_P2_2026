
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

def ask_settings():
    """Ask the user to select a season."""
    print("\nAvailable seasons:")
    print(", ".join(AVAILABLE_SEASONS))

    season = Prompt.ask("Season", default="2024-25")
    return season


def build_table(players, season, selection):
    """Build a table displaying the top scorers."""
    table = Table(title=f"Top scorers of {selection} {season}")
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

    season = ask_settings()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    selection_type = Prompt.ask(
        "Search by",
        choices=["nationality", "team"],
        default="nationality",
    )

    if selection_type == "team":
        choices = stats.get_teams()
        print("\nAvailable teams:")
        print(", ".join(choices))
        selection = Prompt.ask("Team", choices=choices)
        players = stats.top_scorers_by_team(selection)
    else:
        choices = stats.get_nationalities()
        print("\nAvailable nationalities:")
        print(", ".join(choices))
        selection = Prompt.ask(
            "Nationality",
            choices=choices,
            default="FIN" if "FIN" in choices else choices[0],
        )
        players = stats.top_scorers_by_nationality(selection)

    Console().print(build_table(players, season, selection))


if __name__ == "__main__":
    main()
