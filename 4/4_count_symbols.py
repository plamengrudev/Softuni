text=input()
symbols=tuple(text)


for ch in sorted(set(symbols)):
    print(f"{ch}: {symbols.count(ch)} time/s")
