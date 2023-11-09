#Object oriented programming is a computer programming is a computer programming model that organizes software design around data, or objects, rather than functions and logic.
#Advantages
#Troubleshooting is easier with the OOP language.
#Code Reusability.
#Productivity.
#Data Redundancy.
#Code Flexibility.
#Solving problems.
#Security.
#A class is a template for objects.
#A class is an instance of a class.

#Create a user class with properties name, age, location.
class About:
  def __init__(self, name, age, location):
    print("Hello,i am")
    self.name = name
    self.age = age
    self.location =location

About1 = About("Allen", 30, "kira")

print(About1.name)
print(About1.age)
print(About1.location)

#Create a new instance of the user class(a new object).
 
About2= About("Emily", 34, "Kampala")
print(About2.name)
print(About2.age)
print(About2.location)

#Access the username and age
About = About1.name
About = About1.age

print(f"User name: {About1.name}")
print(f"Age: {About1.age}")

#Create a function for the user class that points a user's function.
def my_location(my):
  print("MY location:",my)
my_location("Kira")