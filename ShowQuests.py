from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ShowQuests(object):
    def setupUi(self, ShowQuests):
        ShowQuests.setObjectName("ShowQuests")
        ShowQuests.resize(785, 238)
        self.centralwidget = QtWidgets.QWidget(parent=ShowQuests)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 771, 192))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 210, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 210, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        ShowQuests.setCentralWidget(self.centralwidget)

        self.retranslateUi(ShowQuests)
        QtCore.QMetaObject.connectSlotsByName(ShowQuests)

    def retranslateUi(self, ShowQuests):
        _translate = QtCore.QCoreApplication.translate
        ShowQuests.setWindowTitle(_translate("ShowQuests", "ShowQuests"))
        self.pushButton.setText(_translate("ShowQuests", "Удалить"))
        self.pushButton_2.setText(_translate("ShowQuests", "Закрыть"))
