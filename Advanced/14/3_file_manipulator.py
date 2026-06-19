import os
line=input()
while line!="End":
    args=[x for x in line.split('-')]
    command=args[0]
    if command=="Create":
        file_name=args[1]
        with open(file_name,'w') as file:
            pass
    elif command=="Add":
        file_name, content=args[1],args[2]
        with open(file_name,'a') as file:
            file.write(content)
            file.write('\n')
    elif command=="Replace":
        file_name, old_string, new_string=args[1], args[2],args[3]
        with open(file_name,'r+') as file:
            read_line=file.read().replace(old_string,new_string)
            file.write(read_line)
    elif command=="Delete":
        file_name=args[1]
        try:
            os.remove(file_name)
        except FileNotFoundError:
            pass
    line=input()
