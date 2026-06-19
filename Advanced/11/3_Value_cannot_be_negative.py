class ValueCannotBeNegative(Exception):
    """Number is below zero"""
    pass

for i in range(5):
    n=int(input())
    if n<0:
        raise ValueCannotBeNegative