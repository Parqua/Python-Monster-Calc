from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from configparser import ConfigParser

class View(object):
    def __init__(self, app, creature):
        self.app = app
        self.creature = creature
        label = QLabel('Hello world')
        label.show()
        app.exec_()


