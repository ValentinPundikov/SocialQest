from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AuthWin(object):
    def setupUi(self, AuthWin):
        AuthWin.setObjectName("AuthWin")
        AuthWin.resize(397, 159)
        self.centralwidget = QtWidgets.QWidget(parent=AuthWin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 381, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 381, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 381, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        AuthWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthWin)
        QtCore.QMetaObject.connectSlotsByName(AuthWin)

    def retranslateUi(self, AuthWin):
        _translate = QtCore.QCoreApplication.translate
        AuthWin.setWindowTitle(_translate("AuthWin", "AuthWin"))
        self.pushButton.setText(_translate("AuthWin", "Записать на мероприятие"))
        self.pushButton_2.setText(_translate("AuthWin", "Просмотреть мероприятия"))
        self.pushButton_3.setText(_translate("AuthWin", "Выход"))
