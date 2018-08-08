"""Write a program that reads a positive integer, n, from the user
and then displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using
the formula:sum = (n)(n + 1)/2"""

n=int(input(print("Please enter the N number to calculate the sum till the Nth number")))
sum=n*(n+1)/2
print("The sum of all of the integers from 1 to",n,"is :",sum)
