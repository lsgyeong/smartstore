Instring = input('입력 : ')
Dic = {}
idx = 0
for ch in Instring:
    if ch not in Dic:
        Dic[ch] = []
    Dic[ch].append(idx)
    idx +=1
for ch in Dic:
    print(f'{ch}:count는{len(Dic[ch])}, index는 {Dic[ch]}')
