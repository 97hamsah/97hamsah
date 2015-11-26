# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:55:02 2015

@author: 97hamsah
"""
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from model import * 
model = Model()
Bird() = "Fågel"




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
        self.form_layout = QFormLayout()
        self.resize(200,300)
        
        self.name = QLineEdit()
        #Lägger till en textruta
        
        #Flyttar textrutan
        
        self.form_layout.addRow("Färg", self.name)
        
        
        
        self.name2 = QLineEdit()
        #Lägger till en textruta
        
        #Flyttar textrutan
        
        self.form_layout.addRow("Kön", self.name2)
        
        
        self.vingspann = QLineEdit()
        self.vingspanntext = QLabel("Vingspann")
        
        self.svanslangd = QLineEdit()
        self.svanslangdtext = QLabel("Svanslängd")
        
        
        self.djur = QComboBox(self)
        #skapar en "Combobox"
        self.djur.addItem("Välj djur:")
        self.djur.addItem("Katt")
        self.djur.addItem("Fågel")
        #Lägger till olika alternativ i comboboxen
        self.form_layout.addRow(self.djur)
        #Flyttar komboboxen
        
        self.knapp_add = QPushButton("Lägg till",self)
        self.form_layout.addRow(self.knapp_add)
        #Skapar en knapp som det står "Lägg till" på
        self.knapp_add.clicked.connect(self.knapptryck)
        #Flyttar knappen
        self.djur.activated[str].connect(self.combo)
        
        
        self.knapp_rensa = QPushButton("Rensa", self)
        self.knapp_rensa.clicked.connect(self.rensa)
        self.form_layout.addRow(self.knapp_rensa)
        
        
        self.frame.setLayout(self.form_layout)        
        
    def rensa(self):
        self.name.setText("")
        self.name2.setText("")
        self.vingspann.setText("")
        self.svanslangd.setText("")
        
    def knapptryck(self):
        if self.valt_djur == "Fågel":
            model.add_bird(self.name.text(), self.name2.text(), "Vingspann här")
            print(Model().lista)
        if self.valt_djur == "Katt":
            model.add_cat(self.name.text(), self.name2.text(), "Svanslängd här")
            print(Model().lista)
        
    def combo(self, valt_djur):
        self.valt_djur = valt_djur
        self.combo_drop()
        
    def combo_drop(self):
        if self.valt_djur == "Fågel":
            self.form_layout.addRow(self.vingspanntext, self.vingspann)
        
        if self.valt_djur == "Katt":
            self.form_layout.addRow(self.svanslangdtext, self.svanslangd)
            
        
            
    def run(self):
        self.show()
        sys.exit(app.exec_())


app = QApplication(sys.argv)

# Start the program by calling the run method. 
# When the run method is called the Exam1.__init__ is run too
Exam1().run()