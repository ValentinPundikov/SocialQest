from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateQuest(object):
    def setupUi(self, CreateQuest):
        CreateQuest.setObjectName("CreateQuest")
        CreateQuest.resize(503, 213)
        self.centralwidget = QtWidgets.QWidget(parent=CreateQuest)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 180, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.formLayoutWidget)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 31), QtCore.QTime(22, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        CreateQuest.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateQuest)
        QtCore.QMetaObject.connectSlotsByName(CreateQuest)

    def retranslateUi(self, CreateQuest):
        _translate = QtCore.QCoreApplication.translate
        CreateQuest.setWindowTitle(_translate("CreateQuest", "CreateQuest"))
        self.pushButton.setText(_translate("CreateQuest", "Создать"))
        self.pushButton_2.setText(_translate("CreateQuest", "Отмена"))
        self.label.setText(_translate("CreateQuest", "Тип квеста"))
        self.comboBox.setItemText(0, _translate("CreateQuest", "Хоррор"))
        self.comboBox.setItemText(1, _translate("CreateQuest", "Юмор"))
        self.comboBox.setItemText(2, _translate("CreateQuest", "Приключение"))
        self.label_2.setText(_translate("CreateQuest", "Фамилия"))
        self.label_5.setText(_translate("CreateQuest", "Дата"))
        self.label_3.setText(_translate("CreateQuest", "Имя"))
        self.label_4.setText(_translate("CreateQuest", "Отчество"))
