myPi = 4.0
a = 3.0

user = input("I will estimate pi. How many terms should I use?")

while a < 10 : 
    myPi = myPi - (4/a) + (4/(a+2))
    a += 4 
    print(myPi)

