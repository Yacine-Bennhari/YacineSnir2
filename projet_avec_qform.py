# import cv2
# import numpy

# # Open the video file
# video = cv2.VideoCapture("Users\snir\Desktop\Monpremierprojet.m4v")

# # Check if the video is opened successfully
# if not video.isOpened():
#     print("Error opening the video")
#     exit()

# # Read the frames of the video
# while True:
#     ret, frame = video.read()
#     if not ret:
#         break

#     # Do something with the frame here (e.g. display it)
#     cv2.imshow("Video", frame)

#     # Exit if the user presses 'q'
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# # Release the resources
# video.release()
# cv2.destroyAllWindows()

########################################################################################

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# app = QtWidgets.QApplication([])
# player = QMediaPlayer()
# video_widget = QVideoWidget()
# player.setVideoOutput(video_widget)
# video_widget.show()
# player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("Mon premier projet.m4v")))
# player.play()
# app.exec_()

########################################################################################

import sys
from PySide6 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Lecteur video")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        # self.setup_connections()
        # self.main_widget()

        # Créer un QVideoWidget pour afficher la vidéo
        # self.video_widget = QVideoWidget()

        # # Créer un QMediaPlayer pour lire la vidéo
        # self.media_player = QMediaPlayer(self)
        # self.media_player.setVideoOutput(self.video_widget)

        # # Créer un QFileDialog pour sélectionner un fichier vidéo
        # self.file_dialog = QtWidgets.QFileDialog(self)
        # self.file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        # self.file_dialog.setNameFilter("")

        # # Créez une QToolBar avec des boutons cliquables
        # self.toolbar = QtWidgets.QToolBar("Controls", self)
        # self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        # self.button_media = self.toolbar.addAction("Média")
        # self.button_media.triggered.connect(self.media_video)
        # self.button_lecture = self.toolbar.addAction("Lecture")
        # self.button_lecture.triggered.connect(self.lecture_video)
        # self.button_pause = self.toolbar.addAction("Pause")
        # self.button_pause.triggered.connect(self.pause_video)
        # self.button_stop = self.toolbar.addAction("Stop")
        # self.button_stop.triggered.connect(self.stop_video)
        # self.button_affichage = self.toolbar.addAction("Affichage")
        # self.button_affichage.triggered.connect(self.affichage_video)

        
        
        # Définir le widget central comme widget vidéo
        # self.setCentralWidget(self.video_widget)
        
    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.radioBt_lecture_video = QtWidgets.QRadioButton("Lecture Vidéo")
        self.radioBt_config = QtWidgets.QRadioButton("Configuration des chaines")

        self.lbl_numero_chaine = QtWidgets.QLabel("Numéro de chaine")
        self.LEdit_numero_chaine = QtWidgets.QLineEdit()
        self.LEdit_numero_chaine.setPlaceholderText("Exemple: 2 ")

        self.lbl_nom_chaine = QtWidgets.QLabel("Nom de chaine")
        self.LEdit_nom_chaine = QtWidgets.QLineEdit()
        self.LEdit_nom_chaine.setPlaceholderText("Exemple: France 2 ")

        self.lbl_adresse_chaine = QtWidgets.QLabel("Adresse multicast de la chaine")
        self.LEdit_adresse_chaine = QtWidgets.QLineEdit()
        self.LEdit_adresse_chaine.setPlaceholderText("Exemple: 239.1.1.65 ")
        
        self.lbl_Port = QtWidgets.QLabel(" Port ")
        self.LEdit_Port = QtWidgets.QLineEdit()
        self.LEdit_Port.setPlaceholderText("Exemple: 1234")

        self.btn_Enregistrer = QtWidgets.QPushButton("Enregistrer")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")

        # self.message = QtWidgets.QMessageBox()
        # # self.message.setText("Votre saisie est incorrecte")

    def addWigets_to_layouts(self):
        self.layoutH0.addWidget(self.radioBt_lecture_video)
        self.layoutH0.addWidget(self.radioBt_config)

        self.layoutH1.addWidget(self.lbl_numero_chaine)
        self.layoutH1.addWidget(self.LEdit_numero_chaine)

        
        self.layoutH2.addWidget(self.lbl_nom_chaine)
        self.layoutH2.addWidget(self.LEdit_nom_chaine)

        self.layoutH3.addWidget(self.lbl_adresse_chaine)
        self.layoutH3.addWidget(self.LEdit_adresse_chaine)

        self.layoutH4.addWidget(self.lbl_Port)
        self.layoutH4.addWidget(self.LEdit_Port)

        self.layoutH5.addWidget(self.btn_Enregistrer)
        self.layoutH5.addWidget(self.btn_Effacer)

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)

        self.setLayout(self.layoutV)

    def lecture_video(self):
        if self.radioBt_lecture_video.isChecked():
            print("Méthode Lecture vidéo")
            form1.hide()
            form2.show()


    def config(self):
        if self.radioBt_config.isChecked():
            print("Méthode configuration")
            form2.hide()
            form1.show()

    # def media_video(self):
    #     """Ouvrez un fichier vidéo et définissez-le comme média pour le lecteur multimédia."""
    #     if self.file_dialog.exec_():
    #         video_file = self.file_dialog.selectedFiles()[0]
    #         self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_file)))

    # def lecture_video(self):
    #     """Lecture de la vidéo."""
    #     self.media_player.play()

    # def stop_video(self):
    #     """Arrêt de la lecture vidéo."""
    #     self.media_player.stop()

    # def pause_video(self):
    #     self.media_player.pause()

    # def affichage_video(self):
    #     pass



