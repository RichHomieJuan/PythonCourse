#Tuples cant be changed, Tuples are created using () Lists are created using []

tup = ("math", "football", 2005) #valid tuple
tuper = () #an empty tuple
tuper = (1,) #to write a single value tuple you need a comma

#like strings tuple indexes start at 0 and they can be sliced and cocantenated

print(tup[0])
print(tup[0:2])
#can't change value of tuples but you can add 2 tuples together.
tup1 = (10,5)
tup2 = ("me", "you")

tup3 = (tup1[0], tup2[0]) #this added the value of tup 1[0]=10 and tup2[0]= me
#giving us tup3 = (10, "me")
print(tup3)

tuper = ("grades", 100)
print(tuper)
del tuper
tuper = (1, 2, 3)
 #if a tuple is going to be put with a [] has to be separated by a comma not a + to cocantenate

#tuples have all the basic commands that strings have ex: in + *

lister = [1,5,3]
tuper= tuple(lister) #converts lists into tuples.
print(tuper)

#tuples cant be changed after created, they can be linked together. 


#----------------------------- EXTRA-------------------------------------------

tup = ("sam", 20)
x, y = tup
print(x)
print(y)
temp= x
x = y    #swaps out x and y.
y = temp

x,y = y,x #better method to swap values