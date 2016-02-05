import math 
n = int(input("I will estimate e. How many terms should I use? "))
decimals = int(input("How many decimal places should I use in the result? "))
a = 1.0/sum([((-1.0)**k)/math.factorial(k) for k in range(0,n)])
print("The approximate value of e is {0}".format(round(e, decimals)))
print("(The true value of e is {0})".format(round(math.e, decimals)))
