import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


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
        self.video_widget = QVideoWidget()
        print(self.cb.currentText())
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)
        video_file = r"C:\Users\snir\Desktop\Monpremierprojet.m4v"
        self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_file)))
        
        self.media_player.play()
        print("fin")


    

    # def selectionchange(self,i):
    #     print "Items in the list are :"
		
        # for count in range(self.cb.count()):
        #     print (self.cb.itemText(count))
        #     print ("Current index",i,"selection changed ",self.cb.currentText())
		
# def main():
#    app = QApplication(sys.argv)
#    ex = combodemo()
#    ex.show()
#    sys.exit(app.exec_())

# if __name__ == '__main__':
#    main()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication([])
    # Create and show the form
    form = combodemo()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()