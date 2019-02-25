from model import Creature
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class View(object):
    def __init__(self, db):
        self.app = QApplication([])
        self.creature = Creature(db)
        self.creature.fetchTarget(0.5)
        label = QLabel('Hello world')
        label.show()
        self.app.exec_()



