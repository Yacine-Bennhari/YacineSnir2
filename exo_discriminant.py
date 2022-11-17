from PySide6 import QtWidgets
from math import sqrt

import sys

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Calculateur du discriminant Delta")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.layoutH6 = QtWidgets.QHBoxLayout()
        self.layoutH7 = QtWidgets.QHBoxLayout()
        

    def create_widgets(self):
        self.lbl_nombre1 = QtWidgets.QLabel("valeur de a : ")
        self.LEdit_nombre1 = QtWidgets.QLineEdit()
        self.LEdit_nombre1.setPlaceholderText("Saisir un nombre entier")

        self.lbl_nombre2 = QtWidgets.QLabel("valeur de b : ")
        self.LEdit_nombre2 = QtWidgets.QLineEdit()
        self.LEdit_nombre2.setPlaceholderText("Saisir un nombre entier")

        self.lbl_nombre3 = QtWidgets.QLabel("valeur de c : ")
        self.LEdit_nombre3 = QtWidgets.QLineEdit()
        self.LEdit_nombre3.setPlaceholderText("Saisir un nombre entier")

        self.btn_Calculer = QtWidgets.QPushButton("Calculer")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")
        self.lbl_message1 = QtWidgets.QLabel(" Le discriminant  = ")
        self.lbl_produit1 = QtWidgets.QLabel("......")
        self.lbl_message2 = QtWidgets.QLabel("les racines x1 et x2 sont : ")
        self.lbl_produit2 = QtWidgets.QLabel("......")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_nombre1)
        self.layoutH1.addWidget(self.LEdit_nombre1)

        self.layoutH2.addWidget(self.lbl_nombre2)
        self.layoutH2.addWidget(self.LEdit_nombre2)

        self.layoutH3.addWidget(self.lbl_nombre3)
        self.layoutH3.addWidget(self.LEdit_nombre3)

        self.layoutH4.addWidget(self.btn_Calculer)
        self.layoutH4.addWidget(self.btn_Effacer)

        
        self.layoutH5.addWidget(self.lbl_message1)
        self.layoutH5.addWidget(self.lbl_produit1)

        self.layoutH6.addWidget(self.lbl_message2)
        self.layoutH6.addWidget(self.lbl_produit2)

        self.layoutH7.addWidget(self.btn_Quitter)

        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.layoutV.addLayout(self.layoutH6)
        self.layoutV.addLayout(self.layoutH7)

        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Calculer.clicked.connect(self.calculer)
        self.btn_Effacer.clicked.connect(self.clear_Ledit)
        self.btn_Quitter.clicked.connect(quit)
         
    def clear_Ledit(self):
        self.LEdit_nombre1.setText("")
        self.LEdit_nombre2.setText("")
        self.LEdit_nombre3.setText("")
        self.lbl_produit1.setText("")
        self.lbl_produit2.setText("")
    
    def calculer(self):
        a= int(self.LEdit_nombre1.text())
        b = int(self.LEdit_nombre2.text())
        c = int(self.LEdit_nombre3.text())

        delta = (b*b) -  (4*a*c)
        self.lbl_produit1.setText(str(delta))
        print(delta)

        if delta > 0:
            x1 = ((-b)- sqrt(delta))/(2*a)
            x2 = ((-b)+ sqrt(delta))/(2*a)
        
        elif delta == 0:
            x0 = (-b)/(2*a)

        elif delta < 0:
            resultat2 = print("il n'y a pas de solutions sur R :)")
         
        
        # self.lbl_produit1.setText(str(delta))
        self.lbl_produit2.setText(str(resultat2))
        # print(delta)
        print(resultat2)
        

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()