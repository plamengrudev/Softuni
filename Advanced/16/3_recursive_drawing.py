def print_figure(n):
    if n<=0:
        return
    print('*' * n)
    print_figure(n-1)
    print('#' * n)

input_n=int(input())
print_figure(input_n)