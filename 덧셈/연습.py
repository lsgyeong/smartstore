import pprint

languages = ['python', 'perl', 'c', 'java']
for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
for a in [1, 2, 3]:
    print(a)

i=0
while i < 3:
    i = i+1
    print(i)
c=3
d=4
def add(c, d):
    return c + d
a = 123
print(float(a/10))
q=3
w=4
print(q**w)
e = 4.24E-10
print("%0.100f" %e)


print("10진수  2진수  8진수  16진수")
for i in range(1, 11):
    binary = bin(i) # 2진수 변환 함수
    octal = oct(i) # 8진수 변환 함수
    hexa = hex(i) # 16진수 변환 함수
    print(f'{i}       {binary}   {octal}   {hexa}')
