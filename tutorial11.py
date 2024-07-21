#   Break and countinue statement 

# create a table using for loop
"""
for i in range(11):
  print("5 X",i+1,"=",5 * (i+1))"""

#User input table 
'''
n=int(input("enter the number")) 
for i in range(11):
  print("n X",i+1,"=",n *(i+1))'''

# break and countinue statement i for loop
n=int(input("enter a number "))
for i in range(11):
  if(i==10):                              # agar hamako ye program user input banana hai to hame sirf 
                                        # user input ki line dalani hai
    break
  print("n X",i+1,n * (i+1))
   
else:
  print(" loop se bahar aa gaya")
