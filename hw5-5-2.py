# Author: JD 11/02/2021

string = input("Enter a 6 letters word: ")

odd = (string[1], string[3], string[5])

even = (string[0], string[2], string[4])

odd = "-".join(odd)

even = "-".join(even)

print(odd)

print(even)

