

import csv
field_names = ['language','name','rating','year','genres']
movies = [
    {"language": "malayalam", "name": "2018", "rating": 5, "year": 2023, "genres": ["mystery"]},
    {"language": "malayalam", "name": "aadujeevitahm", "rating": 5, "year": 2023, "genres": ["fiction", "drama"]},
    {"language": "malayalam", "name": "neymar", "rating": 4, "year": 2023, "genres": ["action", "comedy", "romance"]},
    {"language": "malayalam", "name": "sunny", "rating": 4, "year": 2022, "genres": ["drama", "thriller"]},
    {"language": "malayalam", "name": "12th man", "rating": 3, "year": 2022, "genres": ["drama", "thriller"]},
    {"language": "thamil", "name": "vikram", "rating": 5, "year": 2022, "genres": ["action", "thriller"]},
    {"language": "thamil", "name": "jai bhim", "rating": 5, "year": 2021, "genres": ["mystery", "crime"]},
    {"language": "hindi", "name": "pathaan", "rating": 5, "year": 2023, "genres": ["action", "thriller"]},
    {"language": "telungu", "name": "kgf", "rating": 5, "year": 2018, "genres": ["action", "romance", "thriller"]}
]
#print(movies)
with open('movies.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(movies)
print('All movies')
print("___________")
with open('movies.csv', 'r',newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"])
csvfile.close()

with open('movies.csv', 'r',newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ra=row["rating"]
        #print(ra)
        top_rating=max(ra)
        print(top_rating)
csvfile.close()



