class Rhombus:

    def __init__(self, size):
        self.size=int(size)
    
    def print_rhombus(size):
        for i in range(size):
            print(" "*(size-i)+"* "*(i))
        for i in range(size,0,-1):
            print(" "*(size-i)+"* "*(i))


n=int(input())
Rhombus.print_rhombus(n)
