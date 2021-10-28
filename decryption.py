shifted = input("Paste the shifted alphabet: ")
encrypted = input("Paste the encrypted string: ")
alpha = "abcdefghijklmnopqrstuvwxyz"
decrypted = ""
for letter in encrypted:
    if letter == " ":
        decrypted += " "
    else:
        index = shifted.find(letter)
        decrypted += alpha[index]
print(decrypted)
