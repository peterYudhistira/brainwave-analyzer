# Form implementation generated from reading ui file 'LoadingBar.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(311, 140)
        Form.setStyleSheet("QLabel{\n"
"    font: 18pt \"Bahnschrift SemiBold SemiConden\";\n"
"}")
        self.progressBar = QtWidgets.QProgressBar(parent=Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 110, 291, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loadubg = QtWidgets.QLabel(parent=Form)
        self.label_loadubg.setGeometry(QtCore.QRect(10, 40, 291, 31))
        self.label_loadubg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loadubg.setObjectName("label_loadubg")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(180, 30, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_loadubg.setText(_translate("Form", "Now Loading..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())