def reverse_text(word: str):
    i=len(word)-1
    while i>=0:
        yield word[i]
        i-=1


for char in reverse_text("step"):
    print(char, end='')