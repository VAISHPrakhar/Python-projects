import random   
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#ENCRYPT
Text = input("Enter a message to encrypt: ")
cipher_text = " "

for letter in Text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"Original message: {Text}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
Text = " "

for letter in cipher_text:
    index = key.index(letter)
    Text += chars[index]
    
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {Text}")



