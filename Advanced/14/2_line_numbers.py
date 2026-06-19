chars=[]
signs=[]
lines=[]

with open('text.txt','r') as input_file:
    lines=(input_file.read().split('\n'))

def count_symbols(line):
    for char in line:
        if char.isalpha():
            chars.append(char)
        else:
            if char==' ':
                pass
            else:
                signs.append(char)



for i in range(len(lines)):
    count_symbols(lines[i])
    print(f"Line {i+1}: {lines[i]} ({len(chars)})({len(signs)})")
    chars=[]
    signs=[]
