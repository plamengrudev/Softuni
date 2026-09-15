class vowels:

    def __init__(self,word:str):
        self.word=word
        self.l=-1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.l+=1
        if self.l>=len(self.word):
            raise StopIteration()
        if self.word[self.l].lower() in ['a','o','e','i','u','y']:
            return self.word[self.l]
        else:
            return self.__next__()
        

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
