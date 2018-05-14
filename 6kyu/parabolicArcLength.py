#!/bin/python3

#We want to approximate the length of a curve representing a function y = f(x) with a<= x <= b. First, we split the interval [a, b] into n sub-intervals with widths h1, h2, ... , hn by defining points x1, x2 , ... , xn-1 between a and b. This defines points P0, P1, P2, ... , Pn on the curve whose x-coordinates are a, x1, x2 , ... , xn-1, b and y-coordinates f(a), f(x1), ..., f(xn-1), f(b) . By connecting these points, we obtain a polygonal path approximating the curve.
#
#Our task is to approximate the length of a parabolic arc representing the curve y = x * x with x in the interval [0, 1]. We will take a common step h between the points xi: h1, h2, ... , hn = h = 1/n and we will consider the points P0, P1, P2, ... , Pn on the curve. The coordinates of each Pi are (xi, yi = xi * xi).
#
#The function len_curve (or similar in other languages) takes n as parameter (number of sub-intervals) and returns the length of the curve truncated to 9 decimal places.


from math import sqrt

def len_curve(n):
    length = 0
    step = 1
    x0, x1 = 0, 1 / n
    while x1 <= 1 :
        length += sqrt( (x1 - x0)**2 + ( x1*x1 - x0*x0 )**2 )  
        x0 = step * ( 1 / n )                  # Тут считал заново, так как на каком-то знаке после запятой все
        x1 = step * ( 1 / n ) + (  1 / n )     # сбивалось, и число становилось неправельным
        step += 1
        
    return round( length, 9 )

if __name__ == "__main__" :
    print( len_curve( 10 ) )
