def age_assignment(*names,**kwargs):
    temp={}
    people={}
    result=[]

    for letter,age in sorted(kwargs.items()):
        temp[letter]=int(age)
        for name in names:
            if letter in name:
                people[name]=age
    result=[f"{name} is {age} years old." for name,age in people.items()]
    return '\n'.join(result)

    

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))