"""Write a program that asks the user to enter a word
and prints out whether that word contains any vowels"""

word=input("Please enter a word to check whether that word contains any vowels\n")
vowels = ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
print(type(word))
#if any(char in vowels for char in word):
for char in word:
    if char in vowels:
     print("vowels letter",char," is present in the word",)
     break
else:
 print("word dosn't contain any vowels")

