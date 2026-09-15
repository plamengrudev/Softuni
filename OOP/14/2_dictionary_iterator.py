class dictionary_iter:

    def __init__(self, coll: dict):
        self.coll=coll
        self.i=0
        self.keys=list(self.coll.keys())
        self.values=list(self.coll.values())

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i<len(self.coll):
            key=self.keys[self.i]
            value=self.values[self.i]
            self.i+=1
            return (key,value)
        else:
            raise StopIteration()
        

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)