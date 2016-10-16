__author__ = 'Vit'

from PyQt5 import QtCore
from PyQt5.QtGui import QGuiApplication, QCursor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap, QIcon, QKeySequence
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *

from view.qt_ui.bn_view_ui import Ui_ButtonView


class MainView(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # self.buttons=list()
        self.desktop = QApplication.desktop().screenGeometry()
        self.child_access = True

        self.make_view()
        self.setup_directories()
        self.keyboard_mapping()
        self.make_cursors()

        self.show_buttons_page()

        self.setWindowState(QtCore.Qt.WindowNoState)
        self.show()

        self.connect_button(self.ui.bn_1, 'Антошка.mp4', 'antoshka1.jpg')
        self.connect_button(self.ui.bn_2, 'Два весёлых гуся_(480p).mp4', 'gusi1.jpg')
        self.connect_button(self.ui.bn_3, 'Колобок_(720p).mp4', 'kolobok1.jpg')
        self.connect_button(self.ui.bn_4, 'Бременские музыканты (480p).mp4', 'bm1.jpg')

        self.setWindowState(QtCore.Qt.WindowFullScreen)

    def make_view(self):
        self.ui = Ui_ButtonView()
        self.ui.setupUi(self)
        self.ui.statusbar.hide()

        self.setGeometry(QtCore.QRect(self.desktop.width() * 5 // 100, self.desktop.height() * 5 // 100,
                                      self.desktop.width() * 90 // 100, self.desktop.height() * 90 // 100))

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player_widget = QVideoWidget(self.ui.frame_player)
        self.ui.frame_player_layout.addWidget(self.media_player_widget)
        self.media_player.setVideoOutput(self.media_player_widget)

    def setup_directories(self):
        self.video_dir = 'Z:\\Фильмы\\Анимация\\Русские\\Вике\\'
        self.pix_dir = 'view\\files\\'

    def keyboard_mapping(self):
        quit = QAction('Quit', self)
        quit.setShortcut(QKeySequence('Ctrl+`'))
        self.addAction(quit)
        quit.triggered.connect(self.parent_access)

        self._key_disable(Qt.Key_Space)
        self._key_disable(Qt.Key_Space + Qt.SHIFT)
        self._key_disable(Qt.Key_Space + Qt.ALT)
        self._key_disable(Qt.Key_Space + Qt.CTRL)

    def _key_disable(self, key):
        sp = QAction('Noname', self)
        sp.setShortcut(QKeySequence(key))
        self.addAction(sp)
        sp.triggered.connect(lambda: None)

    def make_cursors(self):
        self.cursor_big = QCursor(QPixmap('view/files/hand-icon.png'), 89, 30)
        self.cursor_hide = QCursor(Qt.BlankCursor)

    def connect_button(self, button, filename, pix_filename=''):
        button.clicked.connect(lambda: self.play_mult(filename))

        pixmap = QPixmap(self.pix_dir + pix_filename)
        icon = QIcon()
        icon.addPixmap(pixmap, QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(button.size())
        # self.buttons.append(dict(button=button,media=filename,icon=icon,picture=pix_filename))

    def show_buttons_page(self):
        self.media_player.stop()
        self.ui.frame_player.hide()
        self.ui.frame_bn.show()
        self.show_cursor(self.cursor_big)

    def show_cursor(self, cursor):
        if self.child_access:
            QGuiApplication.restoreOverrideCursor()
            QGuiApplication.setOverrideCursor(cursor)
        else:
            QGuiApplication.restoreOverrideCursor()

    def play_mult(self, mult):
        self.ui.frame_player.show()
        self.ui.frame_bn.hide()
        self.show_cursor(self.cursor_hide)
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_dir + mult)))
        self.media_player.play()

    def mousePressEvent(self, *args, **kwargs):
        self.show_buttons_page()

    def parent_access(self):
        if self.windowState() == QtCore.Qt.WindowNoState:
            self.setWindowState(QtCore.Qt.WindowFullScreen)
            self.child_access = True
            self.show_buttons_page()
        else:
            self.setWindowState(QtCore.Qt.WindowNoState)
            QGuiApplication.restoreOverrideCursor()
            self.child_access = False
            self.show_buttons_page()

if __name__ == "__main__":

        import sys,os
        os.chdir('..')
        app = QApplication(sys.argv)
        view=MainView()
        sys.exit(app.exec_())


