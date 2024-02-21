#Random Password Generator using Python

#import necessary modules
import string
import secrets

#input the length of the password
n=int(input("Enter length of password that you needed: "))

symbols = ['*', '%', '£'] # Can add more

password = ""
for _ in range(n):
    password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(symbols)
print(password)
