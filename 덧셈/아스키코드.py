askii = list(map(int, input("아스키 코드를 입력 해주세요").split()))
aski = []
for i in range(len(askii)):
    aski.append(askii[i])
    print(f'{chr(aski[i])}', end=" ")