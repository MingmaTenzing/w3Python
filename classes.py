# class Person: 
#     def __init__(person, name, age, gender):
#         person.name = name
#         person.age= age
#         person.gender = gender
    
#     def __str__(person):
#         return f"{person.name, person.age, person.gender}"
    
#     def details(person):
#         return print(f"User is {person.name}, age is {person.age}, and the gender is {person.gender}")
        
# p1 = Person('Mingma', 24, 'male')

# p1.age = 20
# del p1
# p1.details()



# inheritance
class Person: 
    def __init__(person, firstname, lastname):
        person.firstname = firstname
        person.lastname = lastname
    
    def printName(person):
        print(person.firstname, person.lastname)
        

p1 = Person("Mingma", "Sherpa")

p1.printName()


# creating child classs
class Student(Person):
    def __init__(person, firstname, lastname, year):
        super().__init__(firstname, lastname)
        person.year = year
    
    def printStudent_details(student):
        print(student.firstname, student.lastname, student.year)

s1 = Student("Pasang", "Sherpa",201) 

s1.printStudent_details()