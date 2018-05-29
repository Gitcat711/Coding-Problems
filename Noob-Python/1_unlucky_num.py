# In range of numner from (1,20) - both inclusive.
# For 4 & 13, print "x in unlucky"
# For even numbers, print "x in even"
# For odd numbers, print "x is ood"




for num in range(1,21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

print("#"*20)
print("-"*20)
print("#"*20)

for num in range(1,21):
    if num == 4 or num ==  13:
        verdict = "unlucky"
    elif num % 2 == 0:
        verdict = "even"
    else:
        verdict = "odd"

    print(f"{num} is {verdict}")


