from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys

class WebApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the QWebEngineView to display HTML content
        self.browser = QWebEngineView()

        # Simple HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Simple HTML in PyQt</title>
        </head>
        <body>
            <h1>Hello, PyQt6 WebEngine!</h1>
            <p>This is a simple HTML page rendered inside the PyQt window.</p>
        </body>
        </html>
        """

        # Set the HTML content in the browser
        self.browser.setHtml(html_content)

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