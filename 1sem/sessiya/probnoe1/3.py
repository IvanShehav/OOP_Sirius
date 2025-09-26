def to_string(*values, sep=' ', end='\n'):
    return sep.join(str(elem) for elem in values) + end
print(to_string(7,3,1, "hello", (1,2,3), sep = ' ', end = '!'))