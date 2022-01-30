#!/usr/bin/env python
# coding: utf-8

# ## Question:1

# In[10]:


lis = ['abcefc','xygyz','abeba','123321']


# In[12]:


def palindrome_strings_count(input_arr):
    return len(list(filter(lambda x:x==x[::-1],[x for x in input_arr if len(x)>2])))


# In[18]:


#version:2
def palindrome_strings_count(input_arr):
    cnt=0
    for word in input_arr:
        if len(input_arr)>2 and word==word[::-1]:
            cnt+=1
    return cnt


# In[19]:


palindrome_strings_count(lis)


# ## Question:2

# In[15]:


lisA=['apple','banana','orange']
lisB=['mango','apple','orange']


# In[21]:


def common_elems_cnt(arr1,arr2):
    return len(set(arr1).intersection(set(arr2)))


# In[22]:


common_elems_cnt(lisA,lisB)


# ### Question:3
# * Updated

# In[1]:


import string


# In[2]:


sample = [x for x in string.ascii_lowercase][:14]
sample


# In[7]:


def even_odd_dict(input_arr):
    return [{x:y} for x,y in dict(zip(sample[::2],sample[1::2])).items()]#dict(zip(sample[::2],sample[1::2]))


# In[27]:


def even_odd_dict(input_arr):
    res=[]
    for x,y in dict(zip(input_arr[::2],input_arr[1::2])).items():
        res.append({x:y})
    return res


# In[28]:


even_odd_dict(sample)


# ### Question:4

# In[29]:


sample_lis = ['ab1c2','de234m5','abc123']


# In[63]:


def get_max_num_list(input_arr):
    input_arr = list(set(input_arr))
    res = dict(zip([len([x for x in word if x.isdigit()]) for word in sample_lis],input_arr))
    return res[max(res.keys())]


# In[34]:


def get_max_num_list(input_arr):
    res={}
    for word in input_arr:
        cnt=0
        for i in word:
            if i.isdigit():
                cnt=cnt+1
        res[cnt]=word
    return res[max(res.keys())]


# In[35]:


get_max_num_list(sample_lis)


# ### Question:5

# In[108]:


test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4, 5] }
test_dict2 = { "Key1" : [1, 7, 3] }


# In[106]:


def common_values(dicA,dicB):
    res = dict()
    for key in dicA: 
        if key in dicB: 
            res[key] = []
            for val in dicA[key]:
                if val in dicB[key]:
                    res[key].append(val)
    return res


# In[109]:


common_values(test_dict1,test_dict2)


# ### Question:6

# In[81]:


dicA = {'a':1,'b':2,'d':5}
dicB = {'c':1,'a':2,'d':3}


# In[84]:


def merge_dicts(dicA,dicB):
    res={}
    for k,v in dicA.items():
        if k in dicB:
            res[k]=dicA[k]+dicB[k]
        else:
            res[k]=v
    return {**res,**{x:y for x,y in dicB.items() if not x in res}}


# In[85]:


merge_dicts(dicA,dicB)


# ### Question:7

# In[36]:


sample_tuple=[(1,2),(2,4),(5,6)]


# In[92]:


def remove_tuple(tup_arr,N):
    return [x for x in sample_tuple if not N in x]


# In[40]:


def remove_tuple(tup_arr,N):
    res=[]
    for tup in tup_arr:
        if not N in tup:
            res.append(tup)
    return res


# In[94]:


remove_tuple(sample_tuple,6)


# ### Question:8

# In[103]:


def sort_list_by_tuples(tup_arr):
#     global tup_arr
    tup_arr.sort(key=lambda y:y[0])


# In[104]:


sample_tuple2 = [(5,6),(2,4),(1,2)]
sort_list_by_tuples(sample_tuple2)
sample_tuple2

