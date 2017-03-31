import csv

faculty = csv.DictReader(open('faculty.csv'), delimiter=',')
emails = list(line[' email'] for line in faculty)

a = csv.writer(open('emails.csv', 'w'))

for i in emails:
    print(i)
    a.writerow([i])
