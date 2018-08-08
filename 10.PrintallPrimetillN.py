"""Write a program to print all prime numbers upto a given number """

n=int(input(print("Please enter the N number to print the prime number till Nth number: \n")))
print("Prime numbers till ",n," are :")
for a in range(2,n):
    for i in range(2,a):
        if a % i == 0:
            break
    else:
        print(a)
