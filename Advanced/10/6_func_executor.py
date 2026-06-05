def func_executor(*args):
    commands=[x for x in args]
    results=[]
    for command in commands:
        func=command[0]
        params=[x for x in command[1]]
        results.append(f"{func.__name__} - {func(*params)}")
    
    return "\n".join(results)

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))