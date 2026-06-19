def calc_fact(num):
    if num==1:
        return num
    return num * calc_fact(num-1)

number=int(input())
print(calc_fact(number))