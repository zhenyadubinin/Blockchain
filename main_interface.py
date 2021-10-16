# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'midterm_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setEnabled(True)
        MainWindow.resize(1332, 850)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("* {\n"
"   box-sizing: border-box;\n"
"   color: rgb(56, 13, 1);\n"
"   font-family: \'Raleway\', \'Lato\', Arial, sans-serif;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-image: url(\"images/coffee_background.jpg\");\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    background-attachment: fixed;\n"
"    background-size: cover;\n"
"    background-color: rgb(35, 33, 42);\n"
"    padding: 60px 50px;\n"
"\n"
"    /* Font styles */\n"
"\n"
"    font-family: \'Raleway\', \'Lato\', Arial, sans-serif;\n"
"    text-shadow: 0 10px 10px rgba(0,0,0,0.3);\n"
"}\n"
"\n"
"QMainWindow:before {\n"
"   content: \"\";\n"
"   position: absolute;\n"
"   top: 0;\n"
"   left: 0;\n"
"   right: 0;\n"
"   bottom: 0;\n"
"   /* background: linear-gradient(to right bottom, rgba(43, 44, 78, .5), rgba(104, 22, 96, .5)); */\n"
"}\n"
"\n"
"QLabel {\n"
"   display: block;\n"
"   font-size: 26px;\n"
"   background-color: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"   display: block;\n"
"   width: 100%;\n"
"   height: 30px;\n"
"   padding: 0 15px;\n"
"   border-width: 0;\n"
"   line-height: 40px;\n"
"   border-radius: 5px;\n"
"   color: black;\n"
"   background: rgba(255, 255, 255, .8);\n"
"}\n"
"\n"
"QComboBox {\n"
"   display: block;\n"
"   width: 100%;\n"
"   height: 30px;\n"
"   padding: 0 15px;\n"
"   margin: 0;\n"
"   border-width: 0;\n"
"   line-height: 40px;\n"
"   border-radius: 5px;\n"
"   color: black;\n"
"   background: rgba(255, 255, 255, .8);\n"
"}\n"
"\n"
"QSpinBox { \n"
"   display: block;\n"
"   margin: 0;\n"
"   border-width: 0;\n"
"   line-height: 40px;\n"
"   border-radius: 5px;\n"
"   color: black;\n"
"   background: rgba(255, 255, 255, .8);\n"
"}\n"
"\n"
"QDateEdit {\n"
"   display: block;\n"
"   width: 100%;\n"
"   height: 30px;\n"
"   padding: 0 15px;\n"
"   margin: 0;\n"
"   border-width: 0;\n"
"   line-height: 40px;\n"
"   border-radius: 5px;\n"
"   color: black;\n"
"   background: rgba(255, 255, 255, .8);\n"
"}\n"
"\n"
"QPushButton{\n"
"    display: block;\n"
"    line-height: 40px;\n"
"    padding: 0 15px;\n"
"    margin: 0;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(214, 140, 105), stop:1             rgb(191, 94, 49));\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(255, 219, 210), stop:1              rgb(217, 148, 115));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(234, 236, 239);\n"
"}\n"
"\n"
"QFrame {\n"
"    border-radius: 10px;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(397, 60, 351, 341))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(30)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label.setEnabled(True)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: none;")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setEnabled(True)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: none;")
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setEnabled(True)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: none;")
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setEnabled(True)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color: none;")
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setEnabled(True)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background-color: none;")
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setEnabled(True)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color: none;")
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_2.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_4.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.lineEdit_5.raise_()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(350, 30, 451, 661))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setObjectName("frame")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(48, 400, 88, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color: none;")
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(227, 400, 171, 31))
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(100, 540, 229, 41))
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_9.setStyleSheet("background-color: none;\n"
"padding: 0;\n"
"height: 10px;\n"
"margin: 0;")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 590, 229, 31))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: white;")
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(48, 465, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("background-color: none;")
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(227, 465, 171, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(410, 470, 27, 21))
        self.toolButton.setObjectName("toolButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(810, 410, 341, 211))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_2)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 321, 191))
        self.calendarWidget.setStyleSheet("background-color: white;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.frame_2.raise_()
        self.frame.raise_()
        self.formLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1332, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Wallet"))
        self.label_2.setText(_translate("MainWindow", "Address"))
        self.label_3.setText(_translate("MainWindow", "Email"))
        self.label_4.setText(_translate("MainWindow", "First Name"))
        self.label_6.setText(_translate("MainWindow", "Sort of coffee"))
        self.label_5.setText(_translate("MainWindow", "Last Name"))
        self.label_7.setText(_translate("MainWindow", "Amount"))
        self.label_9.setText(_translate("MainWindow", "Total cost: 0$"))
        self.pushButton.setText(_translate("MainWindow", "Make order"))
        self.label_8.setText(_translate("MainWindow", "Delivery date"))
        self.toolButton.setText(_translate("MainWindow", "..."))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

