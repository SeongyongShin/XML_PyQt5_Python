import sys
import clipboard
from PyQt5.QtWidgets import *
import allFunc

import myFile


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createPushButtonGroup(), 0, 1)
        grid.addWidget(self.mainGroup(), 0, 2)
        self.setLayout(grid)
        self.setWindowTitle('By. sy')
        self.resize(1000, 700)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('입력 부분')
        self.le = QTextEdit()
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)
        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.clear_btn, 2)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        groupbox = QGroupBox('설정 부분')
        self.submitButton = QPushButton('제출')
        self.pasteSubmitButton = QPushButton('구현중')
        self.pasteSubmitButton.pressed.connect(self.pastSubmit)
        self.submitButton.pressed.connect(self.submit_pressed)
        self.listV = QListWidget(self)
        for i in myFile.itemList():
            item = QListWidgetItem()
            item.setText(i)
            self.listV.addItem(item)
        vbox = QVBoxLayout()
        vbox.addWidget(self.submitButton)
        vbox.addWidget(self.pasteSubmitButton)
        vbox.addWidget(self.listV)
        groupbox.setLayout(vbox)
        return groupbox

    def mainGroup(self):
        groupbox = QGroupBox('결과 부분')
        self.resultView = QLabel("여기에 결과가 표시됩니다.")
        self.htmlView = QTextBrowser()
        self.htmlView.setAcceptRichText(True)
        vbox = QVBoxLayout()
        vbox.addWidget(self.resultView)
        vbox.addWidget(self.htmlView)
        groupbox.setLayout(vbox)
        return groupbox



    def append_text(self):
        text = self.le.text()
        self.le.clear()

    def clear_text(self):
        self.le.setText("")

    def submit_pressed(self):
        self.resultView.setText("진행중")
        try:
            print(self.listV.currentItem().text())
            try:
                self.le.setText(allFunc.make_substring(self.le.toPlainText(), self.listV.currentItem().text()))
                print("asd")
                self.resultView.setText("정상")
            except:
                QMessageBox.about(self, "아님!", "정상 xml 이 아님 or 구현되지 않은 xslt 참조")
                self.resultView.setText("비정상")
                self.htmlView.setText("")
            try:
                f = open("xslt\\abc.html", "r", encoding='utf8')
                read = f.read()
                self.htmlView.setText(read)
                f.close()
            except:
                QMessageBox.about(self, "불가!", "xslt 파일이 정상인지 확인하세요")
                self.resultView.setText("문서 확인 불가")
                self.htmlView.setText("")
        except:
            self.resultView.setText("무언가 문제 발생")
            self.htmlView.setText("")

    def pastSubmit(self):
        try:
            self.le.setText(clipboard.paste())
            #self.submit_pressed()
            print(self.getmyStr(self))
        except:
            print("빈 클립보드")
    def getmyStr(self):
        return self.le.toPlainText()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
