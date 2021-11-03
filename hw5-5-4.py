# Author: JD 11/02/2021

f_wrd_o = input("Enter the first word: ")

f_wrd = f_wrd_o.lower()

s_wrd_o = input("Enter the second word: ")

s_wrd = s_wrd_o.lower()

t_wrd_o = input("Enter the third word: ")

t_wrd = t_wrd_o.lower()

if f_wrd < s_wrd:
    small = f_wrd
    small_o = f_wrd_o
    big = s_wrd
    big_o = s_wrd_o
else:
    small = s_wrd
    small_o = s_wrd_o
    big = f_wrd
    big_o = f_wrd_o
    
if t_wrd < small:
    smallest = t_wrd_o
    middle = small_o
    biggest = big_o
elif t_wrd > big:
    biggest = t_wrd_o
    middle = big_o
    smallest = small_o
else:
    middle = t_wrd_o
    biggest = big_o
    smallest = small_o

print(smallest, middle, biggest)

