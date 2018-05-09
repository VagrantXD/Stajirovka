#!/bin/python3

#Find the total sum of angles in an n sided shape. N will be greater than 2.

def angle(n):
    return 180 * ( n - 2 )

if __name__ == "__main__" :
    print( angle( 4 ) )
