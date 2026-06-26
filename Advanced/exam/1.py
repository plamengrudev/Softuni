from collections import deque

qty_mech_parts=deque([int(x) for x in input().split()])
qty_energy_lvls=deque([int(x) for x in input().split()])

assembled_drones=[]
models={
    'Sentinel-X':100,
    'Viper-MKII':85,
    'Aegis-7':75,
    'Striker-R':65,
    'Titan-Core':55
}


def attempt_assembly(mech_part,energy_level):
    return int(mech_part+energy_level)


def find_drone(result_assembly):
    for model,power_needed in models.items():
        if power_needed==result_assembly and model not in assembled_drones:
            return model,True

    for model,power_needed in models.items():
        if power_needed<result_assembly and model not in assembled_drones:
            return model,False

    return None,None

while True:
    if len(assembled_drones)==5:
        break
    elif len(qty_mech_parts)<=0 or len(qty_energy_lvls)<=0:
        break
    else:
        while qty_energy_lvls and qty_energy_lvls[0]<=0:
            qty_energy_lvls.popleft()
        if len(qty_energy_lvls)<=0:
            break
        result_assembly=attempt_assembly(qty_mech_parts[-1],qty_energy_lvls[0])
        model,exact_match=find_drone(result_assembly)

        if model and exact_match:
            assembled_drones.append(model)
            qty_mech_parts.pop()
            qty_energy_lvls.popleft()
        elif model:
            qty_mech_parts.pop()
            assembled_drones.append(model)
            qty_energy_lvls[0]-=30
            if qty_energy_lvls[0]<=0:
                qty_energy_lvls.popleft()
            else:
                qty_energy_lvls.rotate(-1)
        else:
            qty_mech_parts.pop()
            qty_energy_lvls[0]-=1
            if qty_energy_lvls[0]<=0:
                qty_energy_lvls.popleft()
            else:
                qty_energy_lvls.rotate(-1)

if len(assembled_drones)==5:
    print('Mission Accomplished! All Guardian Drones activated!')
else:
    print('Mission Failed! Some drones were not built.')

if assembled_drones:
    print(f"Assembled Drones: {', '.join(assembled_drones)}")

if qty_mech_parts:
    print(f"Mechanical Parts: {', '.join(map(str,reversed(qty_mech_parts)))}")

if qty_energy_lvls:
    print(f"Power Cells: {', '.join(map(str,qty_energy_lvls))}")
