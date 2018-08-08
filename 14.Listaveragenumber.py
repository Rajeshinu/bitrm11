"""Write a program that: 1) reads numbers from the user until a blank line is entered.
2) Your program should display the average of all of the values entered by the user.
3) Then the program should display all of the below average values,
4) followed by all of the average values (if any),
5) followed by all of the above average values."""

list1=[]
print("Please enter few integer number and enter blank to exit: ")
while True:
    a=input("Please enter next number: ")
    if a!="":
     list1.append(int(a))
    else:
      break

#list1.pop() # pop will remove the last enterd number 0 inside the while loop
print("Entered numbers are:",end="")
print(list1)

list1.sort()
x=max(list1)
avg=x/2
print("Average of the list is: ",avg)
if avg in list1:
    print("The average number is present in the list: ",int(avg))

print("The below  average numbers are: ")
for i in list1:
    if i<avg:
        print(i,",",end="")

print("\nAbove  average numbers are: \n")
for i in list1:
    if i>avg:
        print(i,",",end="")

print("\n****THANK YOU*****")
