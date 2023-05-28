#Section 9: Python Functions, Loops & more Data Types

#Lesson 11 - Enumerate function project number 1 :

countries_and_capitals = [
("Afghanistan", "Kabul"),
("Albania", "Tirana"),
("Algeria", "Algiers"),
("Andorra", "Andorra la Vella"),
("Angola", "Luanda"),
("Antigua and Barbuda", "Saint John's"),
("Argentina", "Buenos Aires"),
("Armenia", "Yerevan"),
("Australia", "Canberra"),
("Austria", "Vienna"),
("Azerbaijan", "Baku"),
("Bahamas", "Nassau"),
("Bahrain", "Manama"),
("Bangladesh", "Dhaka")
]


for i, (country, capital) in enumerate(countries_and_capitals):
    print(f"{i.zfill(2)}. {country}: {capital}")



#Section 9: Python Functions, Loops & more Data Types

#Lesson 11 - Enumerate function project number 2 :


sentences = [
'Hello from Codezilla',
'Python Course is awesome',
'I enjoy learning Python with Codezilla'
]

for index, string in enumerate(sentences):
    string = string.replace(" ", "-").upper()
    sentences[index] = string
print(sentences)


#Section 9: Python Functions, Loops & more Data Types

#Lesson 11 - Enumerate function project number 3 :

books = [
("The 7 Habits of Highly Effective People", "Stephen R.Covey"),
("How to Win Friends and Influence People", "DaleCarnegie"),
("Atomic Habits", "James Clear"),
("The 4-Hour Work Week", "Tim Ferriss"),
("Deep Work", "Cal Newport"),
("So Good They Can't Ignore You", "Cal Newport"),
 ("Digital Minimalism", "Cal Newport")
]

for index, [book, Author] in enumerate(books):
    
    print(f'{index+1}. Book: {book} - Author: {Author}')