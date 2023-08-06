from PyQt5 import QtCore, QtGui, QtWidgets


class StartUI(object):
    def __init__(self):
        self.label = None
        self.pushButton = None
        self.centralwidget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(385, 178)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 381, 151))

        font = QtGui.QFont()
        font.setPointSize(23)

        self.pushButton.setFont(font)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(128, 128))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 150, 151, 21))
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyFactory编辑器 - 正在启动"))

        self.pushButton.setText(_translate("MainWindow", "PyFactory编辑器"))
        self.label.setText(_translate("MainWindow", "正在启动PyFactory编辑器"))
