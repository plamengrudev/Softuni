from collections import deque
green_wave=int(input())
free_wave=int(input())
queue=deque([])
cars_passed=0

is_crash=False

def crossing(cars):
    global cars_passed
    global is_crash
    remaining_green=green_wave
    remaining_free=free_wave
    for car in list(cars):
        length=len(car)
        if length<=remaining_green:
            remaining_green-=length
            cars_passed+=1
            cars.popleft()
        else:
            if remaining_green<=0:
                break
            elif length<=remaining_green+remaining_free:
                length-=remaining_green
                remaining_green=0
                remaining_free-=length
                cars_passed+=1
                cars.popleft()
                break
            else:
                remaining_free+=remaining_green
                is_crash=True
                break
    return cars,is_crash,remaining_free

while True:
    incomming=input()
    if incomming=="green":
        ret_cars,ret_bool,ret_position=crossing(queue)
        if ret_bool:
            print(f'A crash happened!')
            print(f'{queue[0]} was hit at {queue[0][ret_position]}.')
            break

    elif incomming=="END":
            print(f'Everyone is safe.')
            print(f'{cars_passed} total cars passed the crossroads.')
            break
    else:
        queue.append(incomming)
        

            

    

