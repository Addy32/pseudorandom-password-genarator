import random
from cryptography.fernet import Fernet
import time
key = 0
try:
    f = open("key.txt", "r")
    print("key file found")
    key = 1
except FileNotFoundError:
    print("File not accessible")
    q = input("generate key Y/n: ")
    if q == "y" or q == "Y":
        key = Fernet.generate_key()
        with open('key.txt', 'wb') as filekey:
            filekey.write(key)
        key = 1
    else:
        print("WARNING you passwords will not be secure without a key")
        key = 0

name = input("enter seed string: ")

value = 0
chars = "aAbBcCdDEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#$%^&*()_-=+[]{}\|;:,<.>/?"
length = 0
final = ""
charslen = -1


for i in name:
    value = value + ord(i) - 64

if key == 1:
    keyfile = open('key.txt', 'r')
    for i in keyfile.read():
        value = value + ord(i) - 64


for i in chars:
    charslen = charslen + 1

for i in chars:
    length = length + 1
    value = value + 1
    random.seed(value)
    final = final + chars[random.randint(0,charslen)]
    if length >= 15:
        break

print (final)
