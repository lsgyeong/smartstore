
# 배정이 완료되면 자동으로 가위바위보가 시작되고
# 한판 끝날때마다 연재와 의용이의 승리여부에
# 정해진 재일이나 성일이의 승률이 올라가는 것을 표시
# 10판 먼저 이긴쪽이 코드를 더 잘 짠다고 판정한다
# 가위바위보 승무패가 모두 존재한다
# 연속뽑기
# 한번씩 뽑기
from random import choice
from random import randint

players = ['연재','의용']
print(players)

teamJ = []
teamS = []
playerJ = choice(players)
print(playerJ)
teamJ.append(playerJ)
players.remove(playerJ)
print('남은 플레이어: ', players)

playerS = choice(players)
print(playerS)
teamS.append(playerS)
players.remove(playerS)
print('남은 플레이어: ', players)

print('재일 팀: ', teamJ)
print('성일 팀: ', teamS)



teamJwin = 0
teamSwin = 0
cnt = 0
while(teamJwin!=10 and teamSwin!=10):
    cnt = cnt + 1
    print('가위바위보 시작! %d번째 판!\n' % cnt)
    teamJ = randint(0, 2)  # 숫자 0은 가위, 1은 바위, 2는 보
    teamS = randint(0, 2)
    while(teamJ == teamS):
        print('비겼습니다!, 재경기 진행합니다')
        teamJ = randint(0, 2)  # 숫자 0은 가위, 1은 바위, 2는 보
        teamS = randint(0, 2)
    if(teamJ>teamS):
        if(teamJ==2 and teamS==0):
            print('성일팀 승리!\n')
            teamSwin+=1
        else:
            print('재일팀 승리!\n')
            teamJwin+=1

