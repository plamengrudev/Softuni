def recursive_power(n, power):
    result=1
    if power==0:
        return result
    result=n*recursive_power(n, power-1)
    return result

print(recursive_power(2, 10))
print(recursive_power(10, 100))