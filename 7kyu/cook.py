#!/bin/python3
#You've purchased a ready-meal from the supermarket.

#The packaging says that you should microwave it for 4 minutes and 20 seconds, based on a 600W microwave.

#Oh no, your microwave is 800W! How long should you cook this for?!

#Input
#You'll be given 4 arguments:

#1. needed power
#The power of the needed microwave.
#Example: "600W"

#2. minutes
#The number of minutes shown on the package.
#Example: 4

#3. seconds
#The number of seconds shown on the package.
#Example: 20

#4. power
#The power of your microwave.
#Example: "800W"

#Output
#The amount of time you should cook the meal for formatted as a string.
#Example: "3 minutes 15 seconds"

#Note: the result should be rounded up.

#59.2 sec  -->  60 sec  -->  return "1 minute 0 seconds"


import math

def cooking_time(needed_power, minutes, seconds, power):
    time = ( minutes * 60 + seconds ) * int( needed_power[ :-1 ] ) / int( power[ :-1 ] )
    return "{} minutes {} seconds".format( math.ceil( time ) // 60, math.ceil( time ) % 60 )

if __name__ == "__main__" :
    print( cooking_time( "600w", 4, 20, "800w" ) )
