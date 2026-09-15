def read_next(*colls):
    for coll in colls:
        yield from coll


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')