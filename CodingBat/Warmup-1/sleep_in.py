# The Parameter weekday is True if it is weekday, and the
# parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation.
#Return True if we sleep in.

def sleep_in(weekday, vacation):
    """ Most naive solution with Or condition"""
    return not weekday or vacation

sleep_in(False, False) # True
sleep_in(True, False) # False
sleep_in(False, True) # True

#Alternative longer code
"""
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
"""
