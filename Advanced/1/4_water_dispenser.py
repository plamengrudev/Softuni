from collections import deque
queue=deque([])
water=int(input())
while True:
    command=input()
    if command=="Start":
        while True:
            action=input()
            if action=="End":
                print(f"{water} liters left")
                break
            elif action.isdigit():
                if int(action)<=water:
                    water-=int(action)
                    print(f"{queue.popleft()} got water")
                else:
                    print(f"{queue.popleft()} must wait")
            else:
                args=action.split()
                refill_water=int(args[1])
                water+=refill_water
        break
    else:
        queue.append(command)

