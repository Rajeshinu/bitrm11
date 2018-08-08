"""Write a program to print the multiplication tables from 2 to 10,
from 2 * 1=2 to 2 * 12 = 24 etc."""

a=0
b=0
c=0

for a in range(2,11):
    print("-----Table of ",a,"---------")
    for b in range(1,13):
          print(a,"*",b,"=",a*b)
