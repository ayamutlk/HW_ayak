#Q1 the tuple key for relevant declarations.
# dict1 = {("Name, last_name"):"aya kaabyia","age":27,"phone number":5847772018}
# print(dict1)



#Q2
# def func(lst):
#     try:
#         len(lst) < 6
#     except:
#         print(" the fifth index doesn’t exist in the list")
#     else:
#         lst[5] = "@"
#         return lst
#
# print(func([1, 2, 3, 4, 5, 6]))




#Q3

# def func(lst):
#     try:
#         assert len(lst) > 5 , "Fifth index doesn’t exist in the list "
#     except:
#         print("Fifth index doesn’t exist in the list ")
#     else:
#         lst[5]='@'
#         return lst
# print(func([1,2,3,4,5,6,7]))

#or
# def func(lst):
#     assert len(lst) > 5 , "Fifth index doesn’t exist in the list "
#     lst[5]='@'
#     return lst
# print(func([1,2,3,4,7,3,5]))



#Q4 (dict 1+ dict 2 = dict 3)
# def func(dict1,dict2):
#     dict1.update(dict2)
#     return (dict1)
# print(func({'a':1,'b':2,'c':3},{'d':4}))


#or (dictinary + new key +new valeu =new dict)
# def func(dict1,new_key,new_value):
#     d={new_key:new_value}
#     dict1.update(d)
#     return (dict1)
# print(func({'a':1,'b':2,'c':3},'d',4))




#Q5
# n=5
# dict1 = {}
# for x in range(1,n+1):
#     dict1[x]=x+3
#
# print(dict1)
#

#or
# dic1={}
# n=input('plz enter a number: ')
# x=1
# while x<=int(n):
#     d={x:x+3}
#     dic1.update(d)
#     x+=1
# print(dic1)



#Q6
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)



#Q7
# def count_char_appearances (str):
#     new_d={}
#     for ch in str:
#         if ch not in new_d.keys():
#             new_d.update({ch:1})
#         else:
#             old_value=new_d[ch]
#             new_d.update({ch:old_value+1})
#     return new_d
#
#
# print(count_char_appearances('Aya'))


#or
# def count_char_appearances (str):
#     new_d={}
#     for ch in str:
#         count = new_d.get(ch,0)
#         count += 1
#         new_d[ch] = count
#     chars =new_d.keys()
#     chars = sorted(chars)
#     return new_d
#
# print(count_char_appearances('Ayaaa'))




#Q8
# from collections import Counter
# dic1 = {'a': 100, 'b': 200, 'c':300}
# dic2 = {'a': 300, 'b': 200, 'd':400}
# new_d = Counter(dic1) + Counter(dic2)
# print(new_d)
#
#
# or
# d1 = {'a':100, 'b':200,'c':300}
# d2 = {'a':300, 'b':200,'d':400}
# for key in d1:
#     if key in d2:
#         d1[key]= d1[key] + d2[key]
#     else:
#         pass
# print(d1)