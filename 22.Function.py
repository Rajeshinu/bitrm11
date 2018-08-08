"""Write a function to find the the result of (a+b)**2 and
call it passing the values of a and b entered by the user"""

def result(a,b):   #Defining a function name as result and return the x value
    x=((a+b)**2)
    return(x)


a=int(input("Please enter the A value: "))
b=int(input("Please enter the B value: "))
print("The result of (a+b)**2 is: ",result(a,b))
