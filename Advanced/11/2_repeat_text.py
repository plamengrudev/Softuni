error_msg="Variable times must be an integer"
try:
    text=input()
    times=int(input())
    print(text*times)
except ValueError:
    print(error_msg)

