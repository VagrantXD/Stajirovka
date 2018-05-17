#!/bin/python3

#Your task is to implement a function that takes one or more dictionaries and combines them in one result dictionary.
#
#The keys in the given dictionaries can overlap. In that case you should combine all source values in an array. Duplicate values should be preserved.
#
#Here is an example:
#
#source1 = {"A": 1, "B": 2}
#source2 = {"A": 3}
#
#result = merge(source1, source2);
#// result should have this content: {"A": [1, 3]}, "B": [2]}
#You can assume that only valid dictionaries are passed to your function. The number of given dictionaries might be large. So take care about performance.

def merge(*dicts):
    a = {}
    for i in dicts :
        for j in i :
            if j in a :
                a[ j ].append( i[ j ] )
            else :
                a[ j ] = [ i[ j ] ]
    return a

if __name__ == "__main__" :
    print( merge( {"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5} ) )
