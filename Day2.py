#!/usr/bin/env python
# coding: utf-8

# # Reversing the case

# In[ ]:


string = 'PyThON'
rev_str=''
for i in string:
    if i ==i.lower():
        rev_str+=i.upper()
                
    else:
        rev_str += i.lower()
print(rev_str)


# # ADDREV

# In[ ]:


n= int(input())
for i in range(n):
    add =0
    num = input()
    num1, num2 = num.split()
    num1 = num1[::-1]
    num2 = num2[::-1]
    add = str(int(num1)+int(num2))
    print(int(add[::-1]))


# # Linear search

# In[ ]:


n = int(input("Enter the size of list: "))
k  = int(input('Search element please: '))
lst=[]
for i in range(n):
    lst.append(int(input()))
a = [i for i in range(len(lst)) if lst[i]==k]
print(*a)


# # Runner up

# In[ ]:


def runner_up(arr):
    
    sort = sorted(arr, reverse =True)
    for i in sort:
        if i!=max(sort):
            return(i)
    

n = int(input())
arr = list(map(int, input().split()))
print(runner_up(arr))


# # CRDS

# In[ ]:


n= int(input())
for i in range(n):
    add=0
    num = int(input())
    num %= 1000007
    add = (3*(num**2)/2)+(num/2)
    print(int(add))


# # Difference b/n product and addition

# In[ ]:


def add_mul(num):
    add = 0
    mul = 1
    while(num!=0):
        a = num%10
        num = num//10
        add += a
        mul *= a
    return (mul-add)
        
num = int(input())
print(add_mul(num))


# # Grading

# In[ ]:


import math

num = int(input())
for i in range(num):
    n = int(input())
    if n>=38 and (n%5)>=3:
        print((n+(5-(n%5))))
    else:
        print(n)


# In[ ]:




