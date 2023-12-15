""" 6.a. Create a dictionary representing a library catalog with book titles as keys and values as dictionaries c
ontaining information like author, publication year, and genre.
b. Add a new book to the catalog and update the author of an existing book.
c. Write a function to count how many books in the catalog were published before a given year. """

books={
    "My play of justice":{"author":"Dr. kaushik chaudhary","publication year":1991,"genre":"mystery"},
    "cold blooded love":{"author":"Girish dutt shukla","publication year":2012,"genre":"fantacy"},
    "Arya":{"author":"shivakumar GV","publication year":1999,"genre":"Historical"},
    "Rama of the Axe":{"author":"Rnjith Radhakrishnan","publication year":2000,"genre":"Historical"},
    "Vahana":{"author":"stuti gupth","publication year":1975,"genre":"mystery"},
    "vedanta":{"author":"swami vivekananda","publication year":1983,"genre":"Action"},
    "The Guide":{"author":"Rk narayanan","publication year":1998,"genre":"Adventure"}
}
# Add a new book to the catalog
newbook={"malgudy days":{"author":"RK narayan","publication year":1943,"genre":"portrait"}}
books.update(newbook)
print("New book added: ",books,"\n")

# update the author of an existing book
for k,v in books.items():
    if k=="The Guide":
        v["author"]="MULK RAJ ANAND"
print("Author updated: ",books,"\n")

# Write a function to count how many books in the catalog were published before a given year.
def yearcount(years,date):
    count = 0
    for y in years:
        if y < date:
            count += 1
    return count
years=[]
for b,v in books.items():

    years.append(v["publication year"])
count=yearcount(years,2020)
print("Books that published before 2020:",count)

"""
OUTPUT
New book added:  {'My play of justice': {'author': 'Dr. kaushik chaudhary', 'publication year': 1991, 'genre': 'mystery'}, 'cold blooded love': {'author': 'Girish dutt shukla', 'publication year': 2012, 'genre': 'fantacy'}, 'Arya': {'author': 'shivakumar GV', 'publication year': 1999, 'genre': 'Historical'}, 'Rama of the Axe': {'author': 'Rnjith Radhakrishnan', 'publication year': 
2000, 'genre': 'Historical'}, 'Vahana': {'author': 'stuti gupth', 'publication year': 1975, 'genre': 'mystery'}, 'vedanta': {'author': 'swami vivekananda', 'publication year': 1983, 'genre': 'Action'}, 'The Guide': {'author': 'Rk narayanan', 'publication year': 1998, 'genre': 'Adventure'}, 'malgudy days': {'author': 'RK narayan', 'publication year': 1943, 'genre': 'portrait'}}     

Author updated:  {'My play of justice': {'author': 'Dr. kaushik chaudhary', 'publication year': 1991, 'genre': 'mystery'}, 'cold blooded love': {'author': 'Girish dutt shukla', 'publication year': 2012, 'genre': 'fantacy'}, 'Arya': {'author': 'shivakumar GV', 'publication year': 1999, 'genre': 'Historical'}, 'Rama of the Axe': {'author': 'Rnjith Radhakrishnan', 'publication year': 
2000, 'genre': 'Historical'}, 'Vahana': {'author': 'stuti gupth', 'publication year': 1975, 'genre': 'mystery'}, 'vedanta': {'author': 'swami vivekananda', 'publication year': 1983, 'genre': 'Action'}, 'The Guide': {'author': 'MULK RAJ ANAND', 'publication year': 1998, 'genre': 'Adventure'}, 'malgudy days': {'author': 'RK narayan', 'publication year': 1943, 'genre': 'portrait'}}   

Books that published before 2020: 8
"""