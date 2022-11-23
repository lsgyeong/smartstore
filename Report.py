studentScore = []

while True:
       choice = int(input('[1]시험점수입력 [2]성적확인 [3]종료 >>'))

       if choice ==3:
              break
       elif choice == 1:
              name = input('이름 입력 : ')
              kor = int(input('국어 점수 입력 : '))
              eng = int(input('영어 점수 입력 : '))
              mat = int(input('수학 점수 입력 : '))
              clang = int(input('C언어 점수 입력 : '))

              studentScore.append([name, kor, eng, mat, clang])
       elif choice ==2:
              print(' '*15,'성','   ','적','   ','표')
              print('-'*50)
              print('이름    ', '국어    ', '영어   ', '수학   ',  'C언어   ','평균   ')

              for s in studentScore:
                     avg = (s[1]+s[2]+s[3]+s[4])/4
                     print(f'{s[0]}\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}','  ' ,avg)