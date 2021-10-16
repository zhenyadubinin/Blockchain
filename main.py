import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_interface import Ui_MainWindow
from transaction_window import AnotherWindow
from datetime import datetime, timedelta
from threading import Thread
import requests
import random
import string
import time
dir_name = 'images/'

coffee_list = {
        'Brazil': 125,
        'Columbia': 120,
        'Gvatemala': 105,
        'Kenya': 115,
        'Ethiopia': 100,
        'Brazil roasted': 140,
        'Columbia roasted': 135,
        'Gvatemala roasted': 120,
        'Kenya roasted': 130,
        'Ethiopia roasted': 115,
    }

def set_coffee():
    ui.comboBox.addItems(coffee_list.keys())
    ui.comboBox.setCurrentText(list(coffee_list.keys())[0])

def valueChange():
    cost = ui.spinBox.value() * coffee_list[ui.comboBox.currentText()]
    ui.label_9.setText('Total cost: ' + str(cost) + '$')

def alert():
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Message Window")
    msg.setText("You haven't filled out all the fields in the form!")
    msg.exec_()

def alert_date():
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Message Window")
    msg.setText("Incorrect Date!")
    msg.exec_()

def btnClicked():
    wallet = ui.lineEdit.text()
    address = ui.lineEdit_2.text()
    email = ui.lineEdit_3.text()
    first_name = ui.lineEdit_4.text()
    last_name = ui.lineEdit_5.text()
    sort = ui.comboBox.currentText()
    amount = ui.spinBox.value()
    del_date = ui.dateEdit.dateTime().toString('yyyy-MM-dd')
    total_cost = ui.spinBox.value() * coffee_list[ui.comboBox.currentText()]

    if wallet == '' or address == '' or email == '' or first_name == '' or last_name == '' or amount == 0:
        alert()
    elif del_date <= str(datetime.now())[:10]:
        alert_date()
    else:
        print(wallet)
        print(address)
        print(email)
        print(first_name)
        print(last_name)
        print(sort)
        print(amount)
        print(del_date)
        print(total_cost)

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'wallet': wallet,
            'address': address,
            'sort': sort,
            'amount': amount,
            'del_date': del_date,
            'total_cost': total_cost,
        }

        response = requests.post('https://reqres.in/api/users', data=data)
        print(response)
        response = requests.get('https://reqres.in/api/users/2')
        print(response.json())

        show_transaction(first_name, last_name, address, email, sort, amount, del_date, wallet, total_cost)

def show_transaction(first_name, last_name, address, email, sort, amount, del_date, wallet, total_cost):
    ui.w = AnotherWindow()

    letters = string.digits
    transaction_id = ''.join(random.choice(letters) for i in range(10))
    status_list = ['on the configuration', 'on the way', 'done']
    status = status_list[random.randrange(0, 3)]
    # status = status_list[0]
    my_wallet = '0d7hj3v9nhdk43'

    ui.w.transactionIDLabel_14.setText(first_name)
    ui.w.transactionIDLabel_15.setText(last_name)
    ui.w.transactionIDLabel_16.setText(email)
    ui.w.transactionIDLabel_17.setText(sort)
    ui.w.transactionIDLabel_18.setText(str(amount))
    ui.w.transactionIDLabel_19.setText(transaction_id)
    ui.w.transactionIDLabel_20.setText(status)
    ui.w.transactionIDLabel_20.setStyleSheet("QLabel { color : grey; }")
    ui.w.transactionIDLabel_21.setText(str(datetime.now()))
    ui.w.transactionIDLabel_22.setText(str(del_date))
    ui.w.transactionIDLabel_23.setText(wallet)
    ui.w.transactionIDLabel_24.setText(my_wallet)
    ui.w.transactionIDLabel_25.setText(str(total_cost) + '$')
    ui.w.transactionIDLabel_26.setText(str(total_cost * 0.05) + '$')
    ui.w.transactionIDLabel_27.setText(address)

    t1 = Thread(ui.w.show())
    t1.start()

def delivery(status_list, str):
    str.setText(status_list[0])
    str.setStyleSheet("QLabel { color : grey; }")

    timeStart = datetime.now()
    timeFinish = timeStart + timedelta(seconds=3)
    while timeStart < timeFinish:
        timeStart = datetime.now()
        pass

    str.setText(status_list[1])
    str.setStyleSheet("QLabel { color : yellow; }")

    timeStart = datetime.now()
    timeFinish = timeStart + timedelta(seconds=3)
    while timeStart < timeFinish:
        timeStart = datetime.now()
        pass

    str.setText(status_list[2])
    str.setStyleSheet("QLabel { color : green; }")

def show_date():
    if ui.frame_2.isVisible():
        ui.frame_2.hide()
        ui.calendarWidget.hide()
    else:
        ui.frame_2.show()
        ui.calendarWidget.show()

def on_click_calendar():
    ui.dateEdit.setDate(ui.calendarWidget.selectedDate())

def on_dateEdit_change():
    ui.calendarWidget.setSelectedDate(ui.dateEdit.date())

# create app
app = QtWidgets.QApplication(sys.argv)

# init
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.frame_2.hide()
ui.calendarWidget.hide()
set_coffee()

# signals
ui.pushButton.clicked.connect(btnClicked)
ui.spinBox.valueChanged.connect(valueChange)
ui.comboBox.currentTextChanged.connect(valueChange)
ui.calendarWidget.clicked.connect(on_click_calendar)
ui.dateEdit.dateChanged.connect(on_dateEdit_change)
ui.toolButton.clicked.connect(show_date)
MainWindow.show()

# main loop
t1 = Thread(sys.exit(app.exec_()))
t1.start()
t1.join()