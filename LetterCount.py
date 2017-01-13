#!/usr/bin/env python3

# Write a function, `letter_count(str)` that takes a string and
# returns a hash mapping each letter to its frequency. Do not include
# spaces.
#
# Difficulty: 1/5

def letterCount(str):

    numAlphas = {}

    for char in str:
        if char.isalpha():
            if numAlphas.get( char ) == None:
                numAlphas[ char ] = 1
            else:
                numAlphas[ char ] = numAlphas.get( char ) + 1

    return( numAlphas )
  

print( letterCount("cat") )
print( letterCount("moon") )
print( letterCount("cats are fun") )
