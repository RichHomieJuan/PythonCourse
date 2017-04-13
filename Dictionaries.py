#dictionaries are indexed by keys.

dictionary = {} #not very useful
tel = {"Mary": 4165, "John" : 4512, "Jerry" : 5555 }
print(tel)
tel ["jane"] = 5432  #inserts into the dictionary 
print(tel)
print(tel ["Jerry"]) #looks up the specified thing in dictionary
del tel["Jerry"]
print(tel)