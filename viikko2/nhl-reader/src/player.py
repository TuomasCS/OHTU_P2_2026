
class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.nationality = data["nationality"]
        self.team = data["team"]
        self.goals = data["goals"]
        self.assists = data["assists"]

    def __str__(self):
        return (f"{self.name} team {self.team}  "
                f"goals {self.goals} assists {self.assists}")