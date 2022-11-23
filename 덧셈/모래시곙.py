blank = ' '
star = "*"

for i in range(0, 7):
    print(f'{blank*(i+1)}'f'{star*(14-(i*2+1))}', end="")
    print()
for i in range(0, 7):
    print(f'{blank*(7-i)}'f'{star*(i*2+1)}', end="")
    print()