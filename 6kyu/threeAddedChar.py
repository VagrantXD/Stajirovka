#!/bin/python3

#Given two strings, the first being a random string and the second being the same as the first, but with three added characters somewhere in the string (three same characters),
#
#Write a function that returns the added character
#
#E.g
#string1 = "hello"
#string2 = "aaahello"
#
#// => 'a'
#The above is just an example; the characters could be anywhere in the string and string2 is actually shuffled.
#
#Another example
#string1 = "abcde"
#string2 = "2db2a2ec"
#
#// => '2'
#Note that the added character could also exist in the original string
#
#string1 = "aabbcc"
#string2 = "aacccbbcc"
#
#// => 'c'
#You can assume that string2 will aways be larger than string1, and there will always be three added characters in string2.
#
#Can you do it in O(m+n) or O(n) time and O(1) Space ?
#
#When you're done you'll be shown the average runtime your code took to finish all test cases; feel free to include it at the top of your solution ;)
#
#Collapse 'Test cases' or scroll down to the end of the test cases to see your code's Average runtime


# Average runtime: 595 ms

def added_char(s1, s2):  
    for i in s2 :
        if s2.count( i ) - s1.count( i ) == 3 :
            return i

if __name__ == "__main__" :
    print( added_char( "abcde", "2db2a2ec" ) )
