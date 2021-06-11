from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from . resources_rc import *


class TestButton(QPushButton):
    def __init__(self, ob_class = None):
        super().__init__(ob_class)  #super() = QPushButton
        #QPushButton(ob_class)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
     
        
        #font  //設定字形
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        #font  //設定字形
          
        self.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 45))
        self.setFont(font)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setLayoutDirection(Qt.LeftToRight)
        self.setStyleSheet(u"QPushButton {	\n"
                            "background-position: left center;\n"
                            "background-repeat: no-repeat;\n"
                            "border: none;\n"
                            "border-left: 22px solid transparent;\n"
                            "background-color: transparent;\n"
                            "text-align: left;\n"
                            "padding-left: 44px;\n"
                            "}\n"
                            "QPushButton:hover {\n"
                            "background-color: rgb(40, 44, 52);\n"
                            "}\n"
                            "QPushButton:pressed {	\n"
                            "background-color: rgb(189, 147, 249);\n"
                            "color: rgb(255, 255, 255);\n"
                            "}\n"
                            "QPushButton {	\n"
                            "background-position: left center;\n"
                            "background-repeat: no-repeat;\n"
                            "border: none;\n"
                            "border-left: 20px solid transparent;\n"
                            "background-color:transparent;\n"
                            "text-align: left;\n"
                            "padding-left: 44px;\n"
                            "}\n"
                            "QPushButton:hover {\n"
                            "background-color: rgb(40, 44, 52);\n"
                            "}\n"
                            "QPushButton:pressed {	\n"
                            "background-color: rgb(189, 147, 249);\n"
                            "color: rgb(255, 255, 255);\n"
                            "}\n"
                            )

