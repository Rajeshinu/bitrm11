"""Write a program that generates a random number, x, between 1 and 50,
a random number y between 2 and 5, and computes x y. """

from random import randint
x=randint(1,50)
y=randint(2,5)

print("Random number X between 1 to 50 is : ",x)
print("Random number Y between 2 to 5 is : ",y)

print("Sum of x and y is: ",x+y)
print("sub of x and y is: ",x-y)
print("Multiple of x and y is: ",x*y)
print("Division of x and y is: ",x/y)
str=("THANK YOU")
print(str.center(50,"*"))
