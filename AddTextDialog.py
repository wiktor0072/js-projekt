# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addtext_dialog.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget, QSpinBox)

class Ui_AddTextDialog(QDialog):

    def __init__(self, window):
        super().__init__(window)
        self.setupUi(window)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(507, 301)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 488, 279))
        self.verticalLayout_main = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_font = QHBoxLayout()
        self.horizontalLayout_font.setObjectName(u"horizontalLayout_font")
        self.label_font = QLabel(self.verticalLayoutWidget)
        self.label_font.setObjectName(u"label_font")

        self.horizontalLayout_font.addWidget(self.label_font)

        self.comboBox_font = QComboBox(self.verticalLayoutWidget)
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.setObjectName(u"comboBox_font")

        self.horizontalLayout_font.addWidget(self.comboBox_font)


        self.verticalLayout_main.addLayout(self.horizontalLayout_font)

        self.horizontalLayout_size = QHBoxLayout()
        self.horizontalLayout_size.setObjectName(u"horizontalLayout_size")
        self.label_size = QLabel(self.verticalLayoutWidget)
        self.label_size.setObjectName(u"label_size")

        self.horizontalLayout_size.addWidget(self.label_size)

        self.spinBox_size = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_size.setObjectName(u"comboBox_size")

        self.horizontalLayout_size.addWidget(self.spinBox_size)


        self.verticalLayout_main.addLayout(self.horizontalLayout_size)

        self.horizontalLayout_color = QHBoxLayout()
        self.horizontalLayout_color.setObjectName(u"horizontalLayout_color")
        self.label_color = QLabel(self.verticalLayoutWidget)
        self.label_color.setObjectName(u"label_color")

        self.horizontalLayout_color.addWidget(self.label_color)

        self.radioButton_red = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_red.setObjectName(u"radioButton_red")
        icon = QIcon()
        icon.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/red.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_red.setIcon(icon)

        self.horizontalLayout_color.addWidget(self.radioButton_red)

        self.radioButton_orange = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_orange.setObjectName(u"radioButton_orange")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/range.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_orange.setIcon(icon1)

        self.horizontalLayout_color.addWidget(self.radioButton_orange)

        self.radioButton_yellow = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_yellow.setObjectName(u"radioButton_yellow")
        icon2 = QIcon()
        icon2.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/yellow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_yellow.setIcon(icon2)

        self.horizontalLayout_color.addWidget(self.radioButton_yellow)

        self.radioButton_green = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_green.setObjectName(u"radioButton_green")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_green.setIcon(icon3)

        self.horizontalLayout_color.addWidget(self.radioButton_green)

        self.radioButton_blue = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_blue.setObjectName(u"radioButton_blue")
        icon4 = QIcon()
        icon4.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_blue.setIcon(icon4)

        self.horizontalLayout_color.addWidget(self.radioButton_blue)

        self.radioButton_black = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_black.setObjectName(u"radioButton_black")
        icon5 = QIcon()
        icon5.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_black.setIcon(icon5)

        self.horizontalLayout_color.addWidget(self.radioButton_black)

        self.radioButton_white = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_white.setObjectName(u"radioButton_white")
        icon6 = QIcon()
        icon6.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/1200px-White_square_50%_transparency.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_white.setIcon(icon6)

        self.horizontalLayout_color.addWidget(self.radioButton_white)


        self.verticalLayout_main.addLayout(self.horizontalLayout_color)

        self.label_text = QLabel(self.verticalLayoutWidget)
        self.label_text.setObjectName(u"label_text")

        self.verticalLayout_main.addWidget(self.label_text)

        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_main.addWidget(self.textEdit)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_main.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(Dialog)
        self.setLayout(self.verticalLayout_main)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_font.setText(QCoreApplication.translate("Dialog", u"Font", None))
        self.comboBox_font.setItemText(0, QCoreApplication.translate("Dialog", u"Arial", None))
        self.comboBox_font.setItemText(1, QCoreApplication.translate("Dialog", u"Bodoni", None))
        self.comboBox_font.setItemText(2, QCoreApplication.translate("Dialog", u"Futura", None))
        self.comboBox_font.setItemText(3, QCoreApplication.translate("Dialog", u"Garamond", None))
        self.comboBox_font.setItemText(4, QCoreApplication.translate("Dialog", u"Rockwell", None))
        self.comboBox_font.setItemText(5, QCoreApplication.translate("Dialog", u"Times New Roman", None))
        self.comboBox_font.setItemText(6, QCoreApplication.translate("Dialog", u"Verdana", None))

        self.label_size.setText(QCoreApplication.translate("Dialog", u"Size", None))

        self.label_color.setText(QCoreApplication.translate("Dialog", u"Color ", None))
        self.radioButton_red.setText("")
        self.radioButton_orange.setText("")
        self.radioButton_yellow.setText("")
        self.radioButton_green.setText("")
        self.radioButton_blue.setText("")
        self.radioButton_black.setText("")
        self.radioButton_white.setText("")
        self.label_text.setText(QCoreApplication.translate("Dialog", u"Text", None))
    # retranslateUi



