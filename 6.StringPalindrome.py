"""Write a program that asks the user to enter a word and
determines whether the word is a palindrome or not.
A palindrome is a word that reads the same backwards as forwards"""

mystr=str(input(print("Please enter the word to determines "
                      "whether the word is a palindrome or not\n")))

rstr=mystr[::-1]

if mystr==rstr:
    print(mystr,"is a palindrome")
else:
    print(mystr,"is not a palindrome")
