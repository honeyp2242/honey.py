# Part:1 Use of Built-in Function in Python

# import random

# import the random module to generate random number later.

# print("<==== Built-in Function on List ====>")

# numbers = [4 , 2 , 7 , 9 , 5 , 6]

# print("List : " , numbers)

# len()

# A list named number is defined with 5 integers.

# len() return the number of items in the list

# print("Lenght of List : " , len(numbers))

# max() and min() are used to find the largest and smallest numbers respectively.

# print("Max Numbers : " , max(numbers))

# print("Min Numbers : " , min(numbers))

# sum() adds all value in the list

# print("Sum of List : " , sum(numbers))

# Part:2 Negative Float Number Operation

# print("<==== Part:2 Operation in Negative Value")

# num = float(input("Enter a Negative float Number : "))

# abs() return the positive version from the user

# print("Positive Version From The User : " , abs(num))

# pow() raises the positive Value of the power

# print("Power of Value : " , pow(num , 10))

# round() round of the number to 2 digit after the decimal point

# print("Round of Value : " , round(num))

# Part:3 random List and Its Value / Analysis

print("<=== Random List and Its Value / Analysis ===>")

random_num = random.sample(range(1 , 100) , 5)

print(random_num)

# using max() , and min() , sum() in random value

print("Random Number max count: " , max(random_num))
print("Random Number min count: " , min(random_num))
print("Random Number sum count: " , sum(random_num))

# Part:4 Sort and Reverse a List

# print("<=== Sort and Reverse a List ===>")

# user_list = list(map(int , input("Enter Number seperated by space : ").split()))

# print (user_list)

# sorted() the original user inputs

# reverse() return a reverse a iterator , and list convert in back to a list

# print("Sorted List Ascending", sorted(user_list))

# print("Sorted List Desecending" , sorted(user_list , reverse=True))

# print("Reverse value of List : " , List(reversed(user_list) ))