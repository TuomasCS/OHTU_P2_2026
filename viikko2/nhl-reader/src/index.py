
import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)
    
    finns = [p for p in players if p.nationality == "FIN"]
    finns = sorted(finns, key=lambda p: p.points, reverse=True)

    print("Players from FIN:\n")
    for player in finns:
        print(player)

    def __str__(self):
        return (f"{self.name:20} {self.team:15} "
                f"{self.goals:2} + {self.assists:2} = {self.points:3}")


if __name__ == "__main__":
    main()
