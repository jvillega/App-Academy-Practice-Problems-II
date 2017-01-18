#!/usr/bin/env python3

# Write a function `bubble_sort(arr)` which will sort an array of
# integers using the "bubble sort"
# methodology. (http://en.wikipedia.org/wiki/Bubble_sort)
#
# Difficulty: 3/5


# Precondition:
# Postcondition:
def bubbleSort(arr):

    length = len( arr )
    cur = 0

    while cur != length:
        for index in range( length - 1 ):
            if arr[ index ] > arr[ index + 1 ]:
                temp = arr[ index ]
                arr[ index ] = arr[ index + 1 ]
                arr[ index + 1 ] = temp

        cur += 1

    return arr


# Calls to test bubbleSort
print( bubbleSort( [] ) )
print( bubbleSort( [ 1 ] ) )
print( bubbleSort( [ 5, 4, 3, 2, 1 ] ) )
print( bubbleSort( [ 5, 4, 3, 2, 1, 9, 10, 67, 68, 14, -1 ] ) )
