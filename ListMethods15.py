# agar apako list me kuch add karana hai to append word use karake aap add kar sakate ho

l=[2,4,9,1,45,6]
print(l)
l.append(8)
print(l)
# Agar tumhe list ko sort karana hai to l.sort keyword use karana hai
l.sort()
print(l)
#aagr sorting apako desending order me sort karana hai to reverse=True karana hai
l.sort(reverse=True)
print(l)
# originalm list ko reverse karanae ke leye l.reverse use hita hai
l.reverse
print(l)
#agar muze dekhana hai ki ek particular value ek list me kitani bar repeat hue hai 
print(l.count(1))
print(l)
# agar muze perticular index per koi particular value inseart karani hai to
l.insert(1,34)
print(l)
#agar muze kuch values kisi list ke last me dalani hai to apako sir ye karana hai
m=[20,54,10]
'''l.extend(m)
print(l)'''
#jab hame kisi bhi list ko bina change kiye list me last me koi elements ko add karana hai to 
k=l+m
print(k)
