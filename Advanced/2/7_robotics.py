from collections import deque


robots=[x for x in input().split(";")]
starting_time=input()
queue=deque([])

hours,minutes,seconds=[int(x) for x in starting_time.split(":")]

start_sec=hours*3600+minutes*60+seconds
current_time=start_sec

robots_times={}

def print_times(secs):
    hours=secs//3600
    remaining=secs%3600
    minutes=remaining//60
    remaining=remaining%60
    seconds=remaining

    if hours>=24:
        hours%=24
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

for item in robots:
    args=[x for x in item.split("-")]
    robot, time=args[0],int(args[1])
    robots_times[robot]={"processing_time":time, "end_time":0}
    
while True:
    product=input()
    if product=="End":
        break
    else:
        queue.append(product)

counter=0
while len(queue)>=0:
    if len(queue)==0:
        break
    else:
        current_time+=1
        for item in robots_times.keys():
            if robots_times[item]['end_time']<=current_time:
                robots_times[item].update({"end_time":robots_times[item]["processing_time"]+current_time})
                print(f"{item} - {queue[0]} [{print_times(current_time)}]")
                queue.popleft()
                counter=0
                break
            else:
                counter+=1
        if counter==len(robots):
            queue.rotate(-1)


                
