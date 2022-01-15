#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a Python script to check whether a given key already exists in a dictionary.
dict1 = {'First_name':'Disney',
         'Last_name':'Javiya',
         'Country':'India',
         'State':'Gujarat',
         'City':'Rajkot'
        }
#for checking key in a dictionary
print('First_name' in dict1)
print('job_title' in dict1)


# In[5]:


#Write a Python script to merge two Python dictionaries.
dict1 = {'First_name':'Disney',
         'Last_name':'Javiya',
         'Country':'India',
         'State':'Gujarat',
         'City':'Rajkot'
        }

dict2 = {'Job_title':'Student',
         'University':'Charusat',
         'Branch':'CSE',
         'Semester':'4th'
        }
#For merging two dictionaries.
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
dict3 = Merge(dict1,dict2)
print(dict3)


# In[6]:


#Write a Python program to sum all the items in a dictionary.
def returnSum(dict):
     
     sum = 0
     for i in dict.values():
           sum = sum + i
      
     return sum
 
# Driver Function
dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", returnSum(dict))


# In[7]:


# Write a Python script to add a key to a dictionary.
dict1 = {'First_name':'Disney',
         'Last_name':'Javiya',
         'Country':'India',
         'State':'Gujarat',
         'City':'Rajkot'
        }
#Adding element.
dict1['Job_title'] = 'Student'
print(dict1)


# In[9]:


#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}
dic4 = {**dic1,**dic2,**dic3}
print(dic4)


# In[10]:


#Write a Python program to create a tuple with different data types.
fruits = ('Lemon','Orange','Mango','Apple')
print(fruits)


# In[14]:


# Write a Python program to create a tuple with numbers and print one item.
numbers = ('193','278','123','567','879')
print(numbers[3])


# In[22]:


#Write a Python program to add an item in a tuple.
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = fruits + ('Apple',)
print(fruits)


# In[23]:


#Write a Python program to convert a tuple to a string.
def convertTuple(tup):
    str = ''.join(tup)
    return str
 
tuple = ('h', 'e', 'l', 'l', 'o')
str = convertTuple(tuple)
print(str)


# In[24]:


#Write a Python program to find the length of a tuple.
fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(fruits))


# In[26]:


#Write a Python program to add member(s) in a set and clear a set.
color = {'Red','Orange','Blue','Black'}
print(color)
#Adding element in set.
color.add('Yellow')
print(color)
#Clearing a set.
color.clear()
print(color)


# In[27]:


#Write a Python program to remove an item from a set if it is present in the set.
color = {'Red','Orange','Blue','Black'}
color.discard('Black')
print(color)


# In[28]:


#Write a Python program to create an intersection, Union, difference of sets.
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
C = A.union(B)
D = A.intersection(B)
E = A.difference(B)
print(C)
print(D)
print(E)


# In[30]:


#Write a Python program to find maximum and the minimum value in a set.
A = {0, 2, 4, 6, 8};
print(max(A))
print(min(A))


# In[31]:


#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#dictionary
def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value))
if __name__ == "__main__":
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 
    CountFrequency(my_list)


# In[ ]:




