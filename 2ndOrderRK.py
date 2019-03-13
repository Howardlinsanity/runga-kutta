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
    Will ask user for a function and then return said function as well as string representation
'''
def function_parser():
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e','exp','fabs', 'floor', 'fmod','frexp','hypot','ldexp', 'log', 'log10','modf', 'pi','pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan','tanh']
    safe_dict = dict([(k,locals().get(k,None)) for k in safe_list]) 
    expr = input("Input function please: ")
    def f(x,t):
        safe_dict['x'] = x
        safe_dict['t'] = t
        return eval(expr, {"__builtins__":None},safe_dict)
    return f

'''
    Here is the implmentation of the 2nd Order Runga Kutta method
    @parameters:
    f: Python function 
    t: int, initial t
    x: int, initial x given initial t, e.g. x(t)
    h: int, stepsize
    Returns x(t+h)
'''

def second_order_rk_loop(f,t,x,h,n):

    # x(t + h) = x(t) + (1/2)(k1 + k2)
    # k1 = h*f(t,x)
    # k2 = h*f(t + h, x + k1)

    ta = t    
    h = h/n
    for j in range(1, n+1):
        k1 = h*f(t,x)
        #print("K1:",k1)
        k2 = h*f(t + h, x + k1)
        #print("K2:", k2)
        x = x + (1/2)*(k1 + k2)
        t = ta + j*h
        print("Current step output: j = %s, t = %s, x = %s" % (j, t, x))

    return x

def second_order_rk(f,t,x,h):

    # x(t + h) = x(t) + (1/2)(k1 + k2)
    # k1 = h*f(t,x)
    # k2 = h*f(t + h, x + k1)

    k1 = h*f(t,x)
    print("K1:",k1)
    k2 = h*f(t + h, x + k1)
    print("K2:", k2)

    return x + (1/2)*(k1 + k2)

'''
    Here is the implmentation of the 4th Order Runga Kutta method
    @parameters:
    f: Python function 
    t: int, initial t
    x: int, initial x given initial t, e.g. x(t)
    h: int, stepsize
    Returns x(t+h)
'''

def fourth_order_rk(f,t,x,h):

    return 0
'''
    This is the main function
'''

def f(t,x):
        return float(-t*(x**2))

if __name__ == "__main__":
    x = 2
    h = -.2
    t = 0

    #print(second_order_rk(f, t, x, h))
    print(second_order_rk_loop(f, t, x, h, 10))