import sys
import tkinter as tk
from PySide6 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class MaFenetre1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle("Application IPTV")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        self.main_widget()

        

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.formLayout = QtWidgets.QFormLayout() 

        self.layout = QtWidgets.QFormLayout()   #création d'un form layout avec la classe QFormLayout situé dans le module QtWidget(formualaire)

    def create_widgets(self):
        self.radioBt_lecture_video = QtWidgets.QRadioButton("Lecture video")
        self.radioBt_config = QtWidgets.QRadioButton("Configuration des chaines")

        self.lbl_vide = QtWidgets.QLabel("")

        self.LEdit_numero_chaine = QtWidgets.QLineEdit()
        self.LEdit_numero_chaine.setPlaceholderText("Exemple: 2 ")

      
        self.LEdit_nom_chaine = QtWidgets.QLineEdit()
        self.LEdit_nom_chaine.setPlaceholderText("Exemple: France 2 ")

       
        self.LEdit_adresse_chaine = QtWidgets.QLineEdit()
        self.LEdit_adresse_chaine.setPlaceholderText("Exemple: 239.1.1.65 ")
        
       
        self.LEdit_Port = QtWidgets.QLineEdit()
        self.LEdit_Port.setPlaceholderText("Exemple: 1234")

        self.btn_Enregistrer = QtWidgets.QPushButton("Enregistrer")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")


        # self.formLayout.addRow("Lecture Vidéo", self.radioBt_lecture_video)
        # self.formLayout.addRow("Configuration des chaines", self.radioBt_config)

        self.formLayout.addRow("Numéro de chaine:", self.LEdit_numero_chaine)
        self.formLayout.addRow("Nom de chaine:", self.LEdit_nom_chaine)
        self.formLayout.addRow("Adresse multicast de la chaine:", self.LEdit_adresse_chaine)
        self.formLayout.addRow("Port :", self.LEdit_Port)
        # self.formLayout.addRow("Enregistrer", self.btn_Enregistrer)
        # self.formLayout.addRow("Effacer", self.btn_Effacer)


        
        # self.layout.addRow("Name of the student of the year:", self.LEdit_Nom)  # """ ajouter une ligne à notre tableau ( formLayout ) 
        #                                                                         son label c'est : le texte "Name of the student of the year:" 
        #                                                                         et le deuxième paramètre c'est le widget self.LEdit_Nom"""

    def addWigets_to_layouts(self):
        
        
        self.layoutH0.addWidget(self.radioBt_lecture_video)
        self.layoutH0.addWidget(self.radioBt_config)

        self.layoutH1.addWidget(self.lbl_vide)

        self.layoutH2.addWidget(self.lbl_vide)

        self.layoutH3.addWidget(self.btn_Enregistrer)
        self.layoutH3.addWidget(self.btn_Effacer)
        
        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.formLayout)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.setLayout(self.layoutV)

    def main_widget(self):
        self.widget = QtWidgets.QWidget(self)  
        self.widget.setLayout(self.layoutV)
        self.setCentralWidget(self.widget)
                         
    def setup_connections(self):
        self.btn_Enregistrer.clicked.connect(quit)
        self.btn_Effacer.clicked.connect(self.clear_Ledit)
         
    def clear_Ledit(self):
        self.LEdit_numero_chaine.setText("")
        self.LEdit_nom_chaine.setText("")
        self.LEdit_adresse_chaine.setText("")
        self.LEdit_Port.setText("")

    def lecture_video(self):
        if self.radioBt_lecture_video.isChecked():
            print("Méthode Lecture vidéo")
            # form1.hide()
            # form2.show()

    def config(self):
        if self.radioBt_config.isChecked():
            print("Méthode configuration des chaines")
            # form2.hide()
            # form1.show()

# class MaFenetre2(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.resize(300,200)
#         self.setWindowTitle("Lecture Vidéo")
#         self.create_layouts()
#         self.create_widgets()
#         self.addWigets_to_layouts()
#         self.setup_connections()
#         self.main_widget()



    

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre1()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()
