#python -m PyQt5.uic.pyuic -x "order.ui" -o "Order_layout.py"
import sys
from sqldatabase import MySqlDB

from PyQt5 import QtWidgets

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

        # Supplier_list connections
        self.ui.pushButton_10.clicked.connect(self.insertSupplier_list)  # add button in supplier_list page
        self.ui.pushButton_11.clicked.connect(self.deleteSupplier_list)  # delete button in supplier_list page

        # Supplier_Orders connections
        self.ui.pushButton_13.clicked.connect(self.deleteSupplier_Orders)

        # Order page connections
        self.ui.pushButton_22.clicked.connect(self.gotohomepage)  # orders page to home page
        self.ui.pushButton_20.clicked.connect(self.gotonew_orderpage)   # orders page to new order page
        self.ui.pushButton_21.clicked.connect(self.gotomanage_orders)   # orders page to manage orders page

        # Manage order page connections
        self.ui.pushButton_23.clicked.connect(self.gotoorderspage)  # manage orders page to orders page
        self.ui.pushButton_6.clicked.connect(self.deleteOrders)   # delete orders
        self.ui.pushButton_24.clicked.connect(self.loadmanage_orders_items_data)    # display order contents

        # New Order page connections
        self.ui.pushButton_19.clicked.connect(self.gotoorderspage)  # new order page to orders page
        self.ui.pushButton_3.clicked.connect(self.insertNew_order_details)

        self.ui.comboBox.activated.connect(self.display_item_details)   # displays price after item is selected from combobox
        self.ui.pushButton_5.clicked.connect(self.insertNew_order_details_items)








        # Connecting buttons to functions







    def gotohomepage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

    def gotoorderspage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.order)

    def gotonew_orderpage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.new_order)
        self.loadneworder_combobox()    # loads data into the combo box (product list)
        self.display_item_details()     # Loads price data into the label


    def gotomanage_orders(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.manage_orders)
        self.loadmanage_ordersdata()    # loads data into the combo box (product list)


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

    def deleteSupplier_Orders(self):
        index = self.ui.tableWidget_5.currentRow()
        if index > -1:
            data = (self.ui.tableWidget_5.item(index, 0).text(),)

            self.cursor.execute('delete from supplier_orders where Supply_ID = %s', (str(data[0]),))

            self.loadsupplier_ordersdata()  # After deleting loading data into table widget again

    def deleteOrders(self):
        index = self.ui.tableWidget_2.currentRow()
        if index > -1:
            data = (self.ui.tableWidget_2.item(index, 0).text(),)

            self.cursor.execute('delete from orders where Order_ID = %s', (str(data[0]),))

            self.loadmanage_ordersdata()

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

    def loadmanage_ordersdata(self):
        self.cursor.execute("select * from orders")

        a = self.cursor.fetchall()

        self.ui.tableWidget_2.setRowCount(len(a))
        self.ui.tableWidget_2.setColumnCount(5)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["Order ID", "Pincode", "Payment Amount", "Contact Number", "Email"])

        row = 0

        for x in a:
            self.ui.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.ui.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.ui.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.ui.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
            self.ui.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[4])))
            row += 1

    def loadmanage_orders_items_data(self):
        index = self.ui.tableWidget_2.currentRow()
        if index > -1:
            data = (self.ui.tableWidget_2.item(index, 0).text(),)

            self.cursor.execute('select Item_ID, Quantity, Order_Price from order_list where Order_ID = %s', (str(data[0]),))

        a = self.cursor.fetchall()

        self.ui.tableWidget_6.setRowCount(len(a))
        self.ui.tableWidget_6.setColumnCount(3)
        self.ui.tableWidget_6.setHorizontalHeaderLabels(["Item ID", "Quantity", "Price"])

        row = 0

        for x in a:
            self.ui.tableWidget_6.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.ui.tableWidget_6.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.ui.tableWidget_6.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))

            row += 1

    def loadneworder_combobox(self):
        self.cursor.execute('select Item_Name from inventory')
        temp = []
        for x in self.cursor.fetchall():
            temp.append(str(x[0]))


        self.ui.comboBox.addItems(temp)




    # New Order Page
    def insertNew_order_details(self):      # confirm details button
        order_id = self.ui.lineEdit.text()
        contact = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()
        pincode = self.ui.lineEdit_4.text()

        self.cursor.execute("insert into orders values(%s,%s,%s,%s,%s)", (order_id, contact, 0, email, pincode))


    def display_item_details(self):

        itemid = self.ui.comboBox.currentText()
        self.cursor.execute('select Price from inventory where Item_Name = %s', (str(itemid),))
        p = self.cursor.fetchone()[0]

        self.ui.price_display_label.setText(str(p))

    def insertNew_order_details_items(self):        #add button on new order page
        orderid = self.ui.lineEdit.text()

        self.cursor.execute('select Order_Num from order_list order by Order_Num asc')
        a = self.cursor.fetchall()

        if len(a) != 0:
            order_num = a[len(a)-1][0] + 1
        else:
            order_num = 1

        item_name = self.ui.comboBox.currentText()
        self.cursor.execute('select Item_ID from inventory where Item_Name = %s', (item_name,))
        itemid = self.cursor.fetchone()[0]

        quant = self.ui.spinBox.text()

        self.cursor.execute('insert into order_list values(%s, %s, %s, %s, %s)', (order_num, orderid, itemid, quant, 0))

        '''
                try:
                    self.cursor.execute('insert into order_list values(%s, %s, %s, %s, %s)', (order_num, orderid, itemid, quant, 0))
                except Exception as e:
                    print(e)
        '''
        try:
            self.loadnew_order_data()
        except Exception as e:
            print(e)

    def loadnew_order_data(self):
        orderid = self.ui.lineEdit.text()

        self.cursor.execute("select Item_ID, Item_name, Quantity, Order_Price from order_list natural left outer join inventory where Order_ID = %s", (orderid,))

        a = self.cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(a))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Item ID", "Quantity", "Item Name", "Price"])

        row = 0

        for x in a:
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))

            row += 1




########################################################

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        main_win = MainWindow()
        main_win.main_win.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)