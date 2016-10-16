__author__ = 'Vit'

if __name__ == "__main__":

        import os

        interfaces=['bn_view_ui']

        base_dir='E:/Dropbox/Hobby/PRG/PyWork/vika_player'
        source_dir=base_dir+'/view/ui/'
        dest_dir=base_dir+'/view/qt_ui/'

        pyuic5='C:/Python34/Lib/site-packages/PyQt5/pyuic5.bat '

        for fname in interfaces:
            source=source_dir+fname+'.ui'
            dest=dest_dir+fname+'.py'
            command=pyuic5+source+' -o '+dest
            print(command)
            os.system(command)

        from view.main import MainView
        from PyQt5.QtWidgets import QApplication
        import sys

        app = QApplication(sys.argv)
        view=MainView()
        sys.exit(app.exec_())

