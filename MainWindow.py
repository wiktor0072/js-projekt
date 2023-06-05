# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PIL import Image, ImageQt
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QIcon,
                           QPainter,
                           QPixmap, QPen)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout,
                               QLabel, QMainWindow, QMenuBar, QPushButton,
                               QSizePolicy, QSlider, QStatusBar, QTabWidget,
                               QVBoxLayout, QWidget, QFileDialog, QDialog)

from AddTextDialog import Ui_AddTextDialog
from RescaleDialog import Ui_RescaleDialog
from picture import Picture
from SaveDialog import Ui_SaveDialog


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Project")
        MainWindow.setFixedSize(1027, 639)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(19, 59, 771, 511))
        self.horizontalLayout_pic = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_pic.setObjectName(u"horizontalLayout_pic")
        self.horizontalLayout_pic.setContentsMargins(0, 0, 0, 0)

        self.label_pic = QLabel(self.horizontalLayoutWidget)
        self.label_pic.setObjectName(u"label_pic")
        self.horizontalLayout_pic.addWidget(self.label_pic)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(818, 60, 191, 511))
        self.verticalLayout_options = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_options.setObjectName(u"verticalLayout_options")
        self.verticalLayout_options.setContentsMargins(0, 0, 0, 0)
        self.btn_load = QPushButton(self.verticalLayoutWidget)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.clicked.connect(self.load_image)

        self.verticalLayout_options.addWidget(self.btn_load)

        self.btn_save = QPushButton(self.verticalLayoutWidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.clicked.connect(self.save_image)

        self.verticalLayout_options.addWidget(self.btn_save)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_flip_btns = QHBoxLayout()
        self.horizontalLayout_flip_btns.setObjectName(u"horizontalLayout_flip_btns")
        self.btn_flip_left = QPushButton(self.verticalLayoutWidget)
        self.btn_flip_left.setObjectName(u"btn_flip_left")
        icon = QIcon()
        icon.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/1178621.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_flip_left.setIcon(icon)

        self.horizontalLayout_flip_btns.addWidget(self.btn_flip_left)

        self.btn_flip_right = QPushButton(self.verticalLayoutWidget)
        self.btn_flip_right.setObjectName(u"btn_flip_right")

        icon1 = QIcon()
        icon1.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/1178620.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_flip_right.setIcon(icon1)

        self.horizontalLayout_flip_btns.addWidget(self.btn_flip_right)

        self.verticalLayout_2.addLayout(self.horizontalLayout_flip_btns)

        self.verticalLayout_options.addLayout(self.verticalLayout_2)

        self.btn_flip_vertical = QPushButton(self.verticalLayoutWidget)
        self.btn_flip_vertical.setObjectName(u"btn_flip_vertical")
        icon2 = QIcon()
        iconThemeName = u"fds"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_flip_vertical.setIcon(icon2)

        self.verticalLayout_options.addWidget(self.btn_flip_vertical)

        self.label_contrast = QLabel(self.verticalLayoutWidget)
        self.label_contrast.setObjectName(u"label_contrast")

        self.verticalLayout_options.addWidget(self.label_contrast)

        self.slider_contrast = QSlider(self.verticalLayoutWidget)
        self.slider_contrast.setObjectName(u"slider_contrast")
        self.slider_contrast.setValue(49)
        self.slider_contrast.setOrientation(Qt.Horizontal)
        self.slider_contrast.setMinimum(0)
        self.slider_contrast.setMaximum(100)

        self.verticalLayout_options.addWidget(self.slider_contrast)

        self.label_brightness = QLabel(self.verticalLayoutWidget)
        self.label_brightness.setObjectName(u"label_brightness")

        self.verticalLayout_options.addWidget(self.label_brightness)

        self.slider_brightness = QSlider(self.verticalLayoutWidget)
        self.slider_brightness.setObjectName(u"slider_brightness")
        self.slider_brightness.setValue(49)
        self.slider_brightness.setOrientation(Qt.Horizontal)
        self.slider_brightness.setMinimum(0)
        self.slider_brightness.setMaximum(100)

        self.verticalLayout_options.addWidget(self.slider_brightness)

        self.horizontalLayout_fitler = QHBoxLayout()
        self.horizontalLayout_fitler.setObjectName(u"horizontalLayout_fitler")
        self.label_filter = QLabel(self.verticalLayoutWidget)
        self.label_filter.setObjectName(u"label_filter")

        self.horizontalLayout_fitler.addWidget(self.label_filter)

        self.comboBox_filter = QComboBox(self.verticalLayoutWidget)
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.addItem("")
        self.comboBox_filter.setObjectName(u"comboBox_filter")

        self.horizontalLayout_fitler.addWidget(self.comboBox_filter)


        self.verticalLayout_options.addLayout(self.horizontalLayout_fitler)

        self.btn_add_text = QPushButton(self.verticalLayoutWidget)
        self.btn_add_text.setObjectName(u"btn_add_text")
        self.btn_add_text.clicked.connect(self.add_text_init)

        self.verticalLayout_options.addWidget(self.btn_add_text)

        self.btn_crop = QPushButton(self.verticalLayoutWidget)
        self.btn_crop.setObjectName(u"btn_crop")
        self.btn_crop.clicked.connect(self.cropping_init)

        self.verticalLayout_options.addWidget(self.btn_crop)

        self.btn_scaling = QPushButton(self.verticalLayoutWidget)
        self.btn_scaling.setObjectName(u"btn_scaling")
        self.btn_scaling.clicked.connect(self.scaling_init)

        self.verticalLayout_options.addWidget(self.btn_scaling)

        self.btn_add_picture = QPushButton(self.verticalLayoutWidget)
        self.btn_add_picture.setObjectName(u"btn_add_picture")
        self.btn_add_picture.clicked.connect(self.add_picture_init)

        self.verticalLayout_options.addWidget(self.btn_add_picture)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 321, 41))
        self.gridLayout_upper = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_upper.setObjectName(u"gridLayout_upper")
        self.gridLayout_upper.setContentsMargins(0, 0, 0, 0)
        self.btn_undo = QPushButton(self.gridLayoutWidget)
        self.btn_undo.setObjectName(u"btn_undo")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_undo.setIcon(icon3)
        self.btn_undo.setDisabled(True)

        self.gridLayout_upper.addWidget(self.btn_undo, 0, 1, 1, 1)

        self.btn_redo = QPushButton(self.gridLayoutWidget)
        self.btn_redo.setObjectName(u"btn_redo")
        icon4 = QIcon()
        icon4.addFile(u"../../../../../Studia/Sem4/J\u0119zyki skryptowe/redo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_redo.setIcon(icon4)
        self.btn_redo.setDisabled(True)

        self.gridLayout_upper.addWidget(self.btn_redo, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1027, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.selection_rect = QRect()

        self.activate_widgets(False)
        self.show()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Project", u"Project", None))
        self.label_pic.setText("")
        self.btn_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_flip_left.setText("")
        self.btn_flip_right.setText("")
        self.btn_flip_vertical.setText(QCoreApplication.translate("MainWindow", u"Flip vertical", None))
        self.label_contrast.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.label_brightness.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.label_filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.comboBox_filter.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.comboBox_filter.setItemText(1, QCoreApplication.translate("MainWindow", u"Black-white", None))
        self.comboBox_filter.setItemText(2, QCoreApplication.translate("MainWindow", u"Sepia tone", None))
        self.comboBox_filter.setItemText(3, QCoreApplication.translate("MainWindow", u"Inverted", None))
        self.comboBox_filter.setItemText(4, QCoreApplication.translate("MainWindow", u"Sharpen", None))

        self.btn_add_text.setText(QCoreApplication.translate("MainWindow", u"Add text", None))
        self.btn_crop.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.btn_scaling.setText(QCoreApplication.translate("MainWindow", u"Scaling", None))
        self.btn_add_picture.setText(QCoreApplication.translate("MainWindow", u"Add picture", None))
        self.btn_undo.setText("")
        self.btn_redo.setText("")
    # retranslateUi




