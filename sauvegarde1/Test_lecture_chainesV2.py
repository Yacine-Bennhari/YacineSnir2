import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Lecteur_video(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle("Lecteur Vidéo")

        self.setWindowIcon(QtGui.QIcon(r"C:\Users\snir\Downloads\network.ico"))
       
        # Créer un QVideoWidget pour afficher la vidéo
        self.video_widget = QVideoWidget()
        self.lbl= QtWidgets.QLabel()
        mon_logo = QtGui.QPixmap(r"C:\Users\snir\Downloads\player.ico")
        self.lbl.setPixmap(mon_logo)

        # Créer un QMediaPlayer pour lire la vidéo
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

        # Créez une QToolBar avec des boutons pour ouvrir, lire et arrêter la vidéo
        self.toolbar = QtWidgets.QToolBar("Contrôle", self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.ouvrir_button = self.toolbar.addAction("ouvrir")
        self.ouvrir_button.triggered.connect(self.open_video)

        self.liste_chaines_button = self.toolbar.addAction("Liste des chaines")
        self.liste_chaines_button.triggered.connect(self.liste_chaine)

        self.play_button = self.toolbar.addAction("Play")
        self.play_button.triggered.connect(self.play_video)

        self.stop_button = self.toolbar.addAction("Stop")
        self.stop_button.triggered.connect(self.stop_video)

        self.config_button = self.toolbar.addAction("Config chaine")
        self.config_button.triggered.connect(self.config_chaine)


        # Définir le widget central comme widget vidéo
        self.setCentralWidget(self.video_widget)

    def open_video(self, video_file):
        """Ouvrez un fichier vidéo et définissez-le comme média pour le lecteur multimédia."""
        url = QtCore.QUrl.fromUserInput(video_file)
        media = QMediaContent(url)
        self.media_player.setMedia(media)
        self.media_player.play()

    def liste_chaine(self):
        player1.hide()
        form.show()
        

    def play_video(self):
        """Lancez la lecture de la vidéo en cours."""
        self.media_player.play()

    def stop_video(self):
        """Arrêtez de jouer la vidéo en cours."""
        self.media_player.stop()

    def config_chaine(self):
    
        player1.hide()
        player2.show()
        
        
class Choix_chaines(QWidget):
    def __init__(self, parent=None):
        super(Choix_chaines, self).__init__(parent)
        self.resize(300,200)
        self.setWindowTitle("Choix des chaines")

        # self.create_layouts()
        # self.create_widgets()
        # self.addWigets_to_layouts()

        layout = QHBoxLayout()
        self.cb = QComboBox() #Création de la comboBox
        self.btn = QPushButton("Valider")
        self.cb.addItems(["BFM TV", "Gulli", "C8","CNEWS","CSTAR",]) # Ajouter une liste d'item    
        layout.addWidget(self.cb)
        layout.addWidget(self.btn)
        self.setLayout(layout)
        self.setWindowTitle("Choix des chaines")
        self.btn.clicked.connect(self.open_video)

    # def create_layouts(self):
    #     self.layoutV = QtWidgets.QVBoxLayout()
    #     self.layoutH0 = QtWidgets.QHBoxLayout()
    #     # self.layoutH1 = QtWidgets.QHBoxLayout()
    #     # self.layoutH2 = QtWidgets.QHBoxLayout()
    #     # self.layoutH3 = QtWidgets.QHBoxLayout()

    # def create_widgets(self):

    #     self.lbl_Texte = QtWidgets.QLabel("Veuillez choisir la chaine que vous voulez visionner et appuyer sur valider s'il vous plaît : ")
    #     self.LEdit_Texte = QtWidgets.QLineEdit()
        
    #     # self.message = QtWidgets.QMessageBox()
    #     # self.message.setText(" Votre saisie est incorrecte ")

    # def addWigets_to_layouts(self):
    #     self.layoutH0.addWidget(self.lbl_Texte)
    #     # self.layoutH1.addWidget(self.lbl_Texte)
    #     # self.layoutH2.addWidget(self.lbl_Texte)
    #     # self.layoutH3.addWidget(self.lbl_Texte)
    #     self.layoutV.addLayout(self.layoutH0)

    #     self.setLayout(self.layoutV)

    def open_video(self):

        if self.cb.currentText() == "BFM TV":
            print(self.cb.currentText())
            video_file = "rtp://225.0.0.51:20000"
            player1.open_video(video_file)
            player1.show()
            form.hide()

        elif self.cb.currentText() == "Gulli":
            print(self.cb.currentText())
            video_file = "rtp://225.0.0.54:20000"
            player1.open_video(video_file)
            player1.show()
            form.hide()

        elif self.cb.currentText() == "C8":
            print(self.cb.currentText())
            video_file = "rtp://225.0.0.50:20000"
            player1.open_video(video_file)
            player1.show()
            form.hide()

        elif self.cb.currentText() == "CNEWS":
            print(self.cb.currentText())
            video_file = "rtp://225.0.0.52:20000"
            player1.open_video(video_file)
            player1.show()
            form.hide()

        elif self.cb.currentText() == "CSTAR":
            print(self.cb.currentText())
            video_file = "rtp://225.0.0.53:20000"
            player1.open_video(video_file)
            player1.show()
            form.hide()

        else:
            print("Chaine inconnue")


class Configuration_chaines(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle("Configuration des chaines")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        self.main_widget()
        self.setWindowIcon(QtGui.QIcon(r"C:\Users\snir\Downloads\network.ico"))

        

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.formLayout = QtWidgets.QFormLayout() 

        self.layout = QtWidgets.QFormLayout()   #création d'un form layout avec la classe QFormLayout situé dans le module QtWidget(formulaire)

    def create_widgets(self):
        # self.radioBt_lecture_video = QtWidgets.QRadioButton("Lecture video")
       
        # self.radioBt_config = QtWidgets.QRadioButton("Configuration des chaines")
        self.Btn_lecture_video = QtWidgets.QPushButton("Lecture video")

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
        
        self.layoutH0.addWidget(self.Btn_lecture_video)

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
    
        self.Btn_lecture_video.clicked.connect(self.lecture_video)
         
    def clear_Ledit(self):
        self.LEdit_numero_chaine.setText("")
        self.LEdit_nom_chaine.setText("")
        self.LEdit_adresse_chaine.setText("")
        self.LEdit_Port.setText("")

    def lecture_video(self):
        # if self.radioBt_lecture_video.to:
        #     print("Méthode Lecture vidéo")
            # form1.hide()
            # form2.show()
   
        player1.show()
        player2.hide()


    def config(self):
        # if self.radioBt_config.isChecked():
        #     print("Méthode configuration des chaines")
            # form2.hide()
            # form1.show()
     
        player1.show()
        form.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player1 = Lecteur_video()
    player2 = Configuration_chaines()
    form = Choix_chaines()
    form.show()
    player1.hide()
    sys.exit(app.exec_())
