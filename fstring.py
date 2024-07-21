#f string in python
'''letter="hey my name is {1} and i am from {0}"'''
country="india"        # to usane kya kiya ki 0 index pe kon hai use populate kar diya {} braces me 
                        #and 1  index pe kon hai use populate kar diya {} me
name="keshav"
#print(letter.format(country,name))
# agar isis program ko mai fstring ke madat se karu to
print(f"hey my name is {name} and i am from {country}")
 # agar muze name ki jagah name hi rakhana hai to to kya karge ... to sirf {{}}curly braces lagaenge 
print(f"hey my name is {{name}} and i am from {{country}}" )