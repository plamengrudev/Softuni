from functools import reduce

def neg_vs_pos(*args):
    nums=args
    neg=reduce(lambda x,y: (x+y) if y<0 else x,nums,0)
    pos=reduce(lambda x,y: (x+y) if y>0 else x,nums,0)
    print(neg)
    print(pos)
    if abs(neg)>pos:
        return f"The negatives are stronger than the positives"
    else:
        return f"The positives are stronger than the negatives"

line=[int(x) for x in input().split()]

print(neg_vs_pos(*line))