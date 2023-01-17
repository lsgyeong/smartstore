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

        self.tteokbokki1_produce_btn.clicked.connect(lambda :self.discount(0))
        self.tteokbokki2_produce_btn.clicked.connect(lambda :self.discount(1))
        self.pasta_produce_btn.clicked.connect(lambda: self.discount(2))
        self.soba_produce_btn.clicked.connect(lambda: self.discount(3))
        self.kimchi_produce_btn.clicked.connect(lambda: self.discount(4))
        self.softtofu_produce_btn.clicked.connect(lambda: self.discount(5))

    # 재고관리에서 제조버튼을 누르면 self.discount 매서드 실행
    def mealkit_discount(self,num):
        self.discount(k=num)

    # 각 밀키트별 콤보박스 수량 읽기 위한 메서드
    def combo_count(self,k):
        # 일반떡볶이
        if k == 0 :
            count=self.comboBox_4.currentText()
            return count
        # 로제떡볶이
        elif k == 1 :
            count=self.comboBox_3.currentText()
            return count
        # 봉골레파스타
        elif k == 2 :
            count=self.comboBox_5.currentText()
            return count
        # 야끼소바
        elif k == 3 :
            count=self.comboBox_6.currentText()
            return count
        # 김치찌개
        elif k == 4 :
            count=self.comboBox_7.currentText()
            return count
        # 순두부찌개
        elif k == 5 :
            count=self.comboBox_8.currentText()
            return count

    # 밀키트 제조시 재고수량 감소시키기 위한 매서드
    def discount(self,k):
        mealkit_name=['떡볶이','로제떡볶이','봉골레파스타','아끼소바','김치찌개','순두부찌개']
        count=self.combo_count(k)
        print(count)

        # 밀키트, 재료 DB 가져오기
        conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c=conn.cursor()
        c.execute(f'SELECT * FROM mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE where a.MEALKIT_NAME="{mealkit_name[k]}"')
        self.discount_db=c.fetchall()
        print(self.discount_db)

        # DB저장위해 변화된 재고량 리스트화
        inventory_list=[]
        for i in range(len(self.discount_db)):
            temp=int(self.discount_db[i][12])-(int(self.discount_db[i][6])*int(count))
            inventory_list.append(temp)

        # DB저장위해 recipe_code 리스트화
        code_list=[]
        for i in range(len(self.discount_db)):
            code_list.append(self.discount_db[i][5])

        # 변화된 재고량 DB에 저장하기
        for i in range(len(self.discount_db)):
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
            a=conn.cursor()
            a.execute(f'update mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE \
            set b.inventory={inventory_list[i]} where a.recipe_code="{code_list[i]}"')
            conn.commit()
            conn.close()

if __name__ == "__main__" :
    app = QApplication(sys.argv)      #QApplication : 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()          #WindowClass의 인스턴스 생성
    myWindow.show()                   #프로그램 화면을 보여주는 코드
    app.exec_()                       #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드