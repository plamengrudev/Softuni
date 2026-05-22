count=int(input())
cars=set()

for _ in range(count):
    direction,number=[x for x in input().split(", ")]
    if direction=="IN":
        cars.add(number)
    elif direction=="OUT":
        cars.remove(number)

if cars:
    for car in cars:
        print(car)
else:
    print(f"Parking Lot is Empty")