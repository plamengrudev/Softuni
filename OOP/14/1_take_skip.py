class take_skip:

    def __init__(self,step:int,count:int):
        self.step=step
        self.count=count
        self.i=1
        self.n=0
    

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i<=self.count:
            self.i+=1
            n=self.n
            self.n+=self.step
            return n
        else:
            raise StopIteration()


numbers = take_skip(10, 5)
for number in numbers:
    print(number)


