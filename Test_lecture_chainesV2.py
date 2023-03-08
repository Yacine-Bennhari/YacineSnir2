import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget





import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# class VideoPlayer(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Video Player")

#         # Create a QVideoWidget to display the video
#         self.video_widget = QVideoWidget()

#         # Create a QMediaPlayer to play the video
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVideoOutput(self.video_widget)
#         self.media_player.play()

#         # Set the central widget to be the video widget
#         self.setCentralWidget(self.video_widget)

#     def open_video(self, video_file):
#         """Open a video file and set it as the media for the media player."""
#         self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromEncoded(video_file)))
#         self.media_player.play()

# class combodemo(QWidget):
#     def __init__(self, parent=None):
#         super(combodemo, self).__init__(parent)

#         layout = QHBoxLayout()
#         self.cb = QComboBox() #Création de la comboBox
#         self.btn = QPushButton("Valider")
#         self.cb.addItems(["TF1", "Fr2", "Fr3","Fr4","M6","Arte","BTM-TV"]) # Ajouter une liste d'item    
#         layout.addWidget(self.cb)
#         layout.addWidget(self.btn)
#         self.setLayout(layout)
#         self.setWindowTitle("combo box demo")
#         self.btn.clicked.connect(self.faireQLQchose)

#     def faireQLQchose(self):

#         if self.cb.currentText()=="TF1":
#             print(self.cb.currentText())
#             video_file = "rtp://225.0.0.10:5004"
#             player.open_video(video_file)
#             player.show()
#             form.hide()

#         elif self.cb.currentText() == "Fr2":
#             print(self.cb.currentText())
#             video_file = "rtp://225.0.0.54:20000"
#             player.open_video(video_file)
#             player.show()
#             form.hide()

#         else:
#             print("Chaine inconnue")

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     player = VideoPlayer()
#     form = combodemo()
#     form.show()
#     player.hide()
#     sys.exit(app.exec_())


class VideoPlayer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player")

        # Create a QVideoWidget to display the video
        self.video_widget = QVideoWidget()

        # Create a QMediaPlayer to play the video
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

        # Set the central widget to be the video widget
        self.setCentralWidget(self.video_widget)

    def open_video(self, video_file):
        """Open a video file and set it as the media for the media player."""
        url = QtCore.QUrl.fromUserInput(video_file)
        media = QMediaContent(url)
        self.media_player.setMedia(media)
        self.media_player.play()

class combodemo(QWidget):
    def __init__(self, parent=None):
        super(combodemo, self).__init__(parent)

        layout = QHBoxLayout()
        self.cb = QComboBox() #Création de la comboBox
        self.btn = QPushButton("Valider")
        self.cb.addItems(["BFM TV", "Fr2", "Fr3","Fr4","M6","Arte"]) # Ajouter une liste d'item    
        layout.addWidget(self.cb)
        layout.addWidget(self.btn)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")
        self.btn.clicked.connect(self.open_video)

    def open_video(self):

        if self.cb.currentText() == "BFM TV":
            print(self.cb.currentText())
            video_file = "rtp://225.0.0.51:20000"
            player.open_video(video_file)
            player.show()
            form.hide()

        elif self.cb.currentText() == "Fr2":
            print(self.cb.currentText())
            video_file = "rtp://225.0.0.54:20000"
            player.open_video(video_file)
            player.show()
            form.hide()

        else:
            print("Chaine inconnue")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    form = combodemo()
    form.show()
    player.hide()
    sys.exit(app.exec_())
