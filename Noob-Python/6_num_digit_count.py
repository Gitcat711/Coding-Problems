#! /usr/bin/env python3

text = input(str("Enter the String :"))
digits  = 0
characters = 0
for  i in text:
    if(i.isdigit()):
        digits += 1
    characters += 1

print("The number of digits is : ", digits)
print("The number of characters is : " , characters)

