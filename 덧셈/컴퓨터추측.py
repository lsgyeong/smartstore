import random
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