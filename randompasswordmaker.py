"""
Random Password Maker for python 3


"""

import random
import string

password = ""

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

allCase = [lowerCase,upperCase,digits,punctuation]


for a in range(2):
     password += allCase[0][random.randint(0,25)]
for a in range(2):
     password += allCase[1][random.randint(0,25)]
for a in range(2):
     password += allCase[2][random.randint(0,9)]
for a in range(2):
     password += allCase[3][random.randint(0,30)]
  
lastPassword = []   

for i in password:
     lastPassword.append(i)

random.shuffle(lastPassword)

password = ""

for i in lastPassword:
     password += i

print(password)