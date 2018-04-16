# Given a non-empty string like "Code" return
# a string like "CCoCodCode"


def string_splosion(istr):
    result = ""
    # On each iteration, add the substring of the chars 0..i
    for i in range(len(istr)):
        result = result + istr[:i+1]
    return result

string_splosion("Kiron")

def string_splosion(istr):
    c = []
    for i in range(1, len(istr) + 1):
        c.append(istr[:1])
    return "".join(c)
