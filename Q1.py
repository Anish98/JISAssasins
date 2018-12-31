#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1
from collections import Counter
a = input("Enter a four-digit number please: ")
digit_counter = Counter(map(lambda x: int(x), a))
while True:
    if len(a) == 4:
        break
    else:
        
        a = input("Enter a four-digit number please: ")
        digit_counter = Counter(map(lambda x: int(x), a))

print("Zero count", digit_counter[0])
print("Even count", digit_counter[2] + digit_counter[4] + digit_counter[6] + digit_counter[8])
print("Odd count", digit_counter[1] + digit_counter[3] + digit_counter[5] + digit_counter[7] + digit_counter[9])

