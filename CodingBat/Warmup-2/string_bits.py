# Given a string, return a new string made of every other char starting with
# the first, so "Hello" yields "Hlo".

def string_bits(istr):
    return istr[::2]

def string_bits_1(istr):
    result = ""
    for i in range(len(istr)):
        if i % 2 == 0:
            result += istr[i]
    return result

string_bits("Andromeda")
string_bits_1("Stellar")

                
