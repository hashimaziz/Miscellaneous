import random
from datetime import date
Cipher_Date = date.today()
DateStrWeird = Cipher_Date.strftime("%D/%M/%Y")
DateStr = Cipher_Date.strftime("%D")
day = DateStr[3:5]
month = DateStr[0:2]
year = DateStr[6:8] # arbitrary?

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

empty_alpha = [None] * 26 # length stays the same
everyOther = int(month) # will most likely come from the date

caesarShift = int(day)

simple = input("String: ") #string to encode
simple = simple.lower() # make sure the string can be encoded
encoded = ""

# shifts the alphabet according to date 
for i in range(26): 
    if i % everyOther == 0:
        insertion_point = i + 2
        if insertion_point > 25:
            insertion_point = (i + 2) - 25
        empty_alpha.insert(insertion_point, alpha[i])
    else:
        empty_alpha.insert(i, alpha[i])
for element in empty_alpha:
        empty_alpha.remove(None)

print(empty_alpha)
for i in range(caesarShift + 1):
    shiftedLet = empty_alpha[i]
    empty_alpha.pop(i)
    empty_alpha.append(shiftedLet)

print(empty_alpha)
    

for letter in simple:
    if letter == " ":
        encoded += " "
    else:
        index = alpha.index(letter)
        encoded += empty_alpha[index]
'''
print(simple)
print(encoded)
print("")
print(alpha)
print(empty_alpha)
'''