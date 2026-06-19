word_dict={}
results=[]
try:
    with open('words.txt','r') as file:
        line=file.readline()
        words=[x for x in line.split()]
        for word in words:
            if word not in word_dict.keys():
                word_dict[word.lower()]=0
except FileNotFoundError:
    pass

try:
    with open('input.txt','r') as input_f:
        lines=[x for x in input_f.read().split("\n")]
        for line in lines:
            for word in word_dict.keys():
                if word in line.lower():
                    word_dict[word]+=1
except FileNotFoundError:
    pass

sorted_data=sorted(word_dict.items(),key=lambda x: -x[1])
results=[f"{key} - {value}" for key, value in sorted_data]

with open('text.txt','w') as w_file:
    print('\n'.join(results))