class MaFenetre2(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Lecteur video")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        # self.setup_connections()
        # self.main_widget()

    def create_layouts(self):
        self.formumaire = QtWidgets.QFormLayout() 

        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()

        self.layoutH5 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.radioBt_lecture_video = QtWidgets.QRadioButton("Lecture Vidéo")
        self.radioBt_config = QtWidgets.QRadioButton("Configuration des chaines")

       
        self.LEdit_numero_chaine = QtWidgets.QLineEdit()
        self.LEdit_numero_chaine.setPlaceholderText("Exemple: 2 ")

      
        self.LEdit_nom_chaine = QtWidgets.QLineEdit()
        self.LEdit_nom_chaine.setPlaceholderText("Exemple: France 2 ")

       
        self.LEdit_adresse_chaine = QtWidgets.QLineEdit()
        self.LEdit_adresse_chaine.setPlaceholderText("Exemple: 239.1.1.65 ")
        
       
        self.LEdit_Port = QtWidgets.QLineEdit()
        self.LEdit_Port.setPlaceholderText("Exemple: 1234")

        self.formumaire.addRow("Numéro de chaine:", self.LEdit_numero_chaine)
        self.formumaire.addRow("Nom de chaine:", self.LEdit_nom_chaine)
        self.formumaire.addRow("Adresse multicast de la chaine:", self.LEdit_adresse_chaine)
        self.formumaire.addRow("Port r:", self.LEdit_Port)

        self.btn_Enregistrer = QtWidgets.QPushButton("Enregistrer")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")


        # self.message = QtWidgets.QMessageBox()
        # # self.message.setText("Votre saisie est incorrecte")

    def addWigets_to_layouts(self):
        self.layoutH0.addWidget(self.radioBt_lecture_video)
        self.layoutH0.addWidget(self.radioBt_config)
        self.layoutH1.addLayout(self.formumaire)

      

        self.layoutH5.addWidget(self.btn_Enregistrer)
        self.layoutH5.addWidget(self.btn_Effacer)


        # self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        
        # self.layoutV.addLayout(self.layoutH5)

        self.setLayout(self.layoutV)

    def lecture_video(self):
        if self.radioBt_lecture_video.isChecked():
            print("Méthode lecture vidéo")
            form1.hide()
            form2.show()


    def config(self):
        if self.radioBt_config.isChecked():
            print("Méthode configuration des chaines")
            form2.hide()
            form1.show()

    # def setup_connections():
    #     self.btn_Enregistrer.clicked.connect(self.Enregistrer)
  


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    # Create and show the form
    form1 = MaFenetre()
    form2 = MaFenetre2()
    form1.show()
    form2.hide()

    app.exec()  
    
    # app = QtWidgets.QApplication(sys.argv)
    # player = VideoPlayer()
    # player.show()
    # sys.exit(app.exec_())
