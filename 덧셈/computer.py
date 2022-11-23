import random
# 추측게임을 구현하는 방법
# 컴퓨터에는 비밀 번호가 있습니다.
# 그리고 우리는 그 비밀 번호를 추측하려고 노력하고 있습니다.
# 1. 실제로 우리가 추측할 수 있도록 컴퓨터가 비밀번호를 생성하게 하는 것
# 2. 컴퓨터에 임의의 숫자가 있으면 정확하게 추측해야 하며 터미널에서 추측해야 한다.
# 3. 추측한 숫자를 입력하면 컴퓨터가 숫자가 너무 높은지 여부를 알려줍니다.
# 4. 너무 낮은, 또는 숫자를 올바르게 추측 했다면 다음까지 반복해야 한다.
# 5. 반복할 사전 정의된 유니버스가 없다면 , while 루프를 사용할 것이다.
# 6. 숫자는 난수와 같다.
# 7. 추측이 임의의 숫자와 같지 않은 경우 몇 가지를 반복하려고 한다.
# 8. 변수를 초기화하려면 이 변수가 존재한다고 python에 알립니다.

def guess(x):   # x를 매개 변수로 만들어 이 임의의 숫자 가져오기 함수에 전달할 수 있도록 하겠습니다.
    random_number = random.randint(1, x)
    guess = 0 # 임의의 숫자 rand int 1과 x 사이 그리고 그것은 결코 0이 되지 않을 것이라는 것을 의미한다.
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrates. You have guessed the number. {random_number} correctly!!!')
guess(20)  # 함수 호출

# 반대로 컴퓨터가 추측하려고 한다.
# 컴퓨터 손님이라는 새 기능
# 비밀 번호가 있는데, 어떤 비밀 번호가 맞는지 컴퓨터에 알리지 않겠다.
# 이는 기본적으로 컴퓨터가 최소값과 최대값으로 작업 할 수 있는
# 숫자의 범위를 가지고 있음을 의미한다.
# 낮고 높음. 즉, 초기에 낮은 값과 높은 값을 설정하자는 의미
# 이것은 어떤 것도 반복할 필요가 없다.
# 사용자가 피드백을 제공할 수 있을 때까지
# 컴퓨터에 피드백이 너무 많은지 알려줄 수 있어야 합니다.
# 높거나 너무 낮거나 정확하게 추측한 경우 피드백을 초기화하겠습니다.
# guest를 0으로 초기화하는 것과 마찬가지로
# 빈 문자열로 초기화 해 보겠습니다.
# 컴퓨터가 해야 할 첫 번째 일은 새 번호를 받는 것입니다.
# 그래서 추측을 할 것이다.

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f'Yay ! The computer guessed your number, {guess}, correctly! ')
computer_guess(1000)