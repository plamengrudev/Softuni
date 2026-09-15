from collections import deque

def possible_permutations(coll):

    if len(coll)<=1:
        yield coll
    else:
        for i in range(len(coll)):
            for perm in possible_permutations(coll[:i]+coll[i+1:]):
                yield [coll[i]]+perm


[print(n) for n in possible_permutations([1, 2, 3])]