"""Write a program that:1) reads integers from the user and 2) stores them in a list.
3) Your program should continue reading values until the user enters 0.
4) Then it should display all of the values entered by the user (except for the 0)
 in the same line 5) display all of the values entered by the user in order from
 smallest to largest in the same line 6) display all of the values entered by the
 user in order from largest to smallest in the same line."""

ul=[]
a=int(input("Please enter few integer number and press 0 to exit: "))
if a!=0:
    ul.append(a)
    while a!=0:
     a=int(input("Please enter next number: "))
     ul.append(a)

ul.pop() # pop will remove the last enterd number 0 inside list from the while loop
print("Entered numbers are:",end="")
print(ul)

ul.sort()
x=ul
print("Sorted list from smallest to largest is: ",x)

ul.reverse()
y=ul
print("List from largest to smallest is ",y)
