#Given a string, return a string where a
# first and last chars #has been exchnaged

def front_back(strn):
    if len(strn) <= 1:
        return strn

    return strn[len(strn) - 1] + strn[1:len(strn) - 1] + str[0]

        
