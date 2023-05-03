import random
import time
from PyQt6.QtWidgets import QWidget
from objects import (
    loadingbar as lb,
    mainwindow as mw
)
from PyQt6 import (
    QtCore,
    QtWidgets as qtw,
    QtCore as qtc,
    QtGui as qtg,
)


class LoadingThread(qtc.QThread):
    loadingBarSignal = qtc.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.is_running = True
        self.loadValue = 0

    def run(self):
        print("Starting load thread")
        while self.is_running:
            self.loadValue += random.randrange(0, 50) * 0.01
            time.sleep(0.01)
            self.loadingBarSignal.emit(self.loadValue)

    def stop(self):
        self.is_running = False
        print("Stopping load thread")
        self.terminate()


class LoadingWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        # set stuff here
        self.ui = lb.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Reading Your Mind....")
        self.setWindowIcon(qtg.QIcon("assets/images/feather.png"))


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        # set stuff here
        self.ui = mw.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Mind Reader")
        self.setWindowIcon(qtg.QIcon("assets/images/feather.png"))

        # connect stuff here
        self.ui.pushButton.clicked.connect(self.startLoading)

    def startLoading(self):
        print("entering loading thread")
        self.loadThread = LoadingThread()
        self.loadThread.start()
        self.loadThread.loadingBarSignal.connect(self.setProgress)
        self.lt = LoadingWindow()
        self.lt.show()

    def setProgress(self, counter):
        print(counter)
        self.lt.ui.progressBar.setValue(counter)
        self.setMessage(counter)

    def setMessage(self, counter):
        if 0 <= counter and counter <= 16:
            self.lt.ui.label_loadubg.setText("Accessing cortex...")
        elif 16 <= counter and counter <= 32:
            self.lt.ui.label_loadubg.setText("Remapping synapses...")
        elif 32 <= counter and counter <= 48:
            self.lt.ui.label_loadubg.setText("Recording neural activities...")
        elif 48 <= counter and counter <= 64:
            self.lt.ui.label_loadubg.setText("Fetching brain signals...")
        elif 64 <= counter and counter <= 80:
            self.lt.ui.label_loadubg.setText("Reconsidering career choices...")
        elif 80 <= counter and counter <= 96:
            self.lt.ui.label_loadubg.setText("Decoding thought data...")
        elif counter == 100:
            self.lt.ui.label_loadubg.setText("Reading Completed.")
            self.loadThread.stop()
            self.msgBox = qtw.QMessageBox()
            self.msgBox.setStandardButtons(qtw.QMessageBox.StandardButton.Ok)
            self.msgBox.setWindowTitle("WOW!!!!!!!!")
            self.msgBox.setWindowIcon(qtg.QIcon("assets/images/feather.png"))
            self.msgBox.setText("You are thinking of the number {}".format(self.ui.line_thincc.text()))
            self.msgBox.show()
            self.lt.destroy()


if __name__ == "__main__":
    app = qtw.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec()
