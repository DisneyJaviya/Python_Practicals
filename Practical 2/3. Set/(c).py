#c. Write a Python program to create an intersection, Union, difference of sets.
#20CS019 Disney Javiya
fruits = {'Mango','Banana','Apple','Carrot'}            #Create set 1 of fruits
vegetables = {'Cucumber','Tomato','Potato','Mango'}     #Create set 2 of vegetables
inter = fruits.intersection(vegetables)                 #Finds the item common between the two set
union = fruits.union(vegetables)                        #Combines the two given set 
dif1 = fruits.difference(vegetables)                    #Finds the item present in fruits set that are not present in vegetables set
dif2 = vegetables.difference(fruits)                    #Finds the item present in vegetables set that are not present in fruits set
print(inter)                                            #Prints the intersection
print(union)                                            #Prints the union of to set
print(dif1)                                             #Prints difference
print(dif2)                                             #Prints difference