def my_func(arg1,arg2):
    return arg1+arg2
# arg refers to argument
x = map(my_func,('book', 'orange', 'football'), ('arsenal', 'indian', 'hollywood'))
print(x)
print(list(x))