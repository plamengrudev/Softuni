rows=int(input())
array=[]
numbers=[]

for i in range(rows):
    numbers=[int(x) for x in input().split(', ')]
    array.append([x for x in numbers if x%2==0])

print(array)


# 2
# 1, 2, 3
# 4, 5, 6