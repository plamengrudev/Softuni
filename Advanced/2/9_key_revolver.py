from collections import deque

bullet_price=int(input())
gun_barrel=int(input())
bullets=[int(x) for x in input().split()]
locks=deque([int(x) for x in input().split()])
value_intel=int(input())
shots_fired=0
price_before_fire=bullet_price*len(bullets)

for bullet in reversed(bullets):
    if shots_fired==gun_barrel:
        print(f"Reloading!")
        shots_fired=0
    if locks:
        if bullet<=locks[0]:
            print(f"Bang!")
            bullets.pop()
            locks.popleft()
            shots_fired+=1
        elif bullet>locks[0]:
            print(f"Ping!")
            bullets.pop()
            shots_fired+=1

price_after_fire=bullet_price*len(bullets)
price_bullets=price_before_fire-price_after_fire
money_earned=value_intel-price_bullets

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


