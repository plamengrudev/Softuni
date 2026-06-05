from functools import reduce

def even_odd_filter(**kwargs):
    result={}

    for check, els in kwargs.items():
        if check == "even":
            result[check]=[int(x) for x in els if int(x)%2==0]
        elif check == "odd":
            result[check]=[int(x) for x in els if int(x)%2!=0]
    
    return dict(
        sorted(result.items(),key=lambda x: (len(x[1])),reverse=True)
    )

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))