#!/usr/bin/env python3

# Write a method, `ordered_vowel_words(str)` that takes a string of
# lowercase words and returns a string with just the words containing
# all their vowels (excluding "y") in alphabetical order. Vowels may
# be repeated (`"afoot"` is an ordered vowel word).
#
# You will probably want a helper method, `ordered_vowel_word?(word)`
# which returns true/false if a word's vowels are ordered.
#
# Difficulty: 2/5

def get_vowels( word ):

    vowels = [ "a", "e", "i", "o", "u" ]
    vowelsInWord = ""

    for char in word:
        if vowels.count( char ) != 0:
            vowelsInWord += char

    return vowelsInWord
      

def check_vowel_order( word ):

    length = len( word )

    for indexOuter in range( length - 1 ):
        for indexInner in range( length - indexOuter - 1 ):
            indexToTestAgainst = indexInner + indexOuter + 1
            if ord( word[ indexOuter ] ) > ord( word[ indexToTestAgainst ] ):
                return False

    return True
  
def ordered_vowel_word( array ):

    vowels = [ "a", "e", "i", "o", "u" ]
    orderWordsString = ""

    for word in array:
        strOfVowelsInWord = get_vowels( word )
        isOrdered = check_vowel_order( strOfVowelsInWord )

        if isOrdered:
            if orderWordsString == "":
                orderWordsString += word
            else:
                orderWordsString += " " + word

    return orderWordsString
  

def ordered_vowel_words( string ):

    splitString = []
    orderedVowelWords = []

    splitString = string.split( " " )

    return ordered_vowel_word( splitString )

print( ordered_vowel_words("amends" ) )
if ordered_vowel_words("complicated" ) == "": print( "No in order vowels words" )
print( ordered_vowel_words("afoot" ) )
print( ordered_vowel_words("ham" ) )
print( ordered_vowel_words("crypt" ) )
print( ordered_vowel_words("o" ) )
print( ordered_vowel_words("tamely" ) )

phrase = "this is a test of the vowel ordering system"
result = "this is a test of the system"
print( ordered_vowel_words(phrase) )
