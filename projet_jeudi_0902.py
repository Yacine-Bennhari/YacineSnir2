

import sys
import tkinter as tk
from PySide6 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class ConfigForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle("Application IPTV")
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

        self.layout = QtWidgets.QFormLayout()   #création d'un form layout avec la classe QFormLayout situé dans le module QtWidget(formualaire)

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
   
        player.show()
        form.hide()


    def config(self):
        # if self.radioBt_config.isChecked():
        #     print("Méthode configuration des chaines")
            # form2.hide()
            # form1.show()
     
        player.show()
        form.show()

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



    



import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

class LecteurVideo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle("Lecteur Vidéo")
        self.setWindowIcon(QtGui.QIcon(r"C:\Users\snir\Downloads\network.ico"))

        # Create a QVideoWidget to display the video
        self.video_widget = QVideoWidget()
        self.lbl= QtWidgets.QLabel()
        mon_logo = QtGui.QPixmap(r"C:\Users\snir\Downloads\player.ico")
        self.lbl.setPixmap(mon_logo)
        

        # Create a QMediaPlayer to play the video
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

        # Create a QFileDialog to select a video file
        self.file_dialog = QtWidgets.QFileDialog(self)
        self.file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        self.file_dialog.setNameFilter("Video files (*.mp4 *.avi *.mkv *.m4v)")

        # Create a QToolBar with buttons to open, play, and stop the video
        self.toolbar = QtWidgets.QToolBar("Controls", self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.open_button = self.toolbar.addAction("Open")
        self.open_button.triggered.connect(self.open_video)

        self.liste_chaines_button = self.toolbar.addAction("Liste des chaines")
        self.liste_chaines_button.triggered.connect(self.open_video)

        self.play_button = self.toolbar.addAction("Play")
        self.play_button.triggered.connect(self.play_video)

        self.stop_button = self.toolbar.addAction("Stop")
        self.stop_button.triggered.connect(self.stop_video)

        self.config_button = self.toolbar.addAction("Config chaine")
        self.config_button.triggered.connect(self.config_chaine)
        # self.config_chaine_button.triggered.connect(self.config_chaine)
        # self.config_chaine_button = self.toolbar.addAction("Configuration des chaines")

        # Set the central widget to be the video widget
        self.setCentralWidget(self.video_widget)

    def open_video(self):
        """Open a video file and set it as the media for the media player."""
        if self.file_dialog.exec_():
            video_file = self.file_dialog.selectedFiles()[0]
            self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_file)))

    def liste_chaine(self):
        pass

    def play_video(self):
        """Start playing the current video."""
        self.media_player.play()

    def stop_video(self):
        """Stop playing the current video."""
        self.media_player.stop()

    def config_chaine(self):
    
        player.hide()
        form.show()


if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = ConfigForm()
    player = LecteurVideo()
    player.hide()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()
