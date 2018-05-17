#!/bin/python3

#In this Kata, you will be given a string with brackets and an index of an opening bracket and your task will be to return the index of the matching closing bracket. Both the input and returned index are 0-based except in Fortran where it is 1-based. An opening brace will always have a closing brace. Return -1 if there is no answer (Haskell return Nothing, Fortran: return 0)
#
#For example, in JS, Python, Ruby...
#
#solve("((1)23(45))(aB)", 0) = 10 -- the opening brace at index 0 matches the closing brace at index 10
#solve("((1)23(45))(aB)", 1) = 3 
#solve("((1)23(45))(aB)", 2) = -1 -- there is no opening bracket at index 2, so return -1
#solve("((1)23(45))(aB)", 6) = 9
#solve("((1)23(45))(aB)", 11) = 14
#solve("((>)|?(*'))(yZ)", 11) = 14
#In Haskell:
#
#solve("((1)23(45))(aB)", 0) = Just 10 -- the opening brace at index 0 matches the closing brace at index 10
#solve("((1)23(45))(aB)", 2) = Nothing -- there is no opening bracket at index 2, so return "Nothing" instead of -1
#In Fortran:
#
#solve("((1)23(45))(aB)", 1) ! => 11 (the opening brace at index 1 matches the closing brace at index 11)
#solve("((1)23(45))(aB)", 2) ! => 4
#solve("((1)23(45))(aB)", 3) ! => 0 (there is no opening bracket at index 3, so return 0)
##solve("((1)23(45))(aB)", 7) ! => 10
#solve("((1)23(45))(aB)", 12) ! => 15
#solve("((>)|?(*'))(yZ)", 12) ! => 15
#Input will consist of letters, numbers and special characters, but no spaces. The only brackets will be ( and ).
#
#More examples in the test cases.
#
#Good luck!


def solve(st, idx):
    if st[ idx ] != '(' : return -1
    state = 1
    for i in range( idx + 1, len( st ) ) :
        if st[ i ] == '(' : state += 1
        elif st[ i ] == ')' : state -= 1
        if not state : return i 

if __name__ == "__main__" :
    print( solve( "((1)23(45))(aB)", 0) )
