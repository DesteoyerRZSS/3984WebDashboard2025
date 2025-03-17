from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys

class WebApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the QWebEngineView to display HTML content
        self.browser = QWebEngineView()

        # Load a simple webpage
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Set the browser as the central widget of the window
        self.setCentralWidget(self.browser)

        # Set the window title
        self.setWindowTitle("PyQt6 WebEngine Example")

        # Set the window size
        self.resize(800, 600)

# Main entry point for the application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the web app window
    window = WebApp()
    window.show()

    # Start the application event loop
    sys.exit(app.exec())