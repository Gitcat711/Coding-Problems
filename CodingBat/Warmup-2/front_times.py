#Given a string and a non-negative int n,
#we'll say that the front of the string is the first 3 chars,
#or whatever is there if the string is less than length 3.
#Return n copies of the front;

def front_times(istr, n):
    return istr[:3]*n

def front_times_1(istr, n):
    front_len = 3
    if front_len > len(istr):
        front_len = len(istr)
    front = str[:front_len]

    result = ""
    for i in range(n):
        result += front
    return result        
