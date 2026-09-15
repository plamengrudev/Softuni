def tags(tag:str):
    def decorator(func):
        def wrapper(*args,**kwargs):
            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper
    return decorator

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))