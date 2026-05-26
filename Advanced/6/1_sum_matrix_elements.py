rows,columns=[int(x) for x in input().split(', ')]
array=[]
summ=0
for i in range(rows):
    array.append([int(x) for x in input().split(', ')])
    summ+=sum(array[i])

print(summ)
print(array)


# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0