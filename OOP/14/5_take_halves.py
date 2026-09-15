def solution():
    def integers():
        x=0
        while True:
            x+=1
            yield x
    def halves():
        for i in integers():
            yield i/2
    def take(n, seq):
        result=[]
        for _ in range(n):
            result.append(next(seq))
        return result


    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))