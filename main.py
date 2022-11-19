#python -m PyQt5.uic.pyuic -x "order.ui" -o "Order_layout.py"
import random
import sys
from sqldatabase import MySqlDB

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QApplication, QCompleter, QComboBox, QMessageBox, QDialog

from Order_layout import Ui_MainWindow


class MainWindow:
    def __init__(self):
        # Initializing main app window
        self.main_win = QMainWindow()
        self.main_win.setFixedSize(1050, 800)

        # Initialising the MySql cursor
        self.sql = MySqlDB()
        self.cursor = self.sql.dbcursor

        # Adding ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)   # setting home_page as the first page

        # Connecting pages from home buttons
        self.ui.pushButton_2.clicked.connect(self.gottoinventory)    # from home to inventory
        self.ui.pushButton.clicked.connect(self.gotoorderspage)  # home to order
        self.ui.pushButton_4.clicked.connect(self.gotosupplier)     # from home to supplier

        # Inventory page connections
        self.ui.pushButton_12.clicked.connect(self.gotohomepage)  # from inventory to home
        self.ui.pushButton_9.clicked.connect(self.deleteInventory)  # delete button
        self.ui.pushButton_8.clicked.connect(self.insertInventory)  # add button in inventory page

        # Supplier page connections
        self.ui.pushButton_17.clicked.connect(self.gotohomepage)  # from supplier to home
        self.ui.pushButton_15.clicked.connect(self.gotosupplierlist)    # from supplier to supplier_list
        self.ui.pushButton_16.clicked.connect(self.gotosupplier_orders)    # from supplier to supplier_orders
        self.ui.pushButton_14.clicked.connect(self.gotosupplier)  # from supplier_list to supplier
        self.ui.pushButton_18.clicked.connect(self.gotosupplier)    # from supplier_orders to supplier

        # Supplier_list
        self.ui.pushButton_10.clicked.connect(self.insertSupplier_list)  # add button in supplier_list page
        self.ui.pushButton_11.clicked.connect(self.deleteSupplier_list)  # delete button in supplier_list page


        # Order page connections
        self.ui.pushButton_22.clicked.connect(self.gotohomepage)  # orders page to home page
        self.ui.pushButton_20.clicked.connect(self.gotonew_orderpage)   # orders page to new order page
        self.ui.pushButton_21.clicked.connect(self.gotomanage_orders)   # orders page to manage orders page


        self.ui.pushButton_19.clicked.connect(self.gotoorderspage)   # new order page to orders page
        self.ui.pushButton_23.clicked.connect(self.gotoorderspage)  # manage orders page to orders page


        # Connecting page back buttons






        # Connecting buttons to functions







    def gotohomepage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

    def gotoorderspage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.order)

    def gotonew_orderpage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.new_order)
        self.loadneworder_combobox()    # loads data into the combo box (product list)

    def gotomanage_orders(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.manage_orders)

    def gottoinventory(self):
        self.loadinventorytabledata()   # executes table after going to inventory page
        self.ui.stackedWidget.setCurrentWidget(self.ui.inventory)

    def gotosupplier(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.supplier)

    def gotosupplierlist(self):
        self.loadsupplier_listtabledata()
        self.ui.stackedWidget.setCurrentWidget(self.ui.supplier_list)

    def gotosupplier_orders(self):
        self.loadsupplier_ordersdata()
        self.ui.stackedWidget.setCurrentWidget(self.ui.supplier_orders)





    # Insert functions mostly for add buttons (data from text fields being used as input)
    def insertInventory(self):
        itemid = self.ui.lineEdit_5.text()
        name = self.ui.lineEdit_6.text()
        category = self.ui.lineEdit_7.text()
        quantity = self.ui.lineEdit_8.text()
        price = self.ui.lineEdit_9.text()

        self.cursor.execute("Insert into inventory values(%s,%s,%s,%s,%s)", (itemid, name, category, quantity, price))
        self.loadinventorytabledata()

    def insertSupplier_list(self):
        id = self.ui.lineEdit_10.text()
        name = self.ui.lineEdit_11.text()
        email = self.ui.lineEdit_12.text()
        phone = self.ui.lineEdit_13.text()

        self.cursor.execute("insert into supplier values(%s,%s,%s,%s)", (id, name, email, phone))
        self.loadsupplier_listtabledata()

    # De
    def deleteInventory(self):
        index = self.ui.tableWidget_3.currentRow()
        if index > -1:
            data = (self.ui.tableWidget_3.item(index, 0).text(),)

            self.cursor.execute('delete from inventory where Item_ID = %s', (str(data[0]),))

            self.loadinventorytabledata()   # After deleting loading data into table widget again

    def deleteSupplier_list(self):
        index = self.ui.tableWidget_4.currentRow()
        if index > -1:
            data = (self.ui.tableWidget_4.item(index, 0).text(),)

            self.cursor.execute('delete from supplier where Supplier_ID = %s', (str(data[0]),))

            self.loadsupplier_listtabledata()  # After deleting loading data into table widget again

    # Loading data into tables
    def loadinventorytabledata(self):
        self.cursor.execute("select * from inventory")

        a = self.cursor.fetchall()

        self.ui.tableWidget_3.setRowCount(len(a))
        self.ui.tableWidget_3.setColumnCount(5)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["Item ID", "Name", "Category", "Quantity", "Price"])

        row = 0

        for x in a:
            self.ui.tableWidget_3.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.ui.tableWidget_3.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.ui.tableWidget_3.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.ui.tableWidget_3.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
            self.ui.tableWidget_3.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[4])))
            row += 1
        #self.cursor.callproc("procedureaname", (aldkjf,lkdjaflk,jladjf))

    def loadsupplier_listtabledata(self):
        self.cursor.execute("select * from supplier")

        a = self.cursor.fetchall()

        self.ui.tableWidget_4.setRowCount(len(a))
        self.ui.tableWidget_4.setColumnCount(4)
        self.ui.tableWidget_4.setHorizontalHeaderLabels(["Supplier ID", "Name", "Email", "Phone Number"])

        row = 0

        for x in a:
            self.ui.tableWidget_4.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.ui.tableWidget_4.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.ui.tableWidget_4.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.ui.tableWidget_4.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
            row += 1

    def loadsupplier_ordersdata(self):
        self.cursor.execute("select * from supplier_orders")

        a = self.cursor.fetchall()

        self.ui.tableWidget_5.setRowCount(len(a))
        self.ui.tableWidget_5.setColumnCount(4)
        self.ui.tableWidget_5.setHorizontalHeaderLabels(["Supply ID", "Supplier ID", "Item ID", "Item Quantity"])

        row = 0

        for x in a:
            self.ui.tableWidget_5.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.ui.tableWidget_5.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.ui.tableWidget_5.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.ui.tableWidget_5.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
            row += 1

    def loadneworder_combobox(self):
        self.cursor.execute('select Item_Name from inventory')
        temp = []
        for x in self.cursor.fetchall():
            temp.append(str(x[0]))
        print(temp)

        self.ui.comboBox.addItems(temp)



########################################################

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        main_win = MainWindow()
        main_win.main_win.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)