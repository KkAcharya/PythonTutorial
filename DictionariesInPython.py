#dictionaries in python
 
info={'name':'keshav','age':19,'eligible':True}
print(info)
#agar uze dekhana hai ki name key ke jagah kya value hai to
print(info['age'])
# or
print(info.get('name'))

'''print(info['name2']) #ye line error show karegi
print(info.get('name2')) # but ye wali line error show nahi karegi sirrf  None return karegi

'''
# how to acess multiple value 
print(info.keys()) #keys show karane ke liye
print(info.values())# values show karane ke liye

# aap ise iterate karake bhi acess kar sakate ho
'''for key in info.keys():
 print(info[key])'''
 # agr aap pairs me key value acess karana chahate ho to
 #print(info.items())

 #agar aap isko iterate karana chahate ho to
for key,value in info.items():
    print("the corresponding to the key{key} is(info[key]}")