#Gven two int values, return their sum.
# Unless the two values are the same,
# then return double their sum.

# Short
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)

    return a + b

# What Codingbat suggest

def sum_double_1(a, b):
    #Store the sum in a local variable.
    add = a + b

    # Double if both a & b are same.
    if a == b:
        add *= add

    return add

sum_double(1, 2) # ---> 3
sum_double_1(2, 2) # ----> 8
