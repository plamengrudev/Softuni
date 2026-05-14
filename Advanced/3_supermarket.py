from collections import deque
queue=deque([])

while True:
    inp_text=input()
    if inp_text=="End":
        print(f"{len(queue)} people remaining.")
        break
    elif inp_text=="Paid":
        for i in range(len(queue)):
            print(f"{queue.popleft()}")
    else:
        queue.append(inp_text)