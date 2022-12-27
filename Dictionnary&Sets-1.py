#Dictionary is the collection of key values pair which stores same or differnt values of data type. 
from traceback import print_tb


myDictionary={
    "key":"values",
    "num":"100",
    "name":["abhishek","Rahul","Shubham"], #after every key and value "coma"is must.
    "nestDict":{'play':'game'}
}
# print(myDictionary["key"])
# print(myDictionary["name"])
# print(myDictionary["nestDict"] ["play"])

#Methods of Dictionary[key,value and items]
# print(tuple(myDictionary.keys())) #type casting 
# print(list(myDictionary.values())) can be converted from one to another form.
# print(myDictionary.items()) Gives the output in tuple with key and value.

updateDict={
    "G":"Shiva",
    "O":"Ganesh",
    "D":["shiv","Ganesh","Sai"],
    "num":"200" # since the key is same it changes the value form dictionary.
}
myDictionary.update(updateDict) #updates the dictionary
print(myDictionary)
print(myDictionary.get("G2")) get fuction gives none if element is not present in the dictionary.
print(myDictionary(["G2"]))