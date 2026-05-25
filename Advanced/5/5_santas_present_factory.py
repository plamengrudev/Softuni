from collections import deque
from collections import OrderedDict

materials=[int(x) for x in input().split()]
magic_level=deque([int(x) for x in input().split()])
toys={
    "Doll":150,
    "Wooden train":250,
    "Teddy bear":300,
    "Bicycle":400
}
toys_created={
    "Doll":0,
    "Wooden train":0,
    "Teddy bear":0,
    "Bicycle":0
}

def build(mat,level):
    result=mat*level
    if result<0:
        result=mat+level
        materials.pop()
        magic_level.popleft()
        materials.append(result)
    elif result>0 and result in toys.values():
        for toy in toys.keys():
            if result-toys[toy]==0:
                toys_created[toy]+=1
                materials.pop()
                magic_level.popleft()
    elif result>0:
        magic_level.popleft()
        materials[-1]+=15


while materials and magic_level:
    if materials[-1]==0 and magic_level[0]==0:
        materials.pop()
        magic_level.popleft()
        continue
    if magic_level[0]==0 or materials[-1]==0:
        if magic_level[0]==0:
            magic_level.popleft()
        else:
            materials.pop()
        continue
    build(materials[-1],magic_level[0])

if (toys_created["Doll"]>0 and toys_created["Wooden train"]>0) or (toys_created["Teddy bear"]>0 and toys_created["Bicycle"]>0):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str,reversed(materials)))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str,magic_level))}")

for k,v in sorted(toys_created.items()): print(f"{k}: {v}") if v>0 else None



