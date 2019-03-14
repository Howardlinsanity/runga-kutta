'''
Please read the README.md for guide and limitations of this program.
Author: Howard Lin and Danny Lu
'''
from scipy import misc 
from math import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import time

'''
Here is the implmentation of the 2nd Order Runga Kutta method of 1 step
    @parameters:
    f: Python function 
    t: int, initial t
    x: int, initial x given initial t, e.g. x(t)
    h: int, stepsize
    Returns x(t+h)
'''
def second_order_rk_loop(f,t,x,h,n):
    ta = t    
    h = h/n
    for j in range(1, n+1):
        k1 = h * f(t,x)
        k2 = h * f(t + h, x + k1)
        x = x + (1/2) * (k1 + k2)
        t = ta + j*h

    return x

'''
Here is the implmentation of the 2nd Order Runga Kutta method
    @parameters:
    f: Python function 
    t: int, initial t
    x: int, initial x given initial t, e.g. x(t)
    h: int, stepsize
    Returns x(t+h)
'''
def second_order_rk(f,t,x,h):
    k1 = h * f(t,x)
    k2 = h * f(t + h, x + k1)

    return x + ((k1 + k2)/2)

'''
Here is the implmentation of the 4th Order Runga Kutta method of 1 step
    @parameters:
    f: Python function 
    t: int, initial t
    x: int, initial x given initial t, e.g. x(t)
    h: int, stepsize
    Returns x(t+h)
'''
def fourth_order_rk(f,t,x,h):
    k1 = h * f(t,x)
    k2 = h * f(t + (h/2), x + (k1/2))
    k3 = h * f(t + (h/2), x + (k2/2))
    k4 = h * f(t + h, x + k3)

    return x + ((k1 + 2*k2 + 2*k3 + k4)/6)

'''
Here is the implmentation of the 4th Order Runga Kutta method of n steps
    @parameters:
    f: Python function 
    t: int, initial t
    x: int, initial x given initial t, e.g. x(t)
    h: int, stepsize
    n: int, number of iteration
    Returns x(t+h)
'''
def fourth_order_rk_loop(f,t,x,h,n):
    ta = t
    h = h/n 
    for j in range(1,n+1):
        k1 = h * f(t,x)
        k2 = h * f(t + (h/2), x + (k1/2))
        k3 = h * f(t + (h/2), x + (k2/2))
        k4 = h * f(t + h, x + k3)
        x = x + ((k1 + 2*k2 + 2*k3 + k4)/6)
        t = ta + (j * h)

    return x

'''
This is the f(t,x) function
'''
def f(t,x):
    return 2 + (x - t - 1)*(x - t -1)

'''
    This is the main function
'''
if __name__ == "__main__":
    print("Hello there! This is the main file")
    result = fourth_order_rk(f,1,2,0.5625)
    # we are gonna approximate x(1.5624) with initial value x(1) = 2
    print(result)
