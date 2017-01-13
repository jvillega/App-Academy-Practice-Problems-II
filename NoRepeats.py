#!/usr/bin/env python3

# Write a function, `no_repeats(year_start, year_end)`, which takes a
# range of years and outputs those years which do not have any
# repeated digits.
#
# You should probably write a helper function, `no_repeat?(year)` which
# returns true/false if a single year doesn't have a repeat.
#
# Difficulty: 1/5
def noRepeat( year ):

    numOfNums = {}
    yearAsString = str( year )
    yearAsStringLength = len( yearAsString )

    for index in range( yearAsStringLength ):
        num = int( yearAsString[ index ] )

        if numOfNums.get( num ) == None:
            numOfNums[ num ] = 1

        else:
            numOfNums[ num ] = numOfNums.get( num ) + 1

    for key in numOfNums:
        if numOfNums[ key ] > 1:
            return False

    return True

  
def noRepeats(year_start, year_end):

    listOfNoRepeatYears = []

    while year_start != year_end + 1:
        if noRepeat( year_start ) == True:
            listOfNoRepeatYears.append( year_start )

        year_start += 1

    return listOfNoRepeatYears

print( noRepeats( 1234, 1234 ) )  
print( noRepeats( 1134, 1134 ) )
print( noRepeats( 1980, 1987 ) )
print( noRepeats( 1230, 1240 ) )
