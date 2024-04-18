from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import string

class HomeController(QDialog):
    def __init__(self,parent=None):
        super(HomeController,self).__init__(parent)
        loadUi('views/home.ui',self)
        self.btnEncrypt.clicked.connect(self.encrypt)
        self.btnDecrypt.clicked.connect(self.decrypt)
        self.btnClear.clicked.connect(self.clear)
    def encrypt(self):
        try:
            plain = self.txtPlain.text().replace(' ', '')
            key = self.txtKey.text()
            if not plain.isalpha() and not key.isalpha():
                raise ValueError("Input harus berupa huruf dan key tidak boleh memiliki spasi")
            newKey = ''
            if len(plain) != len(key):
                for i in range(len(plain)):
                    newKey += key[i%len(key)]
            alfabet = string.ascii_lowercase
            chiper = ''
            for i in range(len(plain)):
                chiper += alfabet[(alfabet.index(plain[i].lower()) + alfabet.index(newKey[i])) % 26]
            self.txtChiper.setText(chiper)
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
        
    def decrypt(self):
        try:
            chiper = self.txtChiper.text().replace(' ', '')
            key = self.txtKey.text()
            if not chiper.isalpha() and not key.isalpha():
                raise ValueError("Input harus berupa huruf dan key tidak boleh memiliki spasi")
            newKey = ''
            if len(chiper) != len(key):
                for i in range(len(chiper)):
                    newKey += key[i%len(key)]
            alfabet = string.ascii_lowercase
            plain = ''
            for i in range(len(chiper)):
                plain += alfabet[(alfabet.index(chiper[i].lower()) - alfabet.index(newKey[i])) % 26]
            self.txtPlain2.setText(plain)
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def clear(self):
        self.txtPlain.clear()
        self.txtKey.clear()
        self.txtChiper.clear()
        self.txtPlain2.clear()
        