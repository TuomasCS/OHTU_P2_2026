
"Class Player vro"
class Player:
    "Class Player vro"
    def __init__(self, data):
        self.name = data["name"]
        self.nationality = data["nationality"]
        self.team = data["team"]
        self.goals = data["goals"]
        self.assists = data["assists"]

    @property
    def points(self):
        "defines points"
        return self.goals + self.assists

    def __str__(self):
        "str"
        return (f"{self.name:20} {self.team:15} "
                f"{self.goals:2} + {self.assists:2} = {self.points:3}")
