def get_primes(nums:list):
    for num in nums:
        if num<2:
            continue
        else:
            prime=True
            for n in range(2,num):
                if num%n==0:
                    prime=False
            if prime:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
