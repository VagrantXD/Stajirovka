#!/bin/python3

def OddOrEven( arr ) :
    return "even" if sum( arr ) % 2 == 0 else "odd"

print( OddOrEven( [ 5, 7, 88 ] ) );
