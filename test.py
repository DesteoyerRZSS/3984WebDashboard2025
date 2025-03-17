import sys
import os
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl 

from flask import Flask, render_template_string, request
from networktables import NetworkTables
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Window")
        self.setGeometry(100, 100, 800, 600)
        label = QLabel("Hello, PyQt6!", self)
        label.setGeometry(100, 100, 200, 100)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()