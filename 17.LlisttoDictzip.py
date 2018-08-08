"""Write a program that will create a dictionary from the 2 lists [ 'a', 'b', 'c', 'd'] and [1,2,3,4]"""

list1=['a','b','c','d']
list2=[1,2,3,4]
dict1=dict(zip((list1),(list2)))
print("Dictionary items are :",dict1)
