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
        # self.layoutH8 = QtWidgets.QHBoxLayout()
        

    def create_widgets(self):
        self.lbl_Titre = QtWidgets.QLabel("Résolution d'équation du second degré")

        self.lbl_coef_a = QtWidgets.QLabel("x2 + ")
        self.LEdit_coef_a = QtWidgets.QLineEdit()
        self.LEdit_coef_a.setPlaceholderText("a")

        self.lbl_coef_b = QtWidgets.QLabel("+ x + ")
        self.LEdit_coef_b = QtWidgets.QLineEdit()
        self.LEdit_coef_b.setPlaceholderText("b")

        self.lbl_coef_c = QtWidgets.QLabel("= 0 ")
        self.LEdit_coef_c = QtWidgets.QLineEdit()
        self.LEdit_coef_c.setPlaceholderText("c")

        self.btn_Calculer = QtWidgets.QPushButton("Calculer")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")

        self.lbl_discriminant = QtWidgets.QLabel(" Le discriminant  = ")
        self.lbl_valeur_discriminant = QtWidgets.QLabel("......")

        self.lbl_racine1 = QtWidgets.QLabel(" x1 = ")
        self.lbl_racine2 = QtWidgets.QLabel(" x2 = ")
        self.lbl_resultatx1 = QtWidgets.QLabel("......")
        self.lbl_resultatx2 = QtWidgets.QLabel("......")
        self.lbl_discriminant_negatif = QtWidgets.QLabel("Il n'y a pas de solution sur R :)")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")


        self.message = QtWidgets.QMessageBox()
        self.message.setText("erreur de saisie")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_Titre)

        self.layoutH2.addWidget(self.LEdit_coef_a)
        self.layoutH2.addWidget(self.lbl_coef_a)
        self.layoutH2.addWidget(self.LEdit_coef_b)
        self.layoutH2.addWidget(self.lbl_coef_b)
        self.layoutH2.addWidget(self.LEdit_coef_c)
        self.layoutH2.addWidget(self.lbl_coef_c)

        self.layoutH3.addWidget(self.btn_Calculer)

        self.layoutH4.addWidget(self.lbl_discriminant)
        self.layoutH4.addWidget(self.lbl_valeur_discriminant)

        self.layoutH5.addWidget(self.lbl_racine1)
        self.layoutH5.addWidget(self.lbl_resultatx1)

        self.layoutH6.addWidget(self.lbl_racine2)
        self.layoutH6.addWidget(self.lbl_resultatx2)

        self.layoutH7.addWidget(self.btn_Effacer)
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
        self.LEdit_coef_a.setText("")
        self.LEdit_coef_b.setText("")
        self.LEdit_coef_c.setText("")
        self.lbl_valeur_discriminant.setText("")
        self.lbl_resultatx1.setText("")
        self.lbl_resultatx2.setText("")
    
    def calculer(self):
        try:
            a= float(self.LEdit_coef_a.text())
            b = float(self.LEdit_coef_b.text())
            c = float(self.LEdit_coef_c.text())
        except:

            self.message.show()
            self.clear_Ledit()
        else:

            if a == 0:
                self.message = QtWidgets.QMessageBox()
                self.message.setText("Vous avez saisi zéro")
            # print("erreur de saisie")
            self.message.show()
            self.clear_Ledit()

            if b == 0:
                self.message = QtWidgets.QMessageBox()
                self.message.setText("Vous avez saisi zéro")
            self.message.show()
            self.clear_Ledit()

            if c == 0:
                self.message = QtWidgets.QMessageBox()
                self.message.setText("Vous avez saisi zéro")
            self.message.show()
            self.clear_Ledit()
        
            

            delta = (b*b) -  (4*a*c)
            self.lbl_valeur_discriminant.setText(str(delta))
            print(delta)

            if delta > 0:
                x1 = ((-b)- sqrt(delta))/(2*a)
                self.lbl_resultatx1.setText(str(x1))
                x2 = ((-b)+ sqrt(delta))/(2*a)
                self.lbl_resultatx2.setText(str(x2))
                print(x1)
                print(x2)
            
            elif delta == 0:
                x0 = (-b)/(2*a)
                # self.lbl_resultatx0.setText(str(x0))


            else:
                resultat2 = print("il n'y a pas de solutions sur R :)")
                # self.lbl_discriminant_negatif.setText(resultat2)
            
            
            # # self.lbl_produit1.setText(str(delta))
            # self.lbl_produit2.setText(str(resultat2))
            # # print(delta)
            # print(resultat2)
        

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()