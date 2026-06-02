from functools import reduce

mapper={
    '+': lambda x,y: (x+y),
    '-': lambda x,y: (x-y),
    '*': lambda x,y: (x*y),
    '/': lambda x,y: (x/y)
}

def operate(sign,*args):
    return reduce(mapper[sign],args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))