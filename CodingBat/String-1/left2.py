# Given a String, a "a rotated left 2" verison where the first 2 chars
# are moved to the end. The string length will be at least 2.

def left2(strn):
    return strn[2:] + strn [:2]

