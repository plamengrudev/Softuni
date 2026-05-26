rows,columns=[int(x) for x in input().split(', ')]
array=[]

for i in range(rows):
    array.append([int(x) for x in input().split(' ')])

for i in range(columns):
    sum=0
    for j in range(rows):
        sum+=array[j][i]
    print(sum)



# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0