"""Print a list of the values of the given dictionary: d={3:'c', 1: 'a', 5:'e', 4:'d', 2:'b'} in a sorted format"""

d={3:'c', 1: 'a', 5:'e', 4:'d', 2:'b'}
print("Dictionary items are: ",d)
list1=d.keys()
print(list1)
list2=list(list1)
list2.sort()

print("sorted list is ",list2)


print("Dictionary Keys and values in sorted are: ",end="")
for i in list2:
    print(i,":",d[i],end=",")
