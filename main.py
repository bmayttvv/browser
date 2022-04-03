from PyQt5 import QtWidgets, QtCore
from components import tab, titleBar, webPage
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from BrowserUi import Ui_Form
import sys

# YOUR APPLICATION
class Browserapp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Browserapp, self).__init__()
        self.setupUi(self)
        self.tBar = titleBar.TitleBar(self)
        self.verticalLayout.addWidget(self.tBar)
        tabB = tab.Tab()
        self.tBar.insertTab(tabB)
        page = webPage.WebPage()
        self.verticalLayout.addWidget(page)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    From = Browserapp()
    From.show()
    sys.exit(app.exec_())
