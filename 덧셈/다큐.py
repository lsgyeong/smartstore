print("아침 7시, 알람소리를 듣고 일어났다.")
print("원래는 8시에 일어났지만, 1시간일찍 알람맞추기 방법으로 매일 7시에 일어나게 되었다")
print("원래 일어난 시간을 입력하면 당신의 하루일과 게임이 시작됩니다.")
h, m = map(int, input("원래일어난 시간을 입력해주세요 : ").split())
m -= 60
if m < 0:
    h -= 1
    m += 60
    if h < 0:
        h = 23
print("일어난 시간:%d, 몇분:%d" %(h, m))
class human():
    def __init__(self):
        self.name =""
        self.hp = 0
        self.exp = 0
        self.lv = 1

    def 밥먹기(self):
        print(self.name,'이(가) 밥을 먹는다. 체력을 회복합니다.')
    def 잠자기(self):
        print(self.name,'이(가) 잠을 잔다. 체력을 회복합니다.')
    def 운동하기(self):
        print(self.name,'이(가) 운동한다. 체력이 감소하고, 경험치가 오릅니다.')
    def 파이썬공부하기(self):
        print(self.name,'이(가) 파이썬을 공부한다. 체력이 감소하고 경험치가 오릅니다.')
    def 레벨체크(self):
        print(self.name,'레벨체크')
    def 상태정보(self):
        print(self.name,'상태정보출력')
        print('HP:', self.hp)
        print('EXP:', self.exp)
        print('LV:', self.lv)

class 박의용(human):
    def __init__(self):
        super().__init__()
        self.name = '박의용'
        self.hp = 100

    def 밥먹기(self):
        super().밥먹기()
        self.hp += 33

    def 잠자기(self):
        super().잠자기()
        self.hp += 42

    def 운동하기(self):
        super().운동하기()
        self.hp -= 33
        start = self.hp>0
        if start:
            self.exp += 10
            self.레벨체크()
        return start
    def 파이썬공부하기(self):
        super().파이썬공부하기()
        self.hp -= 38
        start = self.hp>0
        if start:
            self.exp += 50
            self.레벨체크()
        return start
    def 레벨체크(self):
        if self.exp>=10:
            self.lv += 1
            print(self.name, '레벨업!')
            self. exp -=10
    def 음유시인(self):
        print("방랑자의 부름, 우주의 결속,수호자의 성소 내딛는 곳은 어디든 나의 세상 음. 인생은 짧은 여행이라네")

class 이현도(human):
    def __init__(self):
        super().__init__()
        self.name = '이현도'
        self.hp = 200

    def 밥먹기(self):
        super().밥먹기()
        self.hp += 10

    def 잠자기(self):
        super().잠자기()
        self.hp += 15

    def 운동하기(self):
        super().운동하기()
        self.hp -= 80
        start = self.hp>0
        if start:
            self.exp += 40
            self.레벨체크()
        return start
    def 파이썬공부하기(self):
        super().파이썬공부하기()
        self.hp -= 10
        start = self.hp>0
        if start:
            self.exp += 10
            self.레벨체크()
        return start
    def 레벨체크(self):
        if self.exp>=10:
            self.lv += 1
            print(self.name, '레벨업!')
            self. exp -=10
    def 중국권법(self):
        print("자네 무술을 아시는가? 태극권법의 창시자 내 주먹을 받으면 자넨 사망에 이를것이네 살려면 도망가시게")

class 고연재(human):
    def __init__(self):
        super().__init__()
        self.name = '고연재'
        self.hp = 250

    def 밥먹기(self):
        super().밥먹기()
        self.hp += 30

    def 잠자기(self):
        super().잠자기()
        self.hp += 25

    def 운동하기(self):
        super().운동하기()
        self.hp -= 60
        start = self.hp > 0
        if start:
            self.exp += 40
            self.레벨체크()
        return start
    def 파이썬공부하기(self):
        super().파이썬공부하기()
        self.hp -= 80
        start = self.hp > 0
        if start:
            self.exp += 30
            self.레벨체크()
        return start
    def 레벨체크(self):
        if self.exp>=10:
            self.lv += 1
            print(self.name, '레벨업!')
            self. exp -=10
    def 우사인볼트(self) :
        print("난 이세계 최고 바로 우사인볼트. 난 키가 크기 때문에 스타트 속도는 느리지만 중간지점부터는 끝까지 간다")

class Menu:
    def __init__(self, humanchoice):
        self.humanchoice = humanchoice

    def run(self):
        start = True
        while start:
            menu = int(input('1.밥먹기 2.잠자기 3.운동하기 4.파이썬공부하기 5.상태확인 6.특성발현 7.종료'))
            if menu == 1:
                self.humanchoice.밥먹기()
            elif menu == 2:
                self.humanchoice.잠자기()
            elif menu == 3:
                self.humanchoice.운동하기()
            elif menu == 4:
                self.humanchoice.파이썬공부하기()
            elif menu == 5:
                self.humanchoice.상태정보()
            elif menu == 6:
                if isinstance(self.humanchoice, 박의용):
                    self.humanchoice.음유시인()
                elif isinstance(self.humanchoice, 이현도):
                    self.humanchoice.중국권법()
                elif isinstance(self.humanchoice, 고연재):
                    self.humanchoice.우사인볼트()
            elif menu == 7:
                start = False
        print('하루 일과 종료')
        print('사실 요새 하루일과가...')
        print('일어나서 밥먹고 수업듣고, 다시 밥먹고...')
        print('공부하고...자고..의 반복이라')
        print('약간 재미있게 할 수 없을까 하여..')
        print('혼자서 만들지는 못했지만')
        print('나중에 더 학습하여 더 재밌는 게임을 만들고 싶습니다.')

def main():
    print('하루 일과 게임 시작')
    human = input('사람 선택\n1.박의용(기본)2.이현도 3.고연재')
    humanchoice = None
    if human == '1':
        humanchoice = 박의용()
    if human == '2':
        humanchoice = 이현도()
    if human == '3':
        humanchoice = 고연재()

    humanchoice.상태정보()
    click = Menu(humanchoice)
    click.run()
main()