import math
count=int(input())
odd_n=set()
even_n=set()

for line in range(1,count+1):
    word=input()
    sum_w=0
    for ch in word:
        sum_w+=ord(ch)
    if int(sum_w/line)%2==0:
        even_n.add(int(sum_w/line))
    else:
        odd_n.add(int(sum_w/line))

if sum(odd_n)==sum(even_n):
    print(f"{', '.join(map(str,(odd_n.union(even_n))))}")
elif sum(odd_n)>sum(even_n):
    print(f"{', '.join(map(str,(odd_n.difference(even_n))))}")
elif sum(odd_n)<sum(even_n):
    print(f"{', '.join(map(str,(odd_n.symmetric_difference(even_n))))}")

