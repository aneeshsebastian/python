class Dog:
    info = "Some info"
    def __init__(self, name, age, color):
        self.name =  name
        self.age = age
        self.color = color
    def bark(self,age):
        print(f"BARK! {age}")
mydog = Dog('Ram', 25, "Black")
mydog.bark(10)

mydog.name = "One name"
print(mydog.name)
print(mydog.info)
print(Dog.info)
    