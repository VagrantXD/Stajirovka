#!/bin/python3

#Given a list of integers, return the nth smallest integer in the list. Only distinct elements should be considered when calculating the answer. n will always be positive (n > 0)
#
#If the nth small integer doesn't exist, return -1 (C++) / None (Python) / nil (Ruby).
#
#Notes:
#
#"indexing" starts from 1
#huge lists (of 1 million elements) will be tested
#Examples
#[1, 3, 4, 5], 7        ==> None  # n is more than the size of the list
#[4, 3, 4, 5], 4        ==> None  # 4th smallest integer doesn't exist
#[45, -10, 4, 5, 4], 4  ==> 45    # 4th smallest integer is 45
#If you get a timeout, just try to resubmit your solution. However, if you always get a timeout, review your code.


def nth_smallest(arr, n):
    arr = sorted( list( set( arr ) ) )                  #Понял, что можно было сделать: sorted( set( arr ) )
    return arr[ n - 1 ] if n - 1 < len( arr ) else None #потому что sorted() принимает какую-нибудь  
                                                        # последовательность, а возрвщает список


if __name__ == "__main__" :
    print( nth_smallest( [ 8, 9, 7, 6, 4, 3, 2 ], 3 ) )

