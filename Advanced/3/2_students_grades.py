import statistics
count=int(input())
students={}
for i in range(count):
    student, grade=[x for x in input().split()]
    if student in students.keys():
        students[student]["grades"].append(float(grade))
    else:
        students[student]={"grades":[float(grade)]}
    
for student in students.keys():
    average=sum(students[student]['grades'])/len(students[student]['grades'])
    print(f"{student} -> {' '.join(format(x,'.2f') for x in students[student]['grades'])} (avg: {average:.2f})")
