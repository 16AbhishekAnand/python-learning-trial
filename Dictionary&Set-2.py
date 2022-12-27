# #set is group of non repeatative element and element cannot be changed.
# a={1,4,5,6,8}
# print(a)
# print(type(a))

# #method to create empty set.
s1=set()
# print(type(s1)) #here if we write "s1={}" then it consider it as dictionary.
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add((3,45,65,6)) # tuple can be added.
s1.add(4) # Here item is being repeated so set it not considering repeating element.
s1.remove(4)
print(s1)
  
#we can not merge "list & dictionary" with set because list and dictionary can be changed whereas "set" cannot.


 