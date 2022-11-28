from PySide6 import QtWidgets

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)
        self.setWindowTitle("Video_calculate")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.radioBt_activer = QtWidgets.QRadioButton("Durée")
        self.radioBt_desactiver = QtWidgets.QRadioButton("HDD")

        self.lbl_taille = QtWidgets.QLabel("Taille")
        self.LEdit_taille = QtWidgets.QLineEdit()
        self.LEdit_taille.setPlaceholderText("Saisir votre Taille")
        

        self.lbl_ips = QtWidgets.QLabel("ips")
        self.LEdit_ips= QtWidgets.QLineEdit()
        self.LEdit_ips.setPlaceholderText("Saisir votre ips")

        self.lbl_Hdd = QtWidgets.QLabel("Hdd")
        self.LEdit_Hdd = QtWidgets.QLineEdit()
        self.LEdit_Hdd.setPlaceholderText("Saisir votre Hdd")

        self.lbl_duree = QtWidgets.QLabel("Durée")
        self.LEdit_duree = QtWidgets.QLineEdit()
        
        self.lbl_Jour = QtWidgets.QLabel("Jour")
        self.LEdit_Jour = QtWidgets.QLineEdit()

        self.lbl_Heure = QtWidgets.QLabel("Heures")
        self.LEdit_Heure = QtWidgets.QLineEdit()

        self.lbl_minute = QtWidgets.QLabel("Minutes")
        self.LEdit_minute = QtWidgets.QLineEdit()

        self.lbl_seconde = QtWidgets.QLabel("Secondes")
        self.LEdit_seconde = QtWidgets.QLineEdit()


        self.btn_Calculer = QtWidgets.QPushButton("Calculer")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")
        self.radioBt_desactiver.setChecked(True)
        # self.LEdit_Hdd.setDisabled(True)

    def addWigets_to_layouts(self):

        self.layoutH0.addWidget(self.radioBt_activer)
        self.layoutH0.addWidget(self.radioBt_desactiver)

        self.layoutH1.addWidget(self.lbl_taille)
        self.layoutH1.addWidget(self.LEdit_taille)

        self.layoutH2.addWidget(self.lbl_ips)
        self.layoutH2.addWidget(self.LEdit_ips)

        self.layoutH3.addWidget(self.lbl_Hdd)
        self.layoutH3.addWidget(self.LEdit_Hdd)

        self.layoutH4.addWidget(self.lbl_duree)
        self.layoutH4.addWidget(self.LEdit_duree)

        self.layoutH4.addWidget(self.lbl_Jour)
        self.layoutH4.addWidget(self.LEdit_Jour)

        self.layoutH4.addWidget(self.lbl_Heure)
        self.layoutH4.addWidget(self.LEdit_Heure)

        self.layoutH4.addWidget(self.lbl_minute)
        self.layoutH4.addWidget(self.LEdit_minute)

        self.layoutH4.addWidget(self.lbl_seconde)
        self.layoutH4.addWidget(self.LEdit_seconde)

        self.layoutH5.addWidget(self.btn_Calculer)
        self.layoutH5.addWidget(self.btn_Quitter)

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)

    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.radioBt_activer.clicked.connect(self.activer)
        self.radioBt_desactiver.clicked.connect(self.desactiver)
        self.btn_Calculer.clicked.connect(self.calculer)

    def calcule1(self):
            try:
                taille = float(self.LEdit_taille.text())
                ips = float(self.LEdit_ips.text())
                duree = float(self.LEdit_duree.text())
                
                print(taille,"***",ips,"***",Hdd)
                
            except:
                pass

            else:
                calcul_hdd = (taille*ips*duree/(1024*1024)
                self.LEdit_Hdd.setText(str(calcul_hdd))
                print(calcul_hdd)

    def calcule2(self):
                try:
                    taille = float(self.LEdit_taille.text())
                    ips = float(self.LEdit_ips.text())
                    duree = float(self.LEdit_duree.text())
                
                    print(taille,"***",ips,"***",Hdd)
                
                except:
                    pass

                else:
                    calcul_temps = (taille*ips*duree/(1024*1024)
                    self.LEdit_duree.setText(str(calcul_hdd))
                    print(calcul_temps)


    def activer(self):
        if self.radioBt_activer.isChecked():
            print("Activer")
            self.LEdit_HDD.setDisabled(False)


    def desactiver(self):
        if self.radioBt_desactiver.isChecked():
            print("Désactiver")
            self.LEdit_HDD.setDisabled(True)



app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()