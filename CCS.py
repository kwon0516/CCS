import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("CCS_main.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1300, 850)
        
        self.pushButton_main_page.clicked.connect(lambda: self.ChangePage(0))
        self.pushButton_add_customer.clicked.connect(lambda: self.ChangePage(1))
        self.pushButton_search_customer.clicked.connect(lambda: self.ChangePage(2))
        self.pushButton_option.clicked.connect(lambda: self.ChangePage(3))
        self.pushButton_exit.clicked.connect(self.ClickedExit)
        
        self.pushButton_add_save.clicked.connect(lambda: self.EditCheck("Add"))
        self.pushButton_add_clear.clicked.connect(lambda: self.EditClear("Add"))
        
        self.pushButton_search_db.clicked.connect(lambda: self.EditCheck("Search"))
        self.pushButton_search_clear.clicked.connect(lambda: self.EditClear("Search"))
    
    def EditCheck(self, separator):
        if separator == "Add":
            if self.lineEdit_add_name.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","이름이 비어있습니다.")
                return
            elif self.lineEdit_add_birthday.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","생년월일이 비어있습니다.")
                return
            elif self.lineEdit_add_phone_number.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","번호가 비어있습니다.")
                return
            elif self.lineEdit_add_agency.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","통신사가 비어있습니다.")
                return
            elif self.lineEdit_add_date.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","개통일이 비어있습니다.")
                return
            elif self.lineEdit_add_agreement.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","약정개월 비어있습니다.")
                return
            elif self.lineEdit_add_condition.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","공시/선약이 비어있습니다.")
                return
            elif self.lineEdit_add_phone_type.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","기종이 비어있습니다.")
                return
            
            print("여기부터 DB저장 작성")
        else:
            if self.lineEdit_search_name.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","이름이 비어있습니다.")
                return
            elif self.lineEdit_search_birthday.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","생년월일이 비어있습니다.")
                return
            elif self.lineEdit_search_phone_number.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","번호가 비어있습니다.")
                return
            elif self.lineEdit_search_agency.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","통신사가 비어있습니다.")
                return
            elif self.lineEdit_search_date.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","개통일이 비어있습니다.")
                return
            elif self.lineEdit_search_agreement.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","약정개월 비어있습니다.")
                return
            elif self.lineEdit_search_condition.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","공시/선약이 비어있습니다.")
                return
            elif self.lineEdit_search_phone_type.text().replace(" ","") == "":
                QMessageBox.warning(self,"Warning","기종이 비어있습니다.")
                return
            
            print("여기부터 DB조회 작성")
            
            
    
    def EditClear(self, separator):
        if separator == "Add":
            self.lineEdit_add_name.clear()
            self.lineEdit_add_birthday.clear()
            self.lineEdit_add_phone_number.clear()
            self.lineEdit_add_agency.clear()
            self.lineEdit_add_date.clear()
            self.lineEdit_add_agreement.clear()
            self.lineEdit_add_condition.clear()
            self.lineEdit_add_phone_type.clear()
            self.textEdit_uniqueness.clear()
        else:
            self.lineEdit_search_name.clear()
            self.lineEdit_search_birthday.clear()
            self.lineEdit_search_phone_number.clear()
            self.lineEdit_search_agency.clear()
            self.lineEdit_search_date.clear()
            self.lineEdit_search_agreement.clear()
            self.lineEdit_search_condition.clear()
            self.lineEdit_search_phone_type.clear()
            
        
    
    def ChangePage(self, page_index):
        self.stackedWidget.setCurrentIndex(page_index)
        
    def ClickedExit(self):
        confirm_exit = QMessageBox.question(self, "종료", "정말 종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No)

        if confirm_exit == QMessageBox.Yes:
            self.Exit()
    
    
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)

    CCS = WindowClass()

    CCS.show()

    app.exec_()