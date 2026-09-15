def squares(size:int):
    i = 1
    while i<=size:
        yield i*i
        i+=1


print(list(squares(5)))