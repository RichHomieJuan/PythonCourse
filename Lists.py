lister = [1, 2, 4, "hello"] #Lists can have variables and Strings
#Lists also are made with [] square brackets

lister.append(2) #Adds a variable or string to the list.
print(lister)

print(lister.index(1)) #tells you index of a specific element, starts from 0.

print(lister.count(2))#tells you the number of (x) inside of your list

print(lister.remove(2)) #removes (x) from your current list.

print(lister)

lister.reverse()
print(lister)

lister2 = [3 ,7, 1 ,6 ,0  ] #listers can be treated as integers in terms of storing a list of strings and variables in any specific order.
print(lister2)

lister2.sort() #sorts a list of integers  into numeric order, does not support strings.
print(lister2)


testscores = [82, 83, 93, 11]
testscores[0]
sum = testscores[0] + testscores[1] + testscores[2] + testscores[3]
print(sum)
print(len(testscores))
print(sum / len(testscores))

import statistics

print(statistics.median(testscores))
