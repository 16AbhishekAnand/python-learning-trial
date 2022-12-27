# comparison operator retun boolean.
# In logical operator "not" return opposite of given condition.
# Type casting is bascially used to convert one data type into another.EX:-
# a="364"
# b=float(a)
# c=int(a)
# print(b+1)
# print(c+1)
# In input function allows the user to take data as string.

# a=input("enter num1:")
# b=input("enter num2:")
# c=int(a) to specify specific data type we took extra variable.
# d=int(b)
# print("sum of c&d is ",c+d)
# print(type(c))

# concatinating two string:-
# a="harry"
# b=" good morning, "
# c= a + b
# (print(c)
 #we can acess the letter from the string  but can not change the letter in the string.(with the help of index.)

 # string slicing [excludes last letter inlcudes intial letter]
# a="harry"
# print(a[1:4]) #1st position gets includes where last gets excludes.
# print(a[:5]) is same as [0:5]
# print(a[1:]) is same as [1:5] (5=length of string)

# negative indices assign the string index  from the last and it starts with(-1). [4:0]=[-1:-5]

# a="thisisharry."
# print(a[0::2])#(skipping the string vlaue.)

story='''A grouping of four countries india, US, Australia and japan , there are also  a while alphabet geopolticlal
 soup that you can wade through BIMSTEC. If you are living in h=the capital very poor days.
  you probably know the ins and out of air quality.'''

# String functions
# print(len(story))
# print(story.endswith("quality."))
# print(story.count("o"))
# print(story.find("of"))
# print(story.replace("grouping","combining"))

# list of escape sequence character.
#  \n= newline \t=tab \'=singlequote \\=backslash,

var="Hi i am abhishek.\tGood to see you."
print(var)






