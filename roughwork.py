s={2,4,67,7,8,5}
m={2,4,3,6,9,"keshav","gopika",True}
print(s)

print(s.union(m))
print(s.intersection(m))               
print(s.symmetric_difference(m))               
print(s.issuperset(m))               
print(s.issubset(m))               

s.add("keshav")
print(s)

s.remove("keshav")
print(s)

m.pop(True)
