def sorting_cheeses(**kwargs):
    sorted_data=sorted(kwargs.items(),key=lambda x: (-len(x[1]),x[0]))

    results=[]

    for (cheese,pieces) in sorted_data:
        results.append(cheese)
        piece_list=sorted(pieces,reverse=True)
        results+=piece_list
    return "\n".join([str(x) for x in results])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)