"""Ask the user to enter a number. Then print the square of that number.
If the user enters a negative number, you should print a message and trap the exception."""


while True:
    try:
        n=int(input("Please enter a number to find the square of it or 0 to exit: "))
        if n==0:
            print("Thankyou")
            break
        elif n<0:
            raise ValueError("please share postive number")
        else:
            print("The square of the number is",n*n)

    except ValueError as er:
        print("Negative number entered : ",er)







