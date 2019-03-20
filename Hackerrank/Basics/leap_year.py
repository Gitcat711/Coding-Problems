#!/usr/bin/python3

# Task
# You are given the year, and you have to write a function to check if the year is leap or not. 
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
#     The year can be evenly divided by 4, is a leap year, unless:
#     The year can be evenly divided by 100, it is NOT a leap year, unless:
#     The year is also evenly divisible by 400. Then it is a leap year.

def leap(year):
    return year % 4 == 0  and (year % 100 == 0 or year % 400 == 0)
    
print(leap(1990))
