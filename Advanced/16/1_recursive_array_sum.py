def calc_sum(numbers, idx):
    if idx==len(numbers)-1:
        return numbers[idx]
    
    return numbers[idx]+calc_sum(numbers,idx+1)

input_array=[int(x) for x in input().split()]
print(calc_sum(input_array,0))