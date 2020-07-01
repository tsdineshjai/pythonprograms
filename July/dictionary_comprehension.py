# Dictionary comprhension
dict_nary = { 'jai' : 10 , 'ammu' : 3}
# increase the 'value 'by its square
new_dict = {key:value**2 for key,value in dict_nary.items() }
print(new_dict)
