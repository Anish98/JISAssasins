#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question23

string=input("enter the string ")
count=0
for i in string:
    count=count+1
print("length of string is ",count)
list=string.split(" ")
list.reverse()
print(string[::-1])
string1=input("enter the string ")
s3=string+string1
print(s3)
if(string==string1):
    print("they are equal ")
else:
    print("they are not equal")
if (string1==string):
    exit()
else:
    print (string1)


# In[ ]:




