def type_check(t):
    def decorator(func):
        def wrapper(*args):
            for item in args:
                if not isinstance(item,t):
                    return f"Bad Type"
            return func(*args)

        return wrapper
    return decorator

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))