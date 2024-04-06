import sqlite3
import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

from AuthWin import Ui_AuthWin
from CreateQuest import Ui_CreateQuest
from DelQuest import Ui_MainWindow
from ShowQuests import Ui_ShowQuests
from database import create_database, create_quest, delete_quest, get_familia




class AuthWin(QMainWindow, Ui_AuthWin):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.pushButton_2.clicked.connect(self.show_show_window)
        self.pushButton.clicked.connect(self.show_auth_create_window)
        self.pushButton_3.clicked.connect(self.close_this)


        self.auth_create_window = None
        self.auth_show_window = None

    def close_this(self):
        self.close()
    def show_auth_create_window(self):
        try:

            self.hide()


            if not self.auth_create_window:
                self.auth_create_window = CreateQuest(self)
            self.auth_create_window.show()
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_show_window(self):
        try:

            self.hide()


            if not self.auth_show_window:
                self.auth_show_window = ShowQuests(self)
            self.auth_show_window.show()
        except Exception as e:
            print(f"An error occurred: {e}")





class CreateQuest(QMainWindow, Ui_CreateQuest):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.pushButton_2.clicked.connect(self.close_and_show_main_auth)
        self.pushButton.clicked.connect(self.create_quest_new)

    def create_quest_new(self):
        try:
            typeq = self.comboBox.currentText()


            familia = self.lineEdit.text()
            name  = self.lineEdit_2.text()
            surname = self.lineEdit_3.text()
            dateq = self.dateEdit.text()
            create_quest(typeq,familia,name,surname,dateq)
            QMessageBox.information(self, "Успешно","Мероприятие создано")
        except Exception as e:
            print(f"An error occurred: {e}")

    def close_and_show_main_auth(self):
        try:

            self.close()

            # Show the MainAuth window
            self.main_window.show()
        except Exception as e:
            print(f"An error occurred: {e}")



class ShowQuests(QMainWindow, Ui_ShowQuests):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.pushButton_2.clicked.connect(self.close_and_show_main_auth)
        self.pushButton.clicked.connect(self.show_del_win)
        self.load_data()
        self.show_del_window = None
        self.show_auth_window = None



    def show_del_win(self):
        try:

            self.hide()


            if not self.show_del_window:
                self.show_del_window = DelQuests(self)
            self.show_del_window.show()
        except Exception as e:
            print(f"An error occurred: {e}")
    def load_data(self):
        try:

            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("data.db")


            if db.open():

                query = QSqlQuery("SELECT * FROM quests")
                self.model = QSqlQueryModel()
                self.model.setQuery(query)

                self.tableView.setModel(self.model)
            else:
                print("Ошибка при открытии базы данных")

        except Exception as e:
            print("Ошибка при выполнении SQL-запроса:", e)




    def close_and_show_main_auth(self):
        try:

            self.close()

            if not self.show_auth_window:
                self.show_auth_window = AuthWin(self)
            self.show_auth_window.show()
        except Exception as e:
            print(f"An error occurred: {e}")



class DelQuests(QMainWindow, Ui_MainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.pushButton.clicked.connect(self.delete_quest)

        self.fill_combobox()
        self.show_s_win = None

    def fill_combobox(self):
        try:

            familia_data = get_familia()


            self.comboBox.addItems(familia_data)

        except Exception as e:
            print("Ошибка при заполнении комбобокса:", e)

    def delete_quest(self):
        self.close()
        try:
            info = self.comboBox.currentText()
            delete_quest(info)
            QMessageBox.information(self, "Успешно","Успешно")
            self.close()
            self.main_window.show()

        except Exception as e:
            print(f"An error occurred: {e}")




if __name__ == "__main__":
    create_database()
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    window = AuthWin(main_window)
    window.show()
    sys.exit(app.exec())