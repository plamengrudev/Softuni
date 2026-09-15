class sequence_repeat:


    def __init__(self,word:str,n:int):
        self.word=word
        self.n=n
        self.i=-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i<self.n-1:
            self.i+=1
            return self.word[(self.i)%len(self.word)]
        else:
            raise StopIteration()
        

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')