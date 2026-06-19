import re
lines=[]
replaced=[]
reverted=[]
results=[]

with open('text.txt','r') as i_file:
    lines=i_file.read().split('\n')

for line in lines:
    replaced.append(re.sub(r"[-,.!?]","@",line))

for rep in replaced:
    reverted.append(' '.join(rep.split()[::-1]))

for i in range(len(reverted)):
    if i%2==0:
        results.append(reverted[i])

print("\n".join(results))