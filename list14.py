# list are oderd collection of data items


"""l=[3,5,4]
print(l)
print(type(l))  #type batane ke liye """

# agar aap yaha pe agar marks ki list bana cahhaete ho to

marks=[70,76,98,"keshav",True]
"""print(marks)
print(marks[0])  # yaha par aap ne jab marks 0 lkha to iska matalab hai 0 index pe jo value hai use display karo aur same hai 1 and 2 ka
print(marks[1])
print(marks[2])   # list ke under multiple number of data type aa sakate hai
print(marks[3])
print(marks[4])"""

# agar apako kabhi bhi negative index mil gayi to uusse { length(list)-negative index}  positive index me convert karana hai
print(marks[-3])
print(marks[len(marks)-3])  # 4 statement ka meaning ek hi hai to muze char bar 98 milega
print(marks[5-3])
print(marks[2])
# agar muze dekhana ahi ki 7 mere list me hai ya nahi to hm use in keyword ka use karake kar sakate hai
'''if 76 in marks :
    print("yes")  # hm string ko bhi search kar sakate hai
else:
    print("No")'''

