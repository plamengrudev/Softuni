def fill_the_box(*args):
    numbers=[]
    for item in args:
        if item=="Finish":
            break
        else:
            numbers.append(int(item))
    height,length,width,*cubes=numbers
    big_c=int(height)*int(length)*int(width)
    if big_c-sum(cubes)>0:
        return f"There is free space in the box. You could put {big_c-sum(cubes)} more cubes."
    else:
        return f"No more free space! You have {abs(big_c-sum(cubes))} more cubes."
    
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))