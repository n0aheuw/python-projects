from __future__ import print_function
import math, sys
from decimal import *

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

# Store previously computed factorials
factorials = {0: 1, 1: 1}

def factorial(n):
    if n in factorials:
        return factorials[n]
    result = n * factorial(n-1)
    factorials[n] = result
    return result

def get_iteration(k):
    k = k + 1
    getcontext().prec = k
    sum = 0
    for k in range(k):
        first = factorial(6*k) * (13591409 + 545140134*k)
        down = factorial(3*k) * (factorial(k))**3 * (640320**(3*k))
        sum += first/down 
    return Decimal(sum) 

def get_value__pi(k):
    iteration = get_iteration(k)
    up = 426880*math.sqrt(10005)
    pi = Decimal(up) / iteration 
    return pi

def shell():
    print ("Welcome to Pi Calculator. In the shell below, enter the number of digits up to which the value of Pi should be calculated or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print ("You did not enter a number. Try again")
        else:
            print (get_value__pi(int(entry)))

if __name__=='__main__':
    shell()
