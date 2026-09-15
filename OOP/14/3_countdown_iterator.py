class countdown_iterator:

    def __init__(self,count: int):
        self.count=count
        self.i=self.count+1
    

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i>0:
            self.i-=1
            return self.i
            
        else:
            raise StopIteration()
        


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
