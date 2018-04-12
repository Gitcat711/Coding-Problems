#We have two monkeys, a and b, and the parameters a_smile
# and b_smile indicate if each is smiling. We are in trouble
# if they both are smiling or if neither of them is smiling,
# Return True of we are in trouble.

#Solution 1.(Shortest)
def monkey_trouble_1(a_smile, b_smile):
    """Checking with == """
    return (a_smile == b_smile)

#Solution 2.(Short)
def monkey_trouble_2(a_smile, b_smile):
    """ Checking with 'and' 'or' statements """
    return ((a_smile and b_smile) or (not a_smile and not b_smile))

#Solution 3.(Acceptable)
def monkey_trouble_3(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False

monkey_trouble_1(True, False) #-->True
monkey_trouble_2(False, False) #--> True
monkey_trouble_3(True, False) #--> False
                
