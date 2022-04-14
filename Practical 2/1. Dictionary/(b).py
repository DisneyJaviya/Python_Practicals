#b. Write a Python script to merge two Python dictionaries.
#20CS019 Disney Javiya
dict1 = {1:20,2:30,3:40,4:50}                                  #Create first dictionary
dict2 = {'Red':'Cherry','Orange':'Mango','Green':'Grapes'}     #Create second dictionary
dict1.update(dict2)                                            #Merges the two dictionary
print(dict1)                                                   #Prints the merged dictionary