age = 10
name = 'Aneesh'
male = True
print("My name is {}".format(name))
print(f"My name is {name}")
if age > 18:
    print("Adult")
else:
    print("Not adult")
if male:
    print("Male")
""" multi line comment
To test
"""
#single line comment
def hello(message):
    #print(f"Hello {message}!")
    print("Hello " + message)
hello("World")
hello("Blue planet")


dognames = ['Fido','Sean',True, 23]
print(dognames)
dognames.insert(1, "Sally")
print(dognames)

for dogname in dognames:
    print(dogname)
dog_dictonory = {"Fido": 25, "Sean": 45}
print(dog_dictonory)

    