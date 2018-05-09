#!/bin/python


#A Madhav array a has the following property.
#
#a[0] = a[1] + a[2] = a[3] + a[4] + a[5] = a[6] + a[7] + a[8] + a[9] = ...
#
#Write a function/method named isMadhavArray/IsMadhavArray/is_madhav_array() that returns true if its array argument is a Madhav array, otherwise it returns false.
#
#Edge cases: An array of length 0 or 1 should not be considered a Madhav array as there is nothing to compare.

def is_madhav_array( arr ) :
    current = 1
    step = 2

    while current + step <= len( arr ) :
        if sum( arr[ current : current + step ] ) != arr[ 0 ] :
            return False
        current += step
        step += 1
    if ( len( arr ) != current ) or ( len( arr ) < 3 ) :
        return False
    return True

if __name__ == "__main__" :
    print( is_madhav_array( [ 2, 1, 1, 4, -1, -1 ] ) )

