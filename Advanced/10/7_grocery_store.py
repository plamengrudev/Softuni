def grocery_store(**kwargs):
    result=[]
    sorted_data=sorted(kwargs.items(),key=lambda x: (-(x[1]),-len(x[0]),x[0]))
    for item in sorted_data:
        result.append(f'{item[0]}: {item[1]}')
        
    return '\n'.join(result)

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))