# Author: JD 11/02/2021

string = input("Enter a string: ")

length = len(string)

half = length // 2

first_half = string[:half]

second_half = string[half:]

print(first_half)

print(second_half)
