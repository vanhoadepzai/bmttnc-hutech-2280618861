# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(130, 264, 61, 21))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(220, 264, 61, 21))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.lbl_header = QtWidgets.QLabel(self.centralwidget)
        self.lbl_header.setGeometry(QtCore.QRect(250, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_header.setFont(font)
        self.lbl_header.setObjectName("lbl_header")
        self.lbl_plaintext = QtWidgets.QLabel(self.centralwidget)
        self.lbl_plaintext.setGeometry(QtCore.QRect(70, 90, 61, 21))
        self.lbl_plaintext.setObjectName("lbl_plaintext")
        self.lbl_ciphertext = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ciphertext.setGeometry(QtCore.QRect(70, 200, 51, 20))
        self.lbl_ciphertext.setObjectName("lbl_ciphertext")
        self.lbl_infor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_infor.setGeometry(QtCore.QRect(300, 94, 61, 21))
        self.lbl_infor.setObjectName("lbl_infor")
        self.lbl_sign = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sign.setGeometry(QtCore.QRect(304, 204, 51, 20))
        self.lbl_sign.setObjectName("lbl_sign")
        self.txt_plain = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain.setGeometry(QtCore.QRect(130, 84, 151, 64))
        self.txt_plain.setObjectName("txt_plain")
        self.txt_cipher = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher.setGeometry(QtCore.QRect(130, 194, 151, 64))
        self.txt_cipher.setObjectName("txt_cipher")
        self.txt_inf = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_inf.setGeometry(QtCore.QRect(360, 84, 161, 64))
        self.txt_inf.setObjectName("txt_inf")
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(360, 194, 161, 64))
        self.txt_sign.setObjectName("txt_sign")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(360, 264, 61, 21))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(460, 264, 61, 21))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(420, 50, 91, 21))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_encrypt.setText(_translate("MainWindow", "encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "decrypt"))
        self.lbl_header.setText(_translate("MainWindow", "RSA CIPHER"))
        self.lbl_plaintext.setText(_translate("MainWindow", "Plaintext"))
        self.lbl_ciphertext.setText(_translate("MainWindow", "Ciphertext"))
        self.lbl_infor.setText(_translate("MainWindow", "Information"))
        self.lbl_sign.setText(_translate("MainWindow", "Signature"))
        self.btn_sign.setText(_translate("MainWindow", "sign"))
        self.btn_verify.setText(_translate("MainWindow", "verify"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
