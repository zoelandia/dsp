import csv
from collections import defaultdict

# Q6

faculty = csv.DictReader(open('faculty.csv'), delimiter=',')

faculty_dict = {}
for row in faculty:
    name = row['name'].split()[-1]
    if name in faculty_dict:
        faculty_dict[name].append([row[' degree'], row[' title'], row[' email']])
    else:
        faculty_dict[name] = [[row[' degree'], row[' title'], row[' email']]]

print(faculty_dict)

# Q7

faculty = csv.DictReader(open('faculty.csv'), delimiter=',')

professor_dict = {}
for row in faculty:
    name = (row['name'].split()[0], row['name'].split()[-1])
    professor_dict[name] = [[row[' degree'], row[' title'], row[' email']]]

print(professor_dict)

# Q8

faculty = csv.DictReader(open('faculty.csv'), delimiter=',')

from collections import OrderedDict

by_first = sorted(professor_dict.items(), key=lambda t: t[0])

print(by_first)
