# Isaac Trevathan
# 1955674

class Team:

    # constructor that initializes teamname team_wins and team_losses
    def __init__(self):
        self.teamname = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # creates function for turning the team_wins and team_losses into floats
    # then getint the wins divided by the sum of the wins and the losses
    def get_win_percentage(self):

        wins = float(self.team_wins)
        losses = float(self.team_losses)

        result = wins / float(wins + losses)

        return result


if __name__ == "__main__":

    # creates and instance of class Team()
    my_team = Team()

    # gets input for team name
    my_name = input()

    # gets input for team_wins
    my_wins = input()

    # gets input for team_losses
    my_losses = input()

    # sets the  team_wins equal to my_wins
    my_team.team_wins = my_wins

    # sets the  team_losses equal to my_losses
    my_team.team_losses = my_losses

    # sets the teamname equal to my_name
    my_team.teamname = my_name

    # sets middle equal to the win percentage, calls get_win_percentage function
    middle = my_team.get_win_percentage()

    # number to check if middle is greater than or equal to 0.5
    point_five_zero = 0.5

    # if middle is greater than or equal to 0.5 it prints that the team has a winning average
    # if middle is not greater than or equal to 0.5 it prints that the team has a loosing average
    if middle >= point_five_zero:
        print('Congratulations, Team', my_name, 'has a winning average!')
    else:
        print('Team', my_name, 'has a losing average.')
