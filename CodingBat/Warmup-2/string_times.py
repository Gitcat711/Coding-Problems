# Given a String and non-negative int n , return a larger string that
#is n copies of the original string.

#string_times("Hi", 2) ==> HiHi
#string_times("Hoy", 2) ==> Hoy
#string_times("His", 2) ==> His

def string_times(istr, n):
    return istr*n

def string_times1(istr, n):
    result = ""
    for i in range(n):
        result += result
    return result
