import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
from PyQt5.QtCore import *
import time

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("main.ui")[0]

# 스레드 클래스
class Inventoryzero(QThread):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.power=True

    # 스레드 할 때 돌아가야하는 조건문
    def run(self):
        while self.power:
            # 밀키트, 재료 DB 가져오기
            conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
            c=conn.cursor()
            c.execute(f'select * from (select MEALKIT_NAME,convert(min(b.INVENTORY/a.RECIPE_GRAM), signed integer) as 최대개수 \
            from mealkit.recipe as a inner join `mealkit`.`jaelyo` as b on a.RECIPE_CODE = b.RECIPE_CODE \
            group by MEALKIT_NAME)t where 최대개수<2')
            alarm_db=c.fetchall()
            conn.commit()
            conn.close()
            # 로그인이 되어있고 제조가능개수가 1개 이하이면-> 로그인이 되어있는 경우를 조건문에 넣어야함.
            if bool(alarm_db) == True:
                for i in range(len(alarm_db)):
                    self.parent.lack_of_material_label_2.setText(f'{alarm_db[i][0]}\n재고부족')
                    time.sleep(1)
            else:
                self.parent.lack_of_material_label_2.setText(f'재고부족알림창')

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 스레드 돌리기
        self.inventoryzero=Inventoryzero(self)
        self.inventoryzero.start()

        self.stackedWidget.setCurrentIndex(5)

        # 떡볶이, 로제떡볶이, 봉골레파스타, 야끼소바, 김치찌개, 순두부찌개 버튼 눌렀을 때 이동
        self.tteokbokki1_produce_btn.clicked.connect(lambda :self.mealkit_discount(0))
        self.tteokbokki2_produce_btn.clicked.connect(lambda :self.mealkit_discount(1))
        self.pasta_produce_btn.clicked.connect(lambda: self.mealkit_discount(2))
        self.soba_produce_btn.clicked.connect(lambda: self.mealkit_discount(3))
        self.kimchi_produce_btn.clicked.connect(lambda: self.mealkit_discount(4))
        self.softtofu_produce_btn.clicked.connect(lambda: self.mealkit_discount(5))

        # 재고조회버튼 눌렀을 때
        self.material_check_btn.clicked.connect(self.inventory_search)

        # 밀키트 이름 리스트
        self.mealkit_name=['떡볶이','로제떡볶이','봉골레파스타','아끼소바','김치찌개','순두부찌개']

        self.order_discount()

    # 재고조회버튼 눌렀을 때
    def inventory_search(self):
        self.inventory_show() # 재고량 보여주기

    # 재고관리에서 제조버튼을 누르면 self.discount 매서드 실행
    def mealkit_discount(self,num):
        self.discount(k=num)

    # 밀키트 제조시 재고수량 감소시키기 위한 매서드
    def discount(self,k):
        combobox_list=[self.comboBox_4,self.comboBox_3,self.comboBox_5,self.comboBox_6,self.comboBox_7,self.comboBox_8]
        # 콤보박스의 갯수 불러오기
        count = combobox_list[k].currentText()

        # 밀키트, 재료 DB 가져오기
        conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c=conn.cursor()
        c.execute(f'SELECT * FROM mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE where a.MEALKIT_NAME="{self.mealkit_name[k]}"')
        self.discount_db=c.fetchall()

        c.execute(f'select * from (select MEALKIT_NAME,convert(min(b.INVENTORY/a.RECIPE_GRAM), signed integer) as 최대개수 \
        from mealkit.recipe as a inner join `mealkit`.`jaelyo` as b on a.RECIPE_CODE = b.RECIPE_CODE \
        group by MEALKIT_NAME)t where 최대개수<=0 and MEALKIT_NAME="{self.discount_db[0][0]}"')
        self.discount2_db=c.fetchall()
        conn.commit()
        conn.close()

        if bool(self.discount2_db) == True:
            QMessageBox.information(self, '알림', '제조불가\n재료확인요망')
        else:
            QMessageBox.information(self,'알림','제조완료')
            # 여기서 리스트화된 재고량 보고 최소수량이하면 알림띄우기

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

            # 변화된 재고량으로 보여주기
            self.inventory_show()

    # 밀키트별 제조가능 갯수 구하기
    def make_mealkit(self):
        # 밀키트, 재료 DB 가져오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c = conn.cursor()
        c.execute(f'SELECT * FROM mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE where a.MEALKIT_NAME="{self.mealkit_name[0]}"')
        self.make_db0 = c.fetchall()
        c.execute(f'SELECT * FROM mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE where a.MEALKIT_NAME="{self.mealkit_name[1]}"')
        self.make_db1 = c.fetchall()
        c.execute(f'SELECT * FROM mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE where a.MEALKIT_NAME="{self.mealkit_name[2]}"')
        self.make_db2 = c.fetchall()
        c.execute(f'SELECT * FROM mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE where a.MEALKIT_NAME="{self.mealkit_name[3]}"')
        self.make_db3 = c.fetchall()
        c.execute(f'SELECT * FROM mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE where a.MEALKIT_NAME="{self.mealkit_name[4]}"')
        self.make_db4 = c.fetchall()
        c.execute(f'SELECT * FROM mealkit.recipe as a left join `mealkit`.`jaelyo` as b on a.RECIPE_CODE=b.RECIPE_CODE where a.MEALKIT_NAME="{self.mealkit_name[5]}"')
        self.make_db5 = c.fetchall()
        conn.commit()
        conn.close()

        # 각 음식별 제조가능수량 구하기
        temp1=[] # 떡볶이
        temp2=[] # 로제떡볶이
        temp3=[] # 봉골레파스타
        temp4=[] # 아끼소바
        temp5=[] # 김치찌개
        temp6=[] # 순두부찌개
        for i in range(len(self.make_db0)):
            a=self.make_db0[i][12]/int(self.make_db0[i][6])
            temp1.append(int(a))
        result0 = min(temp1)
        for i in range(len(self.make_db1)):
            b = self.make_db1[i][12] / int(self.make_db1[i][6])
            temp2.append(int(b))
        result1 = min(temp2)
        for i in range(len(self.make_db2)):
            c = self.make_db2[i][12] / int(self.make_db2[i][6])
            temp3.append(int(c))
        result2 = min(temp3)
        for i in range(len(self.make_db3)):
            d = self.make_db3[i][12] / int(self.make_db3[i][6])
            temp4.append(int(d))
        result3 = min(temp4)
        for i in range(len(self.make_db4)):
            e = self.make_db4[i][12] / int(self.make_db4[i][6])
            temp5.append(int(e))
        result4 = min(temp5)
        for i in range(len(self.make_db5)):
            f = self.make_db5[i][12] / int(self.make_db5[i][6])
            temp6.append(int(f))
        result5 = min(temp6)

        # 제조가능수량 리스트화
        self.make_list=[result0,result1,result2,result3,result4,result5]

    # 밀키트: 제조가능개수 , 재료:재고량 보여주기
    def inventory_show(self):
        # DB 가져오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c = conn.cursor()
        c.execute(f'SELECT * FROM `mealkit`.`jaelyo` order by inventory')
        self.jaelyo_db = c.fetchall()
        conn.commit()
        conn.close()

        # 밀키트 제조가능수량 리스트 가져오기
        self.make_mealkit()

        # table 위젯 열, 행 셋팅
        header_list=['밀키트명','제조가능갯수','재료명','재고량(g)']
        self.current_matarial_tableWidget.setColumnCount(len(header_list))
        self.current_matarial_tableWidget.setRowCount(len(self.jaelyo_db))
        self.current_matarial_tableWidget.setHorizontalHeaderLabels(header_list)

        # 테이블 위젯의 헤더정렬
        self.current_matarial_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 각 셀에 값 넣기
        for i in range(len(self.mealkit_name)):
            self.current_matarial_tableWidget.setItem(i,0,QTableWidgetItem(str(self.mealkit_name[i])))   # 밀키트명
        for i in range(len(self.make_list)):
            self.current_matarial_tableWidget.setItem(i,1, QTableWidgetItem(str(self.make_list[i])))     # 제조가능갯수
        for i in range(len(self.jaelyo_db)):
            self.current_matarial_tableWidget.setItem(i,2,QTableWidgetItem(str(self.jaelyo_db[i][1])))   # 재료명
        for i in range(len(self.jaelyo_db)):
            self.current_matarial_tableWidget.setItem(i,3, QTableWidgetItem(str(self.jaelyo_db[i][4])))  # 재고량(g)

    # 주문내역 받아서 재고 감소시키는 매서드
    def order_discount(self):
        # DB 가져오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c = conn.cursor()
        c.execute(f'update `mealkit`.`recipe` as a inner join jaelyo as b inner join customer_order as c \
        set b.inventory=b.inventory-(a.recipe_gram*c.count), c.order_result="Y" where c.order_result="N"')
        conn.commit()
        conn.close()

if __name__ == "__main__" :
    app = QApplication(sys.argv)      #QApplication : 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()          #WindowClass의 인스턴스 생성
    myWindow.show()                   #프로그램 화면을 보여주는 코드
    app.exec_()                       #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드