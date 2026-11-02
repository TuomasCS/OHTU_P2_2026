import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),   #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53),  # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)   # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_existing_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_when_player_not_found(self):
        player = self.stats.search("Selanne")

        self.assertIsNone(player)

    def test_team_returns_only_players_of_that_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("XXX"), [])

    def test_top_returns_players_in_points_order(self):
        top = self.stats.top(2)

        self.assertEqual(top[0].name, "Gretzky")  # 124
        self.assertEqual(top[1].name, "Lemieux")  # 99

    def test_top_default_sorts_by_points(self):
        names = [player.name for player in self.stats.top(3)]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_sorted_by_points(self):
        names = [player.name for player in self.stats.top(3, SortBy.POINTS)]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_sorted_by_goals(self):
        names = [player.name for player in self.stats.top(3, SortBy.GOALS)]

        self.assertEqual(names, ["Lemieux", "Yzerman", "Kurri"])

    def test_top_sorted_by_assists(self):
        names = [player.name for player in self.stats.top(3, SortBy.ASSISTS)]

        self.assertEqual(names, ["Gretzky", "Yzerman", "Lemieux"])

    def test_top_returns_requested_number_of_players(self):
        self.assertEqual(len(self.stats.top(3)), 3)

    def test_top_with_too_large_number_returns_all_players(self):
        self.assertEqual(len(self.stats.top(10)), 5)