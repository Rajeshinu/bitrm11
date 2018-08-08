"""Write a program to print if a number is a prime number, prime number is which is divisible by one and itself"""

num=int(input("Please enter the number to check the number is prime or not."))

if num > 1:
   # check for factors
   for i in range(2,num):
       print(i)
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"*",num//i,"=",num)
           break
   else:
       print(num,"is a prime number")

# if input number is less than 1 or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
