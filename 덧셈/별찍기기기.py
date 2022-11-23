blank = ' '
star = "*"

for i in range(0, 5):
    print(f'{blank*(4-i)}'f'{star*(i*2+1)}', end="")
    print()
for i in range(0, 5):
    print(f'{blank*i}'f'{star*(10-(i*2+1))}', end="")
    print()
