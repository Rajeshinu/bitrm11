"""Write a program that asks the user to enter a word and then
capitalizes every other letter of that word. So if the user enters "rhinoceros",
the program should print "rHiNoCeRoS"""

word=str(input("please enter the word\n"))
count=0
for char in word:
    if count==0:
     print(char.upper(),end="")
     count=1
    else:
        print(char.lower(),end="")
        count=0
