#!/bin/python3

#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.
#
#Examples
#to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
#
#to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"


def to_camel_case(text):
    a = text.replace( '-', '_' ).split( '_' )
    for i in range( 1, len( a ) ) : a[ i ] = a[ i ].capitalize() 
    return ''.join( a )


if __name__ == "__main__" :
    print( to_camel_case( "the_stealth-warrior" ) )
