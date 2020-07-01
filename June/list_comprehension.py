#1  using list comprehension
elements = [x for  x in 'arsenal']
print(elements)

# 2
#using lambda  inside a list
letters = list(map(lambda x : x, 'arteta'))
print(letters)

#3 Conditionals in List Comprehension
filtered_list = [ x for x in range(50) if x % 3 == 0]
print(filtered_list)

#4  Nested IF with List Comprehension

double_filteredlist = [ x for x in range (100) if x % 6 == 0 if x % 8 == 0]
print(double_filteredlist)

