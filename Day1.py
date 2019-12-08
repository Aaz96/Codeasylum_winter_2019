#!/usr/bin/env python
# coding: utf-8

# In[2]:


nums = input()
summ =0
mul =1
for i in nums.split():
    summ = summ+int(i)
    mul = mul*int(i)
print(summ)
print(mul)
print(summ/len(nums.split()))


# In[11]:


def summ(nums):
    summ =0
    for i in nums:
        summ = summ+int(i)
    return summ
def mul(nums):
    mul =1
    for i in nums:
        mul = mul*int(i)
    return mul
def avg(nums):
    for i in nums:
        add = add+int(i)
    return add/len(nums)
nums = input()
nums = [int(i) for i in nums.split()]


print(summ(nums))
print(mul(nums))
print(avg(nums))


# In[28]:


def summ(*nums):
    summ = sum(nums)
    return summ
def mul(*nums):
    mul =1
    for i in nums:
        mul = mul*int(i)
    return mul
def avg(*nums):
    add= 0
    for i in nums:
        add = add+int(i)
    return add/len(nums)
nums = input()
nums = [int(i) for i in nums.split()]


print(summ(*nums))
print(mul(*nums))
print(avg(*nums))


# In[50]:


my_list = [['beautiful', 'soup','spacy','nltk']]
b = [*my_list]
print(b)


# # Cube

# In[53]:


def cube(nums):
    for i in range(len(nums)):
        if nums[i]>0:
            print(nums[i]**3)
        else:
            print(nums[i])
num = input()
nums = [int(i) for i in num.split()]

cube(nums)
    


# # Prime numbers

# In[80]:


def checking_prime(x,y):
    lst = []
    count=0
    for i in range(x,y):
        for j in range(2,i):
            if i%j==0:
                break
            else:
                lst.append(i)
    return set(lst)
n = int(input())
h = int(input())
checking_prime(n,h)       
    


# # Hello

# In[121]:


def hello(nums):
    lst = []
    while nums!=0:
        if nums>0:
#             print(num%10)
            lst.append(nums%10)
        nums = nums//10
#         print(num)
    lst = lst[::-1]
    print(lst)
    for i in lst:
        for j in range(1,i+1):
            print('Hello'+str(j), end="\t")
        print()
num = int(input())
hello(num)


# # Pattern

# In[184]:


def pattern(num):
    for i in range(1,num+1):
        for h in range(1,i):
            print(end = '\t')
        for j in range(i, num+1):
            print(j, end ='\t')
        print()
num = int(input())
pattern(num)


# # Second Largest

# In[188]:


def second_largest(lst):
    first = 0
    second = 0
    for i in range(len(lst)):
        if lst[i]>first:
            second = first
            first = lst[i]
        elif lst[i]>second and lst[i]<first:
            second = lst[i]
    return second
n = input()
lst = [int(i) for i in n.split()]
second_largest(lst)


# # Bus

# In[198]:


def bus(n):
    if n%6==0 or (n-1)%6==0:
        print('Window')
        print(str(n+6))
    elif n%3==0 or (n-1)%3==0:
        print('Away')
        print(str(n+6))
    else:
        print('Middle')
        print(str(n+6))
n = int(input())
bus(n)

