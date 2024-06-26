import random
import itertools
import pickle


class Player:
    def __init__(self):
        self.skill = random.randint(10, 100)
        self.con = random.randint(10, 50)

    def play(self):
        return self.skill - random.randint(0, self.con)

class Team:
    def __init__(self):
        self.players = [Player() for _ in range(7)]
        self.sort_players()
        self.wins = 0
        self.losses = 0

    def sort_players(self):
        self.players.sort(key=lambda player: player.skill, reverse=True)

    def replace_random_player(self):
        if self.players:
            random_index = random.randint(0, len(self.players) - 1)
            self.players.pop(random_index)
        self.players.append(Player())
        self.sort_players()

    def play(self, line):
        if line == "first":
            players_to_play = [0, 1, 2]  # indexes of players in the team
        elif line == "second":
            players_to_play = [0, 3, 4]
        elif line == "third":
            players_to_play = [1, 5, 6]
        return sum(self.players[i].play() for i in players_to_play)

class League:
    def __init__(self):
        team_names = ["Quantum", "Neon", "Shadows", "Cosmos", "Thunder", "Voltage", "Eclipse", "Vortex", "Sapphire", "Ironside", "Celestial", "Galactic", "Inferno", "Blizzard", "Fireborne", "Mystic"]
        self.teams = [Team() for _ in range(len(team_names))]
        self.team_dict = {name: team for name, team in zip(team_names, self.teams)}

    def update_teams(self):
        print("Updating teams")
        for team in self.teams:
            team.replace_random_player()
            team.sort_players()
            team.wins = 0
            team.losses = 0

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
                print(f"{team1_name} scored")
            else:
                team2_points += 1
                print(f"{team2_name} scored")

        if team1_points > team2_points:
            print(f"{team1_name} wins the match against {team2_name} {team1_points}-{team2_points}.")
            team1.wins += 1
            team2.losses += 1
            return team1_name, team2_name
        else:
            print(f"{team2_name} wins the match against {team1_name} {team2_points}-{team1_points}.")
            team1.losses += 1
            team2.wins += 1
            return team2_name, team1_name


    def round_robin(self):
        """Generate round robin matches"""

        # Create a list of matches, excluding self-play
        matchups = list(itertools.combinations(self.team_dict, 2))
        random.shuffle(matchups)
        for match in matchups:
            self.match(*match)
            

def save_league_state(league):
        """
        Save the state of the league to a file using pickle.

        Args:
        league (League): The league object to be saved.
        filename (str): The name of the file where the league state will be saved.
        """
        with open("save", 'wb') as f:
            pickle.dump(league, f)

def load_league_state():
        """
        Load the state of the league from a file using pickle.

        Args:
        filename (str): The name of the file from which to load the league state.

        Returns:
        League: The loaded league object.
        """
        with open("save", 'rb') as f:
            return pickle.load(f)




def main():
    while True:
        league = load_league_state()
        team1 = input("team1: ")
        if team1 == "r":
            league.update_teams()
        if team1 == "s":
            save_league_state(league)
            break
        team2 = input("team2: ")
        if team2 == "p":
            league.round_robin()
            sorted_teams = sorted(league.team_dict.items(), key=lambda item: item[1].wins, reverse=True)
            # Display results
            print("\n\nResults\n")
            for name, team in sorted_teams:
                print(f"{name}: {team.wins} Wins, {team.losses} Losses")
        try: league.match(team1, team2)
        except: print("misinput")

if __name__ == "__main__":
    main()

        
        