# for loop with else in python


'''for i in range(4):
    print(i)            # to is program me hamara else ka part print hoga ku ki for loop jab sare iteration ko suceesfully complte kar
                        # dega tab hamara else ka content print hoga
    
else:
    print("sorry no i ")'''

# par jab ham isame  break laga denge to hamara else ka part print nahi hoga ku ki 
#jab else ka part print ho gaya tha tab hamara loop sabhi itearation ko complete karake aaya tha .. apr jab loop me brak laga diya 
# to loop khatam ho gaya ...aur hamara else ka part print nahi hoaga
for i in range(4):
    print(i)
    if i==2:
     break
else:
     print("no i here")