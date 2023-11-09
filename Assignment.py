#Write a python program to sum all numbers in a list
#List = (8, 2, 3, 0, 7)
def sum(numbers):
    total = 0
    for m in numbers:
        total += m
    return total
print(sum((8, 2, 3, 0, 7)))

#Write a python program to multiply all numbers in a list
#list = (8, 2, 3,-1, 7)
def multiply(numbers):
    total = 1
    for m in numbers:
        total *= m
    return total
print(multiply((8, 2, 3, -1, 7))) 

#Write a python program to reverse a string
#String =(1, 2, 3, 4, a, b, c, d)
def string_reverse(str1):

    index = len(str1)
    rstr1 = ''
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))

#Write a python program to print the even number from
#list =(1, 2, 3, 4, 5, 6, 7, 8, 9)
def is_even_numbers(l):
    even_numbers = []
    for m in l:
        if m % 2 == 0:
            even_numbers.append(m)
    return even_numbers
print(is_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))