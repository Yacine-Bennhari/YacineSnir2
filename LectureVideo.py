import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player")

        # Create a QVideoWidget to display the video
        self.video_widget = QVideoWidget()

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
        self.play_button = self.toolbar.addAction("Play")
        self.play_button.triggered.connect(self.play_video)
        self.stop_button = self.toolbar.addAction("Stop")
        self.stop_button.triggered.connect(self.stop_video)

        # Set the central widget to be the video widget
        self.setCentralWidget(self.video_widget)

    def open_video(self):
        """Open a video file and set it as the media for the media player."""
        if self.file_dialog.exec_():
            video_file = self.file_dialog.selectedFiles()[0]
            self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_file)))

    def play_video(self):
        """Start playing the current video."""
        self.media_player.play()

    def stop_video(self):
        """Stop playing the current video."""
        self.media_player.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
