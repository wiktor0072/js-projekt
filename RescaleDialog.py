# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rescale.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QIntValidator)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget, QMessageBox)


class Ui_RescaleDialog(QDialog):

    def __init__(self, window, image_size):
        super().__init__(window)
        self.setupUi(window, image_size)

    def setupUi(self, Dialog, image_size):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Rescale")
        Dialog.resize(447, 233)
        self.setWindowTitle('Rescale')
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 19, 411, 201))
        self.verticalLayout_main = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.label_size = QLabel(self.verticalLayoutWidget)
        self.label_size.setObjectName(u"label_size")

        self.verticalLayout_main.addWidget(self.label_size)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_x_curr = QLabel(self.verticalLayoutWidget)
        self.label_x_curr.setObjectName(u"label_x_curr")

        self.horizontalLayout.addWidget(self.label_x_curr)

        self.lineEdit_x_curr = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_x_curr.setObjectName(u"lineEdit_x_curr")
        self.lineEdit_x_curr.setReadOnly(True)
        self.lineEdit_x_curr.setText(str(image_size[0]))

        self.horizontalLayout.addWidget(self.lineEdit_x_curr)

        self.label_y_curr = QLabel(self.verticalLayoutWidget)
        self.label_y_curr.setObjectName(u"label_y_curr")

        self.horizontalLayout.addWidget(self.label_y_curr)

        self.lineEdit_y_curr = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_y_curr.setObjectName(u"lineEdit_y_curr")
        self.lineEdit_y_curr.setReadOnly(True)
        self.lineEdit_y_curr.setText(str(image_size[1]))

        self.horizontalLayout.addWidget(self.lineEdit_y_curr)


        self.verticalLayout_main.addLayout(self.horizontalLayout)

        self.label_provide = QLabel(self.verticalLayoutWidget)
        self.label_provide.setObjectName(u"label_provide")

        self.verticalLayout_main.addWidget(self.label_provide)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_x_from = QLabel(self.verticalLayoutWidget)
        self.label_x_from.setObjectName(u"label_x_from")

        self.horizontalLayout_2.addWidget(self.label_x_from)

        self.label_new_width = QLabel(self.verticalLayoutWidget)
        self.label_new_width.setObjectName(u"label_new_width")

        self.horizontalLayout_2.addWidget(self.label_new_width)

        self.lineEdit_new_width = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_new_width.setObjectName(u"lineEdit_new_width")

        self.horizontalLayout_2.addWidget(self.lineEdit_new_width)

        self.label_new_height = QLabel(self.verticalLayoutWidget)
        self.label_new_height.setObjectName(u"label_new_height")

        self.horizontalLayout_2.addWidget(self.label_new_height)

        self.lineEdit_new_height = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_new_height.setObjectName(u"lineEdit_new_height")

        self.horizontalLayout_2.addWidget(self.lineEdit_new_height)


        self.verticalLayout_main.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_main.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.validate_input)
        self.buttonBox.rejected.connect(self.reject)

        self.validator = QIntValidator()
        self.lineEdit_new_width.setValidator(self.validator)
        self.lineEdit_new_height.setValidator(self.validator)

        QMetaObject.connectSlotsByName(Dialog)
        self.setLayout(self.verticalLayout_main)
    # setupUi


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_size.setText(QCoreApplication.translate("Dialog", u"Picture size", None))
        self.label_x_curr.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.label_y_curr.setText(QCoreApplication.translate("Dialog", u"y", None))
        self.label_provide.setText(QCoreApplication.translate("Dialog", u"Provide values to resize", None))
        self.label_x_from.setText("")
        self.label_new_width.setText(QCoreApplication.translate("Dialog", u"New width", None))
        self.label_new_height.setText(QCoreApplication.translate("Dialog", u"New height", None))
    # retranslateUi

    def validate_input(self):
        if int(self.lineEdit_new_width.text()) <= 0 or int(self.lineEdit_new_height.text()) <= 0:
            QMessageBox.warning(self, 'Error', 'Width and height have to positive numbers')
        else:
            self.accept()

    def get_parameters(self):
        return self.lineEdit_new_width.text(), self.lineEdit_new_height.text()

