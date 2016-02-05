"""
calculatepi.py
Author: Hagin Onyango
Credit: Teacher

""" 
math 
n = int(input("I will estimate pi. How many terms should I use? "))
decimals = int(input("How many decimal places should I use in the result? "))
a = 4.0*sum([((-1.0)**k)/(2*(k) + 1) for k in range(0,n)])
print("The approximate value of pi is {0}".format(round(a, decimals)))
