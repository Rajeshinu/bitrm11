"""Write a program to print the sum of all even numbers upto and including 100 """

sum=0
print("Even number from 2 to 100 is: ")
for i in range(2,101,2):
    sum=sum+i
    print(i,end=",")

print("\n")
print("Sum of even number is :",sum)
print("good")