#!/usr/bin/env python3

# Write a function word_unscrambler that takes two inputs: a scrambled
# word and a dictionary of real words.  Your program must then output
# all words that our scrambled word can unscramble to.
#
# Hint: To see if a string `s1` is an anagram of `s2`, split both
# strings into arrays of letters. Sort the two arrays. If they are
# equal, then they are anagrams.
#
# Difficulty: 3/5


#
# Postcondition: returned is word sorted and converted to an array
def convertWordToArray( word ):

    wordAsArray = []

    for char in word:
        wordAsArray.append( char )

    return sorted( wordAsArray )


# Precondition: word is a string, dictionary is a list of strings
# Postcondition: a list of entries in dictionary that are anagrams of word
def wordUnscrambler(word, dictionary):

    matches = []

    wordAsArray = convertWordToArray( word )

    for word in dictionary:
        if wordAsArray == convertWordToArray( word ):
            matches.append( word )

    return matches

print( wordUnscrambler( "cat", [ "tac" ] ) )
print( wordUnscrambler( "cat", [ "tom" ] ) )
print( wordUnscrambler( "cat", [ "tic", "toc", "tac", "toe" ] ) )
print( wordUnscrambler( "cat", [ "scatter", "tac", "ca" ] ) )
print( wordUnscrambler( "turn", [ "numb", "turn", "runt", "nurt" ] ) )
