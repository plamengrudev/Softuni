def math_operations(*args,**kwargs):
    numbers=[float(x) for x in args]
    kv_p={}
    for key, value in kwargs.items():
        kv_p[key]=float(value)
    for i in range(len(numbers)):
        if i%4==0:
            kv_p['a']+=numbers[i]
        elif i%4==1:
            kv_p['s']-=numbers[i]
        elif i%4==2:
            if numbers[i]==0:
                continue
            else:
                kv_p['d']/=numbers[i]
        elif i%4==3:
            kv_p['m']*=numbers[i]
    sorted_data=sorted(kv_p.items(),key=lambda x: (-(x[1]),x[0]))
    result=[f"{key}: {value:.1f}" for key,value in sorted_data]
    return '\n'.join(result)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
