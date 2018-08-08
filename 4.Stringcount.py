"""Write a program that asks the user for a string
and returns an estimate of how many words are in the string"""

string=input("Please enter the string to count the number of words in the string\n")
c=string.count(" ")
print(c+1)
