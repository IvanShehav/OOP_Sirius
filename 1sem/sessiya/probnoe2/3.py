def to_string(*evals, sep=' ', end='\n'):
    return sep.join(str(x) for x in evals) + end
print(to_string(1,2,3))
