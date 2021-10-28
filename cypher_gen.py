import random
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha_str = "abcdefghijklmnopqrstuvwxyz"
alpha_change = []
user_in = input("Type in the string you would like to encrypt(special characters excluded): ")
change_str = ""
encrypted = ""

for i in range(26):
    shift = random.randint(0,len(alpha)-1)
    alpha_change.append(alpha[shift])
    removal = alpha[shift]
    alpha.remove(removal)
    
for let in alpha_change:
    change_str += let

for letter in user_in:
    if letter == " ":
        encrypted += " "
    else:
        index = alpha_str.find(letter)
        encrypted += alpha_change[index]

print()
print(change_str)
print(alpha_str)
print()
print(encrypted)
