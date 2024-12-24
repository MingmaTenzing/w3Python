class Person: 
    def __init__(self, name, age, gender):
        self.name = name
        self.age= age
        self.gender = gender
    
    def __str__(self):
        return f"{self.name, self.age, self.gender}"
    
    def details(self):
        return print(f"User is {self.name}, age is {self.age}, and the gender is {self.gender}")
        
p1 = Person('Mingma', 24, 'male')

p1.details()



