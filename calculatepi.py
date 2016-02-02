myPi = 4.0
a = 3.0

while a < 88000 : 
    myPi = myPi - (4/a) + (4/(a+2))
    a += 4 
    print(myPi)

