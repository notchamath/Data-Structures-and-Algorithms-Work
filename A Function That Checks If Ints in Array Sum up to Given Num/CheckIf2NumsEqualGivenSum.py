# This function checks an array of ints to see if two elements in the array could sum up to a given number
# The Time Complexity of this function is O(n)

def check_for_sum(array, sum):

    dict = {}

    for num in array:

        if sum - num in dict:
            return print(True)

        dict[num] = num

    return print(False)


check_for_sum([3, 4, 1, 2, 8], 6)
check_for_sum([2, 4, 1, 4, 8], 8)
