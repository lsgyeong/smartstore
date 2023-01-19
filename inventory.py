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
            if bool(alarm_db) == True:
                for i in range(len(alarm_db)):
                    self.parent.lack_of_material_label_2.setText(f'{alarm_db[i][0]}\n재고부족')
                    time.sleep(2)
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
        # 주문내역제조 버튼 눌렀을 떄
        self.jumun_btn.clicked.connect(self.order_discount_go)
        # 재고조회버튼 눌렀을 때
        self.material_check_btn.clicked.connect(self.inventory_search)
        # 재고일괄발주 눌렀을 때
        self.material_check_btn_2.clicked.connect(self.balju)
        # 밀키트 재고량 보이기
        self.make_mealkit()

        self.stackedWidget.setCurrentIndex(5)

    # 재고일괄발주 눌렀을 때
    def balju(self):
        # 재고량 DB 재고량 10000으로 일괄적용
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        a = conn.cursor()
        a.execute(f'update `mealkit`.`jaelyo` set inventory=10000')
        conn.commit()
        conn.close()
        # 변화된 재고량으로 보여주기
        self.inventory_show()
        self.make_mealkit()

    # 재고조회버튼 눌렀을 때
    def inventory_search(self):
        self.inventory_show() # 재고량 보여주기
        self.make_mealkit() # 밀키스 수량 보여주기

    # 밀키트별 제조가능 갯수 구하기
    def make_mealkit(self):
        # 밀키트, 재료 DB로 밀키트별 제조가능갯수 가져오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c = conn.cursor()
        c.execute(f'select a.MEALKIT_NAME,convert(min(b.INVENTORY/a.RECIPE_GRAM), signed integer) as 최소갯수 from recipe as a inner join jaelyo as b \
        on a.RECIPE_code=b.RECIPE_CODE group by mealkit_name order by a.mealkit_name')
        make_list = c.fetchall()
        conn.commit()
        conn.close()
        # 라벨에 셋팅
        self.kimchi_inven.setText(f'{make_list[0][1]}')
        self.bboki_inven.setText(f'{make_list[1][1]}')
        self.rose_inven.setText(f'{make_list[2][1]}')
        self.pasta_inven.setText(f'{make_list[3][1]}')
        self.sundubu_inven.setText(f'{make_list[4][1]}')
        self.yaki_inven.setText(f'{make_list[5][1]}')

    # 재료:재고량 보여주기
    def inventory_show(self):
        # DB 가져오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c = conn.cursor()
        c.execute(f'SELECT * FROM `mealkit`.`jaelyo` order by inventory')
        self.jaelyo_db = c.fetchall()
        conn.commit()
        conn.close()

        # table 위젯 열, 행 셋팅
        header_list=['재료명','재고량(g)']
        self.current_matarial_tableWidget.setColumnCount(len(header_list))
        self.current_matarial_tableWidget.setRowCount(len(self.jaelyo_db))
        self.current_matarial_tableWidget.setHorizontalHeaderLabels(header_list)

        # 테이블 위젯의 헤더정렬
        self.current_matarial_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 각 셀에 값 넣기
        for i in range(len(self.jaelyo_db)):
            self.current_matarial_tableWidget.setItem(i,0,QTableWidgetItem(str(self.jaelyo_db[i][1])))   # 재료명
        for i in range(len(self.jaelyo_db)):
            self.current_matarial_tableWidget.setItem(i,1, QTableWidgetItem(str(self.jaelyo_db[i][4])))  # 재고량(g)

    # 제조 안한 주문을 전체 가져와서 order_discount 매서드를 활용해서 전체 바꿔주기
    def order_discount_go(self):
        # order_result='N'인 항목 전체 가져오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c = conn.cursor()
        c.execute(f'SELECT * FROM mealkit.customer_order where order_result="N"')
        standard_db=c.fetchall()
        # 제조할 주문이 없을 경우
        if bool(standard_db) == False:
            QMessageBox.information(self, '알림', '주문이 없습니다')
        # 제조할 주문이 있는 경우
        else:
            # 반복문과 매서드를 활용하여 아직 제조 안한 주문을 하나씩 처리함.
            for i in range(len(standard_db)):
                self.order_discount()       # order_result='N'인 한 개의 주문을 가져와서 재고량 감소시키는 메서드
        conn.commit()
        conn.close()
        self.make_mealkit()                 # 밀키트 재고량 보여주는 매서드

    # order_result='N'인 한 개의 주문을 가져와서 재고량 감소시키는 메서드
    def order_discount(self):
        # order_result='N'인 한개의 주문 가져옴
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c = conn.cursor()
        c.execute(f'SELECT * FROM mealkit.customer_order where order_result="N" limit 1')
        self.count_db = c.fetchall()

        # 주문한 만큼의 재고가 충분히 있는지 확인을 위한 쿼리문
        c.execute(f'select * from (select MEALKIT_NAME,convert(min(b.INVENTORY/a.RECIPE_GRAM), signed integer) as 최대개수 \
        from mealkit.recipe as a inner join `mealkit`.`jaelyo` as b on a.RECIPE_CODE = b.RECIPE_CODE \
        group by MEALKIT_NAME)t where MEALKIT_NAME="{self.count_db[0][3]}" and 최대개수<{self.count_db[0][4]}')
        alarm_db = c.fetchall()

        # 최대개수가 주문량보다 부족한 제품이 있을 때
        if bool(alarm_db) == True:
            if bool(alarm_db) == True and self.count_db[0][3]==alarm_db[0][0]:
                QMessageBox.information(self, '알림', f'{self.count_db[0][3]}재고 부족, 재료 일괄 발주')
                self.balju()
                QMessageBox.information(self, '알림', f'발주완료, 밀키트 생산')
            else:
                self.order_repeat()
        else:
            self.order_repeat()
        conn.commit()
        conn.close()

    # 주문시 반복해서 쓰이는 메서드
    def order_repeat(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='mealkit')
        c = conn.cursor()

        # 가져온 주문의 재고량과 1번 제조시 들어가는 재료량 가져오기
        c.execute(f'SELECT a.MEALKIT_NAME,b.RECIPE_NAME,a.recipe_gram,b.inventory FROM recipe as a \
                                    inner join mealkit.jaelyo as b on a.RECIPE_CODE=b.RECIPE_CODE where a.mealkit_name="{self.count_db[0][3]}"')
        inventory_db = c.fetchall()

        # 주문 음식의 재고량 변화, order_result="Y"로 변경
        for i in range(len(inventory_db)):
            c.execute(
                f'update mealkit.jaelyo set inventory={inventory_db[i][3] - int(inventory_db[i][2]) * int(self.count_db[0][4])} where recipe_name="{inventory_db[i][1]}"')
        c.execute(f'update customer_order set order_result="Y" where idcustomer_order="{self.count_db[0][0]}"')
        QMessageBox.information(self, '알림', f'{self.count_db[0][0]}번, {self.count_db[0][3]}주문이 정상적으로 처리되었습니다')
        conn.commit()
        conn.close()
        self.make_mealkit()
        self.inventory_show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)      #QApplication : 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()          #WindowClass의 인스턴스 생성
    myWindow.show()                   #프로그램 화면을 보여주는 코드
    app.exec_()                       #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드