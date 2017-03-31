import csv
import string
import re

# Q1: Degrees and frequencies

faculty = csv.DictReader(open('faculty.csv'), delimiter=',')

degrees = [line[' degree'].split() for line in faculty]
degrees = sorted(d.replace('.', '') for degree_list in degrees for d in degree_list)

counting = {}
for i in degrees:
    if i in counting:
        counting[i] += 1
    elif i not in counting and not(i.isdigit()):
        counting.update({i: 1})

print(counting)
print(len(counting), "degrees")

# Oops, I thought we had to find the degree that occurred the most:
"""
counter = 0
degree = []
for i, j in counting.items():
    if j > counter:
        counter = j
        degree = [i]
    elif j == counter:
        counter = j
        degree.append(i)

print(degree, ": ", counter)
"""

# Q2: Titles and frequencies

faculty = csv.DictReader(open('faculty.csv'), delimiter=',')

titles = sorted(line[' title'] for line in faculty)

# I tried to correct for the errant "Assistant Professor is Biostatistics" title, but I couldn't
# get it to work, so I just adjusted my answer manually. Here's what I was going for:
# titles = d.split().replace(i for i in d if i < len(3), '').join(" ") for d in titles

counting = {}
for i in titles:
    if i in counting:
        counting[i] += 1
    elif i not in counting:
        counting.update({i: 1})

print(counting)
print(len(counting), "titles")


# Q3: List of email addresses

faculty = csv.DictReader(open('faculty.csv'), delimiter=',')

emails = [line[' email'] for line in faculty]

print(emails)

# Q4: List of unique domains

faculty = csv.DictReader(open('faculty.csv'), delimiter=',')
domains = sorted(email[email.index("@"):] for email in emails)

domains_unique = [domains[0]]
for i in domains:
    if i != domains_unique[-1]:
        domains_unique.append(i)

print(domains_unique)
print(len(domains_unique), "unique domains")
