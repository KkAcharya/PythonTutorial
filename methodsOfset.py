#union operation

s1={1,2,3,4}
s2={4,5,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

#intersaction opration in set
cities1={"mumbai","thane","lakhanau","delhi"}
cities2={"mumbai","thane","pune","solapur"}
cities3=cities1.intersection(cities2)
print(cities3)

# diffference and difference update
cities3=cities1.difference(cities2)
print(cities3)

#isdisjoint opration in set
s3={"keshav","shivraj","pradip","prathamesh"}
s4={"ashish","rihan","ayush","keshav","shivraj","pradip","prathamesh"}
print(s3.issubset(s4))
