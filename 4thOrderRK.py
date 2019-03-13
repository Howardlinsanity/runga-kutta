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
def second_order_rk(f,t,x,h):

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


'''
    This is the main function
'''
if __name__ == "__main__":
    f = function_parser()
