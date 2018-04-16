# Given 2 Strings, a and b, return the number
# of the positions where they contain the same
# length 2 2 substring. SO "xxcaazz" and "xxbaaz" yeilds 3,
# since the "xx", "aa" & "az" substings appear in the same place in both stings.

def strings_match(a, b):
    count = 0
    for i in range(min(len(a), len(b) - 1)):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count        

print(strings_match("abbracdabra", "abbbracadabbra"))
