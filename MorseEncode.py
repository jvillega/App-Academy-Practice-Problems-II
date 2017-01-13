#!/usr/bin/env python3

# Build a function, `morse_encode(str)` that takes in a string (no
# numbers or punctuation) and outputs the morse code for it. See
# http://en.wikipedia.org/wiki/Morse_code. Put two spaces between
# words and one space between letters.
#
# You'll have to type in morse code: I'd use a hash to map letters to
# codes. Don't worry about numbers.
#
# I wrote a helper method `morse_encode_word(word)` that handled a
# single word.
#
# Difficulty: 2/5


#
#
def getMorseCode():
    morseCode = {'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..' }

    return morseCode

#
#
def convertWordToMorse( word ):

    morseCode = getMorseCode()
    wordInMorse = ""

    for char in word:
        wordInMorse += morseCode[ char ] + " "

    return wordInMorse + " "
  

#
#
def morseEncode( string ):

    completeStringInMorse = ""
    splitString = string.split( " " )

    for index in splitString:
        completeStringInMorse += convertWordToMorse( index.lower() )

    return completeStringInMorse

print( morseEncode( "q" ) )
print( morseEncode( "Hello fda World" ) )
print( morseEncode("cat") )
print( morseEncode("cat in hat") )
