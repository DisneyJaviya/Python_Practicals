#e. Write a Python script to concatenate following dictionaries to create a new one.
#20CS019 Disney Javiya
dic1={1:10, 2:20}                #Create first dictionary
dic2={3:30, 4:40}                #Create second dictionary
dic3={5:50, 6:60}                #Create third dictionary
dic4 = {}                        #Create empty dictionary
for d in (dic1,dic2,dic3):       #Concatenation of the three dictionary
    dic4.update(d)
print(dic4)                      #Prints the concatenated dictionary