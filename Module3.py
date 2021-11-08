# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:12:16 2021

@author: Wujian
"""
# 3.1.1.2 Making decisions in Python: Equality: the equal to operator (==)
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)


# 
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# 3.1.1.9 Making decisions in Python

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)


# 3.1.1.10 LAB: Comparison operators and conditional execution
x = input()
if (x == 'Spathiphyllum'): print("Yes - Spathiphyllum is the best plant ever")
elif (x == 'spathiphyllum'): print("No, I want a big Spathiphyllum!")
else : print("Spathiphyllum! Not", x)

# 3.1.1.11 LAB: Essentials of the if-else statement

income = float(input("Enter the annual income: "))

#
# Write your code here.
#

if income <= 85528 : tax = (income) * .18 - 556.02
else : tax = 14839 + (income - 85528) * .32

tax = round(tax, 0)
if (tax < 0) : tax = 0.0

print("The tax is:", tax, "thalers")

# 3.1.1.12 LAB: Essentials of the if-elif-else statement

year = int(input("Enter a year: "))

#
# Write your code here.
#	
if year <= 1582 : print("Not within the Gregorian calendar period")
elif year %   4 != 0: print("common year")
elif year % 100 != 0: print('leap year')
elif year % 400 != 0: print('common year')
else : print ("leap year")


# 3.1.1.14 SECTION SUMMARY (2/2)
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")



# 3.2.1.1 Loops in Python | while
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# 3.2.1.2 Loops in Python | while
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


# 3.2.1.3 LAB: Essentials of the while loop - Guess the secret number
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Input a number
number = int(input("Enter a number: "))

# If the number is not equal to -1, continue.
while number != secret_number:
    # If the number chosen by the user is different than the magician's secret number
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter a number again: "))

# Print the largest number.
print("Well done, muggle! You are free now.")


power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2


# 3.2.1.6 LAB: Essentials of the for loop - counting mississippily
import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

for i in range(1,6):
    print(i,"Mississippi")
    time.sleep(1)

# 3.2.1.7 Loop control in Python | break and continue
# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")    
    
# 3.2.1.8 Loop control in Python | break and continue

# break
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# continue    
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# 3.2.1.9 LAB: The break statement - Stuck in a loop
secret_word = "chupacabra"

# Input a word
number = input("Enter a word: ")

# If the number is not equal to -1, continue.
while number != secret_word:
    # If the number chosen by the user is different than the magician's secret number
    print("Ha ha! You're stuck in my loop!")
    number = input("Enter a word again: ")

# Print the largest number.
print("You've successfully left the loop.")    

# 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater
# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A" : continue
    elif  letter == "E": continue
    elif  letter == "I": continue
    elif  letter == "O": continue
    elif  letter == "U": continue
    print(letter)


# 3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater
user_word = input("Enter a word: ")
word_without_vowels = ""
user_word = user_word.upper()
# Prompt the user to enter a word
# and assign it to the user_word variable.

for letter in user_word:
    # Complete the body of the loop.
    if letter == "A" : continue
    elif  letter == "E": continue
    elif  letter == "I": continue
    elif  letter == "O": continue
    elif  letter == "U": continue
    else : word_without_vowels += letter


# Print the word assigned to word_without_vowels.
print(word_without_vowels)


# 3.2.1.12 Python loops | else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
    

# 3.2.1.13 Python loops | else
    
for i in range(5):
    print(i)
else:
    print("else:", i)
    
    
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
    
    
# 3.2.1.14 LAB: Essentials of the while loop
  
blocks = int(input("Enter the blocks : "))

i=1
layer=1
height=0

while i < blocks + 1:
    height += layer
    if height > blocks:
        print(layer-1)
        break
    i += 1
    layer += 1
    

# 3.2.1.15 LAB: Collatz's hypothesis

c0 = int(input("Enter the c0 : "))

i = 0
while c0 != 1.0:
    if c0 % 2 == 0 : c0 = c0/2
    else: c0 = 3 * c0 + 1
    print(c0)
    i += 1
print('steps=',i)


# 3.2.1.16 SECTION SUMMARY (1/2)

# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

# 3
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

# 4
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

# 3.2.1.17 SECTION SUMMARY (2/2)
"""
Exercise 1
Create a for loop that counts from 0 to 10, 
and prints odd numbers to the screen. Use the skeleton below:
"""
for i in range(1, 11):
    if i % 2 != 0:   print(i)
    
"""
Exercise 2
Create a while loop that counts from 0 to 10,
 and prints odd numbers to the screen. Use the skeleton below:
"""

x = 1
while x < 11:
    if x % 2 != 0:   
        print(x)
    x += 1
    
"""
Exercise 3
Create a program with a for loop and a break statement. 
The program should iterate over characters in an email address, 
exit the loop when it reaches the @ symbol, 
and print the part before @ on one line. Use the skeleton below:
"""    
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
    
"""
Exercise 4
Create a program with a for loop and a continue statement. 
The program should iterate over a string of digits, 
replace each 0 with x, and print the modified string to the screen. 
Use the skeleton below:
"""
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

    
"""
Exercise 5
Create a program with a for loop and a continue statement. 
The program should iterate over a string of digits, 
replace each 0 with x, and print the modified string to the screen. 
Use the skeleton below:
"""

# 3.3.1.2 Logic and bit operations in Python | and, or, not

# Example 1:
var = 1
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))


i = 1
j = not not i
print(j)


x = 3
y = 7

if (y > 1 and y > x) : print("y is greater than 1 AND x")

z = x & y
print(z)

# 3.3.1.5 Logic and bit operations in Python | Bit shifting
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)


# 3.3.1.6 SECTION SUMMARY

#Exercise 1
#What is the output of the following snippet?

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

#Exercise 2
#What is the output of the following snippet?

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)


x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
