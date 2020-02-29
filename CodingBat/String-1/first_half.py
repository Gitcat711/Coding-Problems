#!/usr/bin/env python3

# Given a string aof even length, return the first half. So the
# Sting "WooHoo" yeilds "Woo"

# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(strn):
    return strn[:len(strn)//2]

print(first_half('WooHoo'))
