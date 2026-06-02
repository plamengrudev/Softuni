matrix=[[int(x) for x in b.split()] for b in input().split("|")]
print(' '.join([str(el) for row in reversed(matrix) for el in row]))