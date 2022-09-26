#webbrowser
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()  #to see full screen

        #navbar
        navbar = QToolBar() #create a navbar
        self.addToolBar(navbar) #add navbar to browser

        back_btn = QAction('Back', self) #back btn with action
        back_btn.triggered.connect(self.browser.back) #when is trigger(click on it, it connect to the browser back)
        navbar.addAction(back_btn) #tell navbar to add the action

        forward_btn = QAction('Forward', self)  # Forward btn with action
        forward_btn.triggered.connect(self.browser.forward)  # when is trigger(click on it, it connect to the browser back)
        navbar.addAction(forward_btn)  # tell navbar to add the action

        reload_btn = QAction('Reload', self)  # Forward btn with action
        reload_btn.triggered.connect(self.browser.reload)  # when is trigger(click on it, it connect to the browser back)
        navbar.addAction(reload_btn)  # tell navbar to add the action

        home_btn = QAction('Home', self)  # Forward btn with action
        home_btn.triggered.connect(self.navigate_home)  # when is trigger(click on it, navigate to this page)
        navbar.addAction(home_btn)  # tell navbar to add the action

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)#here we are calling the browser-> if something change
        #you have to connect to update url method and update



    def navigate_home(self):
            self.browser.setUrl(QUrl('http:youtube.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())






app = QApplication(sys.argv)
QApplication.setApplicationName('SpazS Browser')
window = MainWindow()
app.exec()





