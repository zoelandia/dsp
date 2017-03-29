# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

stats = csv.DictReader(open('football.csv'), delimiter=',')

smallest_diff = 99999
team = []

for line in stats:
    this_diff = abs(int(line['Goals'])-int(line['Goals Allowed']))
    if this_diff < smallest_diff:
        smallest_diff = this_diff
        team = line['Team']
    elif this_diff == smallest_diff:    #CYA!
        team.append(line['Team'])

print(team, ": ", smallest_diff)
