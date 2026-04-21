# Create a simple class to represent a person
class Person():
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def speak(self):
        print(f"Hi. My name is {self.first_name} {self.last_name}.")

p1 = Person("George", "Washington")
p1.speak()

p2 = Person("John", "Adams")
p2.speak()

p3 = Person("Thomas", "Jefferson")
p3.speak()