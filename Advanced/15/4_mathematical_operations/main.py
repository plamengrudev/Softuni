from calculation import figure_out

line = [x for x in input().split()]

number1,sign,number2=float(line[0]),line[1],float(line[2])
result=figure_out(number1,number2,sign)
print(f"{result:.2f}")