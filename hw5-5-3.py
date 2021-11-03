# Author: JD 11/02/2021

string = input("Enter a word: ")

x = len(string) - 1

forward = string[0:]


backward = string[::-1]

if forward == backward:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")

