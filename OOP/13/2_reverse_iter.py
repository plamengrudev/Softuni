class reverse_iter:

    def __init__(self, array:list):
        self.array=array
        self.a=len(self.array)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a>0:
            self.a-=1
            return self.array[self.a]
        else:
            raise StopIteration()
    


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
