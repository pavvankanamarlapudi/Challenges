#!/usr/bin/env python
# coding: utf-8

# ## ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question:1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####



lis = ['abcefc','xygyz','abeba','123321']




def palindrome_strings_count(input_arr):
    return len(list(filter(lambda x:x==x[::-1],[x for x in input_arr if len(x)>2])))




palindrome_strings_count(lis)


# ## ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question:2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####



lisA=['apple','banana','orange']
lisB=['mango','apple','orange']




def common_elems_cnt(arr1,arr2):
    return len(set(arr1).intersection(set(arr2)))




common_elems_cnt(lisA,lisB)


# ### ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question:3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####
# * Updated



import string




sample = [x for x in string.ascii_lowercase][:14]
sample




def even_odd_dict(input_arr):
    return [{x:y} for x,y in dict(zip(sample[::2],sample[1::2])).items()]#dict(zip(sample[::2],sample[1::2]))




even_odd_dict(sample)


# ### ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question:4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####



sample_lis = ['ab1c2','de234m5','abc123']




def get_max_num_list(input_arr):
    input_arr = list(set(input_arr))
    res = dict(zip([len([x for x in word if x.isdigit()]) for word in sample_lis],input_arr))
    return res[max(res.keys())]




get_max_num_list(sample_lis)


# ### ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question:5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####



test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4, 5] }
test_dict2 = { "Key1" : [1, 7, 3] }




def common_values(dicA,dicB):
    res = dict()
    for key in dicA: 
        if key in dicB: 
            res[key] = []
            for val in dicA[key]:
                if val in dicB[key]:
                    res[key].append(val)
    return res




common_values(test_dict1,test_dict2)


# ### ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question:6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####



dicA = {'a':1,'b':2,'d':5}
dicB = {'c':1,'a':2,'d':3}




def merge_dicts(dicA,dicB):
    res={}
    for k,v in dicA.items():
        if k in dicB:
            res[k]=dicA[k]+dicB[k]
        else:
            res[k]=v
    return {**res,**{x:y for x,y in dicB.items() if not x in res}}




merge_dicts(dicA,dicB)


# ### ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question:7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####



sample_tuple=[(1,2),(2,4),(5,6)]




def remove_tuple(tup_arr,N):
    return [x for x in sample_tuple if not N in x]




remove_tuple(sample_tuple,6)


# ### ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question:8~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####



def sort_list_by_tuples(tup_arr):
#     global tup_arr
    tup_arr.sort(key=lambda y:y[0])




sample_tuple2 = [(5,6),(2,4),(1,2)]
sort_list_by_tuples(sample_tuple2)
sample_tuple2

