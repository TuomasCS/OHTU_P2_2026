class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        matching = [p for p in self._players
                    if p.nationality == nationality]
        return sorted(matching, key=lambda p: p.points, reverse=True)

    def get_nationalities(self):
        return sorted(set(p.nationality for p in self._players))

    def get_teams(self):
        return sorted(set(p.team for p in self._players))