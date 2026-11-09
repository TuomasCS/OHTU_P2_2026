"""Tests for PlayerStats."""

import unittest
from types import SimpleNamespace

from player_stats import PlayerStats


class PlayerReaderStub:  # pylint: disable=too-few-public-methods
    """Provide players without making an HTTP request."""

    def __init__(self, players):
        self._players = players

    def get_players(self):
        """Return the stubbed players."""
        return self._players


class PlayerStatsTest(unittest.TestCase):
    """Tests for player statistics queries."""

    def setUp(self):
        self.players = [
            SimpleNamespace(
                name="Player One",
                nationality="FIN",
                team="AAA",
                points=30,
            ),
            SimpleNamespace(
                name="Player Two",
                nationality="SWE",
                team="BBB",
                points=50,
            ),
            SimpleNamespace(
                name="Player Three",
                nationality="FIN",
                team="AAA",
                points=40,
            ),
        ]
        self.stats = PlayerStats(PlayerReaderStub(self.players))

    def test_top_scorers_by_nationality_are_sorted_by_points(self):
        """Filter by nationality and sort the result by points."""
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in result],
            ["Player Three", "Player One"],
        )

    def test_top_scorers_by_team_are_sorted_by_points(self):
        """Filter by team and sort the result by points."""
        result = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(
            [player.name for player in result],
            ["Player Three", "Player One"],
        )

    def test_top_scorers_return_empty_list_for_unknown_group(self):
        """Return an empty list when there are no matching players."""
        self.assertEqual(self.stats.top_scorers_by_nationality("NOR"), [])
        self.assertEqual(self.stats.top_scorers_by_team("CCC"), [])

    def test_get_nationalities_returns_unique_sorted_values(self):
        """Return unique nationalities in alphabetical order."""
        self.assertEqual(self.stats.get_nationalities(), ["FIN", "SWE"])

    def test_get_teams_returns_unique_sorted_values(self):
        """Return unique teams in alphabetical order."""
        self.assertEqual(self.stats.get_teams(), ["AAA", "BBB"])


if __name__ == "__main__":
    unittest.main()
