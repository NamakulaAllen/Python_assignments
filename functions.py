#Fuctions without parameters
#def means define
def my_name():
    print("Allen")


def my_school():
    print("WITU")
#Calling the function so that items so that it performs its purpose
my_name()
my_school()

#Arguements/functions with parameters
#Create a function that multiplies two numbers a and b wher a=3 and b=10
def product_of_two_numbers(a, b):
    output = a*b
    print(f"The product of {a} and {b} is {output}")

product_of_two_numbers(3, 10)
product_of_two_numbers(5, 12)
product_of_two_numbers(3, 19)

#Create a funtion that returns your name and your age
def my_name_and_age(name,age):
    print(f"My name is {name} and i am {age} years of age")
my_name_and_age("Allen", 17)

#Create a function that finds the maximun function of three numbers
#a=70, b=80, c=65
def maximum_number(a, b, c):
    if a>b and a>c:
        print("{a} is greater than {b} and {c}")
    elif b>a and b>c:
        print(f"{b} must be greater than {a} and {c}")
    else:
        print(f"{c} is greter than {a} and {b}")
maximum_number(90,80,65)

#Write a python program to sum all numbers in a list
