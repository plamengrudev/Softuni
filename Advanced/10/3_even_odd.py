def even_odd(*args):
    *numbers, command=args
    if command=="even":
        evens=[int(x) for x in numbers if int(x)%2==0]
        return evens
    elif command=="odd":
        odds=[int(x) for x in numbers if int(x)%2!=0]
        return odds

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))