# -*- coding: utf-8 -*-
"""
Created on Sun May  8 12:12:06 2022

@author: Doğuş
"""

# FLATTEN

a = [[1,2],["patika" , 15],[14.8, 20]]

        
new_a =[]

for i in a:
    for e in i :
        new_a.append(e)
        print(e)
        

print(new_a)


# REVERSE

b = [[1,2],["patika" , 15],[14.8, 20]]

b= b[::-1]


for i in range (len(b)) :
    (b[i])=(b[i])[::-1]
print(b)
