import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(5)

        self.tteokbokki1_produce_btn(self.tteokbokki1_discount)

    def tteokbokki1_discount(self):
        conn=pymysql.conncet(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c=conn.cursor()
        c.execute(f'select * from `mealkit`.`recipe`')



if __name__ == "__main__" :
    app = QApplication(sys.argv)      #QApplication : 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()          #WindowClass의 인스턴스 생성
    myWindow.show()                   #프로그램 화면을 보여주는 코드
    app.exec_()                       #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드