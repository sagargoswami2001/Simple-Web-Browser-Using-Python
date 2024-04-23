import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os


class MainWindow(QMainWindow):
    def __init__(self):
        #init browser and window
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #get current directory
        try:
            self.savedurl = 'http://google.com'
            self.dir = os.getcwd()
            self.savepath = os.path.join(self.dir, 'Web_saves\\Full_Settings.txt')
        except:
            self.savedurl = 'http://google.com'
            self.dir = os.getcwd()
            self.savepath = os.path.join(self.dir, 'Web_saves/Full_Settings.txt')

        #add toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        #make buttons
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        start_btn = QAction('Start', self)
        start_btn.triggered.connect(lambda: self.load_url(c=4))
        navbar.addAction(start_btn)

        search_btn = QAction('Search', self)
        search_btn.triggered.connect(lambda: self.load_url(c=5))
        navbar.addAction(search_btn)

        home_btn = QAction('Creator', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        save_btn_1 = QAction('As Bookmark 1', self)
        save_btn_1.triggered.connect(lambda: self.save_url(c=1))
        save_btn_2 = QAction('As Bookmark 2', self)
        save_btn_2.triggered.connect(lambda: self.save_url(c=2))
        save_btn_3 = QAction('As Bookmark 3', self)
        save_btn_3.triggered.connect(lambda: self.save_url(c=3))
        startset_btn = QAction('As Start', self)
        startset_btn.triggered.connect(lambda: self.save_url(c=4))
        searchset_btn = QAction('As Search', self)
        searchset_btn.triggered.connect(lambda: self.save_url(c=5))

        load_btn_1 = QAction('Load Bookmark 1', self)
        load_btn_1.triggered.connect(lambda: self.load_url(c=1))
        load_btn_2 = QAction('Load Bookmark 2', self)
        load_btn_2.triggered.connect(lambda: self.load_url(c=2))
        load_btn_3 = QAction('Load Bookmark 3', self)
        load_btn_3.triggered.connect(lambda: self.load_url(c=3))

        #add bookmark menu
        Save_File_Menu = self.menuBar()
        Save_File_Save = Save_File_Menu.addMenu("Save Page")
        Save_File_Save.addAction(save_btn_1)
        Save_File_Save.addAction(save_btn_2)
        Save_File_Save.addAction(save_btn_3)
        Save_File_Save.addAction(startset_btn)
        Save_File_Save.addAction(searchset_btn)

        Save_File_Load = Save_File_Menu.addMenu("Load Bookmark")
        Save_File_Load.addAction(load_btn_1)
        Save_File_Load.addAction(load_btn_2)
        Save_File_Load.addAction(load_btn_3)

        #add the search bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        #setup browser for start
        self.browser.urlChanged.connect(self.update_url)
        self.load_url(c=4, seturl=True)


    def navigate_home(self):
        """Sets Url to Creators GitHub"""
        self.browser.setUrl(QUrl('https://github.com/sagargoswami2001'))

    def navigate_to_url(self):
        """Sets Url to the clicked link"""
        url = self.url_bar.text()
        self.savedurl = url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        """Sets Url to the entered text string"""
        self.savedurl = q.toString()
        self.url_bar.setText(q.toString())

    def save_url(self, c=3):
        """Saves Url to txt file"""
        with open(self.savepath, "r") as f:
            lines = f.readlines()
        with open(self.savepath, "w") as f:
            for number, line in enumerate(lines):
                if number ==(c):
                    f.write(self.savedurl + '\n')
                else:
                    f.write(line)


    def load_url(self, c=3, seturl=False):
        """Loads Url from txt file"""
        with open(self.savepath, 'r') as f:
            for i in range(c):
                f.readline()
            c=f.readline()
            c=c.rstrip('\n')
            self.browser.setUrl(QUrl(c))
            if seturl:
                self.savedurl = c

        

            



app = QApplication(sys.argv)
QApplication.setApplicationName("Sagar's Browser")
window = MainWindow()
app.exec_()
