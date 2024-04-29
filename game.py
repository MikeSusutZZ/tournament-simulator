import random
import copy
import itertools

class Player:
    def __init__(self):
        self.skill = random.randint(10, 100)
        self.con = random.randint(10, 50)
    
    def play(self):
        return self.skill - random.randint(0, self.con)

class Team:
    def __init__(self):
        self.players = [Player() for _ in range(7)]
        self.players.sort(key=lambda x: x.skill, reverse=True)

    def play(self, line):
        lineups = {
            'first': [0, 1, 2],
            'second': [0, 3, 4],
            'third': [1, 5, 6]
        }
        return sum(self.players[i].play() for i in lineups[line])

class League:
    def __init__(self):
        team_names = ["Quantum", "Neon", "Shadows", "Cosmos", "Thunder", 
                      "Voltage", "Eclipse", "Vortex", "Sapphire", "Ironside", 
                      "Celestial", "Galactic", "Inferno", "Blizzard", "Fireborne", "Mystic"]
        self.teams = [Team() for _ in range(16)]
        self.team_dict = {name: team for name, team in zip(team_names, self.teams)}

    def match(self, team1_name, team2_name):
        team1 = self.team_dict[team1_name]
        team2 = self.team_dict[team2_name]
        team1_points = 0
        team2_points = 0
        lineups = ["first"] * 4 + ["second"] * 2 + ["third"] * 1
        for lineup in lineups:
            score1 = team1.play(lineup)
            score2 = team2.play(lineup)
            if score1 > score2:
                team1_points += 1
            else:
                team2_points += 1
        if team1_points > team2_points:
            print(f"{team1_name} wins the match {team1_points}-{team2_points}.")
            return team1_name, team2_name
        else:
            print(f"{team2_name} wins the match {team2_points}-{team1_points}.")
            return team2_name, team1_name

    def full_round_robin(self):
        results = {team: 0 for team in self.team_dict.keys()}
        
        # Generate all possible pairings
        pairings = list(itertools.combinations(self.team_dict.keys(), 2))
        
        for team1, team2 in pairings:
            winner, _ = self.match(team1, team2)
            results[winner] += 1
        
        return results

def main():
    league = League()
    results = league.full_round_robin()
    print(f"")
    for team, wins in sorted(results.items(), key=lambda item: item[1], reverse=True):
        print(f"{team}: {wins} wins")
    # while True:
    #     team1 = input("Team 1: ")
    #     team2 = input("Team 2: ")
    #     try:
    #         league.match(team1, team2)
    #     except:
    #         print(f"you may have misentered a name")
main()
