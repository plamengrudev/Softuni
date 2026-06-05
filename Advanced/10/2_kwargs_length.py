def kwargs_length(**kwargs):
    return len(kwargs.items())

dictionary = {}

print(kwargs_length(**dictionary))