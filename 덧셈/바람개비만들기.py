a = '*'
b = ' '
c = int(input())
for i in range(0, c):
    print(f'{a*(i+1)}'f'{b*(c-i)}'f'{a*(c-i)}', end=" ")
    print()
for j in range(0, c):
    print(f'{b*(c-j)}'f'{a*(j+1)}'f'{b*(j+1)}'f'{a*(c-j)}', end= " ")
    print()