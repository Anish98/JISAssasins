#!/usr/bin/env python
# coding: utf-8

# In[8]:


#question 10
print("Enter 'x' for exit.")
string = input("Enter any string to remove all vowels from it: ")
if string == 'x':
    exit();
else:
    newstr = string;
    print("\nRemoving vowels from the given string...");
    vowels = ('a', 'e', 'i', 'o', 'u');
    for x in string.lower():
        if x in vowels:
            newstr = newstr.replace(x,"");
    print("New string after successfully removed all the vowels:");
    print(newstr);


# In[ ]:



