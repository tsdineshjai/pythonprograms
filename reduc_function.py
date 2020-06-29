list22 = [2,4,6,10]
from functools import reduce

def mult_elements(n1,n2):
    return n1*n2

print(reduce(mult_elements,list22,5))
#  the reduce fucntion is handy in place of loop as it makes the code simple and clean