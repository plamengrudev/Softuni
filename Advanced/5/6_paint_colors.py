from collections import deque
main_colors=["red","yellow","blue"]
sec_colors=["orange","purple","green"]
all_colors=main_colors+sec_colors

raw_string=deque(input().split())
colors_result=[]

def check_colors(concatenated_string):
    raw_string.pop()
    raw_string.popleft()
    colors_result.append(concatenated_string)

while len(raw_string)>0:
        if len(raw_string)>1:
            concat_sub = raw_string[0] + raw_string[-1] if raw_string[0] + raw_string[-1] in all_colors else raw_string[-1] + raw_string[0]
            if concat_sub in all_colors:
                check_colors(concat_sub)
            
            else:
                pre=raw_string.popleft()
                post=raw_string.pop()
                pre=pre[:-1]
                post=post[:-1]
                mid=len(raw_string)//2
                if post:
                    raw_string.insert(mid,post)
                if pre:
                    raw_string.insert(mid,pre)
        else:
            concat_sub=raw_string[0]
            if concat_sub in main_colors or concat_sub in sec_colors:
                raw_string.pop()
                colors_result.append(concat_sub)
            else:
                 raw_string[0]=raw_string[0][:-1]
            if raw_string:
                if raw_string[0]=='':
                    raw_string.pop()
        


if "orange" in colors_result:
    if "red" in colors_result and "yellow" in colors_result:
        pass
    else:
        colors_result.remove("orange")
if "purple" in colors_result:
    if "red" in colors_result and "blue" in colors_result:
        pass
    else:
        colors_result.remove("purple")
if "green" in colors_result:
    if "blue" in colors_result and "yellow" in colors_result:
        pass
    else:
        colors_result.remove("green")
print(colors_result)





