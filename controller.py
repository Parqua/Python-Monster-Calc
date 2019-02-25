from model import Creature
from view import View
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Controller(object):
    def __init__(self):
        self.app = QApplication([])
        self.creature = Creature()
        self.view = View(self.app, self.creature)


