# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:55:02 2015

@author: 97hamsah
"""
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import model

class Exam1(QMainWindow):
    
    def __init__(self, parent=None):
        super(Exam1, self).__init__()
        
        self.setWindowTitle("Exam1 template")
        
        self.initUI()
        
    
    def initUI(self):
        """This method is called when the application first runs
            The method initializes all the gui """
        self.frame = QWidget(self)
        self.setCentralWidget(self.frame)
        self.layout = QVBoxLayout
        self.form_layout = QFormLayout
        self.resize(200,500)
        
        self.name = QLineEdit(self)
        #Lägger till en textruta
        self.name.move(50,0)
        #Flyttar textrutan
        self.text = QLabel("Färg:", self)
        self.text.move(25,0)
        
        
        
        self.name2 = QLineEdit(self)
        #Lägger till en textruta
        self.name2.move(50,30)
        #Flyttar textrutan
        self.text2 = QLabel("Kön:", self)
        self.text2.move(25,30)
        
        
        
        self.djur = QComboBox(self)
        #skapar en "Combobox"
        self.djur.addItem("Välj djur:")
        self.djur.addItem("Katt")
        self.djur.addItem("Fågel")
        #Lägger till olika alternativ i comboboxen
        self.djur.move(50,70)
        #Flyttar komboboxen
        
        self.knapp_kor = QPushButton("Kör",self)
        #Skapar en knapp som det står "kör" på
        self.knapp_kor.move(50,100)
        #Flyttar knappen
        
        
        self.knapp_rensa = QPushButton("Rensa", self)
        self.knapp_rensa.clicked.connect(self.rensa)
        self.knapp_rensa.move(50,130)
        
        
    def rensa(self):
        self.name.setText("")
        self.name2.setText("")
        self.djur.setText("Välj djur:")
        
        
    def run(self):
        self.show()
        sys.exit(app.exec_())


app = QApplication(sys.argv)

# Start the program by calling the run method. 
# When the run method is called the Exam1.__init__ is run too
Exam1().run()