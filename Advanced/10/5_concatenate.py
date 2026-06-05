def concatenate(*args,**kwargs):
    line=''.join([x for x in args])
    for key,value in kwargs.items():
        if key in line:
            line=line.replace(key,value)

    return line

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
