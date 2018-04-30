# Author: Carter Brown

# Finds the number of "Transitive" Champs from the 17-18 NCAA Basketball Season

# Ex: Villanova won the championship, but Butler beat them earlier in the season, so they are considered
# transitive champs

# All winners were on the left while losers were on the right
teams = [(line[12:line.index("  ", 12, 39)], line[41:line.index("  ", 41, 67)]) for line in open("games.txt")]

winners = ["Villanova"]
new_champ = True

while new_champ:
    new_champ = False
    for game in teams:
        if game[1] in winners:
            if not winners.__contains__(game[0]):
                winners.append(game[0])
                teams.remove(game)
                new_champ = True

print(len(winners))

