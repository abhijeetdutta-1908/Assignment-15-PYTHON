class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self):
        print(f"Hey Buddy,My name is {self.name},I am {self.age} years old and I am a {self.gender}.")

person1 = Person("Abhijeet Dutta", 20, "Male")
person1.introduce()
