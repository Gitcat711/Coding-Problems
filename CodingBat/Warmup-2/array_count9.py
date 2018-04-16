# GIven an aray of ints,
# Return number of 9's in the
# array.

def array_count9(num_arr):
    count = 0
    for num in num_arr:
        if num == 9:
            count += 1

    return count

print(array_count9([1,7,8, 9, 9, 90]))
