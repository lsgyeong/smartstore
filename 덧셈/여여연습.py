from pprint import pprint
list = [[1, "강민영"],
        [2, "고연재"],
        [3, "김기태"],
        [4, "김명은"],
        [5, "김성일"],
        [6, "김연수"],
        [7, "김재일"],
        [8, "노도현"],
        [9, "류가미"],
        [10, "박규환"],
        [11, "박성빈"],
        [12, "박시형"],
        [13, "박의용"],
        [14, "오송화"],
        [15, "이범규"],
        [16, "이보라"],
        [17, "이소윤"],
        [18, "이여름"],
        [19, "이지혜"],
        [20, "이현도"],
        [21, "임성경"],
        [22, "임영효"],
        [23, "임홍선"],
        [24, "장은희"],
        [25, "정연우"],
        [26, "정철우"],
        [27, "주민석"],
        [28, "최지혁"],
        ]
pprint(list, indent=4, width=20)

for num, name in list: # 리스트 가로 한 줄(안쪽 리스트)에서 요소 두 개를 꺼냄
    print(num, name)
print()

for num in list:  # 리스트에서 안쪽 리스트를 꺼냄
    for name in num: # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(name, end=' ')
    print()
print()

for num in range(len(list)):  # 세로 크기
    for name in range(len(list[num])): # 가로 크기 list[i] [값, 값]의 len은 2
        print(list[num][name], end=' ')
    print()
print()

i = 0
while i < len(list): # 반복할 때 리스트의 크기 활용 (세로 크기)
    num, name = list[i] # 요소 두 개를 한꺼번에 가져오기
    print(num, name)
    i += 1 # 인덱스를 1 증가 시킴.
print()

i = 0
while i < len(list):      # 세로 크기
    j = 0
    while j < len(list[i]): # 가로 크기
        print(list[i][j], end=' ')
        j += 1 # 가로 인덱스를 1 증가 시킴.
    print()
    i += 1 # 세로 인덱스를 1 증가 시킴.

list_make = []   # 빈 리스트 생성

for i in range(3):
    line = [] # 안 쪽 리스트로 사용할 빈 리스트 생성
    for j in range(1):
        line.append((input("번호를 입력 해주세요")))
        line.append((input("이름을 입력 해주세요")))# 안 쪽 리스트에 0 추가
    list_make.append(line) # 전체 리스트에 안 쪽 리스트를 추가
    pprint(list_make, indent=4, width=20)

pprint(list_make, indent=4, width=20)

list_two = [[0 for j in range(2)] for i in range(3)] # 바깥 for문을 뒤에
print(list_two)

