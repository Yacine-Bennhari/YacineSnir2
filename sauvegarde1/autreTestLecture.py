import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget





import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class VideoPlayer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player")





        # layout = QtWidgets.QHBoxLayout()
        # self.cb = QtWidgets.QComboBox() #Création de la comboBox
        # self.btn =QtWidgets.QPushButton("Valider")
        # self.cb.addItems(["TF1", "Fr2", "Fr3","Fr4","M6","Arte","BTM-TV"]) # Ajouter une liste d'item	
        # layout.addWidget(self.cb)
        # layout.addWidget(self.btn)
        # self.setLayout(layout)
    
        # self.btn.clicked.connect(self.faireQLQchose)












        # Create a QVideoWidget to display the video
        self.video_widget = QVideoWidget()

        # Create a QMediaPlayer to play the video
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)
        video_file = r"C:\Users\snir\Desktop\Monpremierprojet.m4v"
        self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_file)))
        
        self.media_player.play()

        
        


        # Create a QFileDialog to select a video file
        # self.file_dialog = QtWidgets.QFileDialog(self)
        # self.file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        # self.file_dialog.setNameFilter("")

        # # Create a QToolBar with buttons to open, play, and stop the video
        # self.toolbar = QtWidgets.QToolBar("Controls", self)
        # self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        # self.open_button = self.toolbar.addAction("Open")
        # self.open_button.triggered.connect(self.open_video)
        # self.play_button = self.toolbar.addAction("Play")
        # self.play_button.triggered.connect(self.play_video)
        # self.stop_button = self.toolbar.addAction("Stop")
        # self.stop_button.triggered.connect(self.stop_video)

        

        # Set the central widget to be the video widget
        self.setCentralWidget(self.video_widget)

    def open_video(self):
        """Open a video file and set it as the media for the media player."""
        
            # video_file = self.file_dialog.selectedFiles()[0]
            
        video_file = r"C:\Users\snir\Desktop\Monpremierprojet.m4v"

        self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_file)))

    def play_video(self):
        """Start playing the current video."""
        self.media_player.play()

    def stop_video(self):
        """Stop playing the current video."""
        self.media_player.stop()




class combodemo(QWidget):
    def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)

      
      
      layout = QHBoxLayout()
      self.cb = QComboBox() #Création de la comboBox
      self.btn =QPushButton("Valider")
      self.cb.addItems(["TF1", "Fr2", "Fr3","Fr4","M6","Arte","BTM-TV"]) # Ajouter une liste d'item	
      layout.addWidget(self.cb)
      layout.addWidget(self.btn)
      self.setLayout(layout)
      self.setWindowTitle("combo box demo")
      self.btn.clicked.connect(self.faireQLQchose)

    def faireQLQchose(self):

        if self.cb.currentText()=="TF1":
            self.video_widget = QVideoWidget()
            print(self.cb.currentText())
            self.media_player = QMediaPlayer(self)
            self.media_player.setVideoOutput(self.video_widget)
            # video_file = r"C:\Users\snir\Desktop\Monpremierprojet.m4v"
            video_file = "rtp://225.0.0.10:5004"
            self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_file)))
            
            self.media_player.play()
            player.show()
            form.hide()
            print("fin")
        else:
            print("Chaine inconnue")

    
        # self.video_widget = QVideoWidget()
        # print(self.cb.currentText())
        # self.media_player = QMediaPlayer(self)
        # self.media_player.setVideoOutput(self.video_widget)
        # video_file = r"C:\Users\snir\Desktop\Monpremierprojet.m4v"
        # self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_file)))
        
        # self.media_player.play()
        # player.show()
        # form.hide()
        # print("fin")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    form = combodemo()
    form.show()
    player.hide()
    sys.exit(app.exec_())
