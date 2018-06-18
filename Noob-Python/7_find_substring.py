#! /usr/bin/env python3

string = input(str("Please enter the string: "))
word = input(str("please enter the word: "))

if(string.find(word)==-1):
    print(f"There's no such word as '{word}' in this string")
else:
    print(f"The word '{word}' is present in the text")


