#!/bin/python3

#A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
#Within that sequence, he chooses two numbers, a and b.
#He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
#Given a number n, could you tell me the numbers he excluded from the sequence?
#The function takes the parameter: n (don't worry, n is always strictly greater than 0 and relatively small) and returns an array or a string (depending on the language) of the form:
#
#[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
#with all (a, b) which are the possible removed numbers in the sequence 1 to n.
#
#[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".
#
#It happens that there are several possible (a, b). The function returns an empty array if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).
#
#(See examples of returns for each language in "RUN SAMPLE TESTS")
#
#Examples:
#removNb(26) should return [(15, 21), (21, 15)]
#or
#
#removNb(26) should return { {15, 21}, {21, 15} }
#or
#
#removeNb(26) should return [[15, 21], [21, 15]]
#or
#
#removNb(26) should return [ {15, 21}, {21, 15} ]
#or
#
#removNb(26) should return "15 21, 21 15"
#or
#
#in C:
#removNb(26) should return  **an array of pairs {{15, 21}{21, 15}}**
#tested by way of strings.


def removNb(n):
    total = sum( range( 1, n + 1 ) )
    ans = []
    print( total )
    for a in range( total // n, n + 1) :
         if ( total - a ) % ( a + 1 ) == 0 :
            ans.append( ( a, ( total - a ) // ( a + 1 ) ) )
            
    return ans

if __name__ == "__main__" :
    print( removNb( 26 ) )
