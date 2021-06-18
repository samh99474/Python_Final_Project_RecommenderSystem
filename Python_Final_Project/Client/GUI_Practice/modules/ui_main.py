# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingnxZcz.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *
from modules.TestButton import TestButton

#from modules.ui_functions import UIFunctions

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #第一區塊
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))

        #設定APP風格
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")

        #font  //設定字形
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        #font  //設定字形

        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        
        #設定APP風格

        #appMargins
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        #appMargins

        #bgApp
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        #bgApp

        #appLayout
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        #appLayout

        #leftMenuBg
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        #leftMenuBg

        #verticalLayout_3
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        #verticalLayout_3

        #topLogoInfo
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        #topLogoInfo

        #topLogo
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        #topLogo

        #titleLeftApp
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        #titleLeftApp

        #font1
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        #font1

        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))

        #font2
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        #font2


        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        #leftMenuFrame
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        #leftMenuFrame

        #verticalMenuLayout
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        #verticalMenuLayout

        #toggleBox
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        #toggleBox

        #verticalLayout_4
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        #verticalLayout_4

        #三條槓
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)
        #三條槓


        self.verticalMenuLayout.addWidget(self.toggleBox)



        #leftMenuFrame
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        
        

        #menu的GUI

        #btn
        """
        #測試用class包裝
        self.btn_test = TestButton(self.topMenu)
        self.verticalLayout_8.addWidget(self.btn_test)


        self.btn_test3 = QPushButton(self.topMenu)
        self.verticalLayout_8.addWidget(self.btn_test3)
        """

        #btn_home
        #self.btn_home = TestButton(self.topMenu)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")
        
        self.verticalLayout_8.addWidget(self.btn_home)
        #btn_home
        
        


        #btn_new
        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)
        #btn_new

        #btn_save
        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)
        #btn_save

        #btn_exit
        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)
        #btn_exit
        #menu的GUI
        #btn
        
        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)


        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)

         
        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.appLayout.addWidget(self.leftMenuBg)


        #icon
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        #icon


        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)

        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)

        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())

        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        #contentBottom
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        #contentBottom

        #verticalLayout_6
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        #verticalLayout_6

        #content
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        #content

        #horizontalLayout_4
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        #horizontalLayout_4

        #pagesContainer
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        #pagesContainer

        #verticalLayout_15
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        #verticalLayout_15

        #stackedWidget
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        #stackedWidget

        #home的GUI
        self.home = QWidget()
        self.home.setObjectName(u"home")
#         self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
# "background-position: center;\n"
# "background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)

        
        #用垂直的排列
        self.verticalLayout_home = QVBoxLayout(self.home)
        self.verticalLayout_home.setObjectName(u"verticalLayout_home")
        #用垂直的排列


        #row_home
        
        #第一個row
        self.row_home = QFrame(self.home)
        self.row_home.setObjectName(u"row_home")
        self.row_home.setMinimumSize(QSize(0, 150))
        self.row_home.setFrameShape(QFrame.StyledPanel)
        self.row_home.setFrameShadow(QFrame.Raised)
        #第一個row

        #用水平的排列
        self.horizontalLayout_home = QHBoxLayout(self.row_home)
        self.horizontalLayout_home.setSpacing(0)
        self.horizontalLayout_home.setObjectName(u"horizontalLayout_home")
        self.horizontalLayout_home.setContentsMargins(0, 0, 0, 0)
        #用水平的排列


        #tableWidget_home
        self.tableWidget_home = QTableWidget(self.row_home)  #表格
        #設定col的數目
        if (self.tableWidget_home.columnCount() < 2):
            self.tableWidget_home.setColumnCount(2)
        #設定col的數目

        """
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_home.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        """

        #設定row的數目
        #print("self.tableWidget_home.rowCount() : {}".format(self.tableWidget_home.rowCount()))
        if (self.tableWidget_home.rowCount() < 20):
            self.tableWidget_home.setRowCount(20)
        #設定row的數目

        """
        font_test = QFont()
        font_test.setFamily(u"Segoe UI")
        
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font_test);
        self.tableWidget_home.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(14, __qtablewidgetitem18)
        
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_home.setVerticalHeaderItem(15, __qtablewidgetitem19)


        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_home.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_home.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_home.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_home.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget_home.setObjectName(u"tableWidget_home")
        sizePolicy_test = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy_test.setHorizontalStretch(0)
        sizePolicy_test.setVerticalStretch(0)
        sizePolicy_test.setHeightForWidth(self.tableWidget_home.sizePolicy().hasHeightForWidth())
        self.tableWidget_home.setSizePolicy(sizePolicy_test)
        """

        #設定顏色
        palette_home = QPalette()  #調色盤
        #QColor(R, G, B, lightness)  //lightness : 數字愈大愈亮
        #QBrush  //設定筆刷
        brush_home = QBrush(QColor(221, 221, 221, 255))  #設定筆刷顏色
        brush_home.setStyle(Qt.SolidPattern)  #背景圖案
        palette_home.setBrush(QPalette.Inactive, QPalette.WindowText, brush_home)  #設定背景文字顏色

        brush_home1 = QBrush(QColor(0, 0, 0, 0))
        brush_home1.setStyle(Qt.SolidPattern)
        palette_home.setBrush(QPalette.Active, QPalette.Button, brush_home1)  #設定button外框顏色
        palette_home.setBrush(QPalette.Active, QPalette.Text, brush_home)  #設定背景文字顏色
        palette_home.setBrush(QPalette.Active, QPalette.ButtonText, brush_home)  #設定button的文字顏色

        brush_home2 = QBrush(QColor(0, 0, 0, 255))
        brush_home2.setStyle(Qt.NoBrush)
        palette_home.setBrush(QPalette.Active, QPalette.Base, brush_home2)  #設定框內背景顏色
        palette_home.setBrush(QPalette.Active, QPalette.Window, brush_home1)  #設定背景顏色

#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette_home.setBrush(QPalette.Active, QPalette.PlaceholderText, brush_home)
#endif
        palette_home.setBrush(QPalette.Inactive, QPalette.WindowText, brush_home)
        palette_home.setBrush(QPalette.Inactive, QPalette.Button, brush_home1)
        palette_home.setBrush(QPalette.Inactive, QPalette.Text, brush_home)
        palette_home.setBrush(QPalette.Inactive, QPalette.ButtonText, brush_home)

        brush_home3 = QBrush(QColor(0, 0, 0, 255))
        brush_home3.setStyle(Qt.NoBrush)
        palette_home.setBrush(QPalette.Inactive, QPalette.Base, brush_home3)
        palette_home.setBrush(QPalette.Inactive, QPalette.Window, brush_home1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette_home.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush_home)
#endif
        palette_home.setBrush(QPalette.Disabled, QPalette.WindowText, brush_home)
        palette_home.setBrush(QPalette.Disabled, QPalette.Button, brush_home1)
        palette_home.setBrush(QPalette.Disabled, QPalette.Text, brush_home)
        palette_home.setBrush(QPalette.Disabled, QPalette.ButtonText, brush_home)

        brush_home4 = QBrush(QColor(0, 0, 0, 255))
        brush_home4.setStyle(Qt.NoBrush)
        palette_home.setBrush(QPalette.Disabled, QPalette.Base, brush_home4)
        palette_home.setBrush(QPalette.Disabled, QPalette.Window, brush_home1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette_home.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush_home)
#endif
        #設定顏色
        
        #設定tableWidget_home
        self.tableWidget_home.setPalette(palette_home)
        self.tableWidget_home.setFrameShape(QFrame.NoFrame)
        self.tableWidget_home.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_home.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_home.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_home.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_home.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_home.setShowGrid(True)
        self.tableWidget_home.setGridStyle(Qt.SolidLine)
        self.tableWidget_home.setSortingEnabled(False)
        self.tableWidget_home.horizontalHeader().setVisible(False)
        self.tableWidget_home.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_home.horizontalHeader().setDefaultSectionSize(100)  #設定第一個col的寬度
        self.tableWidget_home.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_home.verticalHeader().setVisible(False)
        self.tableWidget_home.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_home.verticalHeader().setDefaultSectionSize(100)  #設定每個row的寬度
        self.tableWidget_home.verticalHeader().setHighlightSections(False)
        self.tableWidget_home.verticalHeader().setStretchLastSection(True)
        #設定tableWidget_home
        
        self.horizontalLayout_home.addWidget(self.tableWidget_home)
        #tableWidget_home
        

        self.verticalLayout_home.addWidget(self.row_home)
        
        #row_home
        #home的GUI


        #new_page的GUI
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")

        self.verticalLayout_NP = QVBoxLayout(self.new_page)
        self.verticalLayout_NP.setObjectName(u"verticalLayout_NP")

        
        #設定row_NP
        self.row_NP = QFrame(self.new_page)
        self.row_NP.setObjectName(u"row_NP")
        self.row_NP.setMinimumSize(QSize(400, 150))
        self.row_NP.setFrameShape(QFrame.StyledPanel)
        self.row_NP.setFrameShadow(QFrame.Raised)
        #設定row_NP

        #用垂直的排列
        self.verticalLayout_NP2 = QVBoxLayout(self.row_NP)
        self.verticalLayout_NP2.setObjectName(u"verticalLayout_NP2")
        #用垂直的排列

        #新增gridLayout_NP
        self.gridLayout_NP = QGridLayout()
        self.gridLayout_NP.setObjectName(u"gridLayout_NP")
        #新增gridLayout_NP


        #新增label_video
        self.label_video = QLabel(self.row_NP)
        self.label_video.setObjectName(u"label_video")
        self.label_video.setAlignment(Qt.AlignCenter)
        self.label_video.setText(QCoreApplication.translate("MainWindow", u"SHOW VIDEO", None))

        self.gridLayout_NP.addWidget(self.label_video, 0, 0, 2, 2)
        #新增label_video

        #新增label_status

        #設定scrollArea_status
        self.scrollArea_status = QScrollArea(self.row_NP)
        self.scrollArea_status.setObjectName(u"scrollArea_status")
        self.scrollArea_status.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea_status.setFrameShape(QFrame.NoFrame)
        self.scrollArea_status.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_status.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_status.setWidgetResizable(True)
        self.scrollArea_status.setStyleSheet(u" QScrollBar:vertical {\n"
                                                "background: rgb(52, 59, 72);\n"  #scroll bar的背景顏色
                                                "}\n"
                                                " QScrollBar:horizontal {\n"
                                                "    background: rgb(52, 59, 72);\n"
                                                " }\n"
                                                "QScrollArea{\n"  #QScrollArea的背景顏色
                                                "background: rgb(33, 37, 43);"
                                                "border-radius: 10px;\n"
                                                "}\n"
                                                )
        #設定scrollArea_NP

        #設定scrollArea_WidgetContents_status
        self.scrollArea_WidgetContents_status = QWidget()
        self.scrollArea_WidgetContents_status.setObjectName(u"scrollArea_WidgetContents_status")
        self.scrollArea_WidgetContents_status.setGeometry(QRect(0, 0, 218, 218))
        self.scrollArea_WidgetContents_status.setStyleSheet(u" QScrollBar:vertical {\n"
                                                                "	border: none;\n"
                                                                "    background: rgb(52, 59, 72);\n"
                                                                "    width: 14px;\n"
                                                                "    margin: 21px 0 21px 0;\n"
                                                                "	border-radius: 0px;\n"
                                                                " }")
        #原本顏色為background: rgb(52, 59, 72)
        #設定scrollArea_WidgetContents_status

        self.horizontalLayout_status = QHBoxLayout(self.scrollArea_WidgetContents_status)
        self.horizontalLayout_status.setObjectName(u"horizontalLayout_status")

        self.label_status = QLabel(self.scrollArea_WidgetContents_status)
        self.label_status.setObjectName(u"label_video")
        self.label_status.setAlignment(Qt.AlignCenter)
        self.label_status.setMinimumSize(QSize(700, 200))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"SHOW STATUS", None))
        self.horizontalLayout_status.addWidget(self.label_status)

        self.scrollArea_status.setWidget(self.scrollArea_WidgetContents_status)

        self.gridLayout_NP.addWidget(self.scrollArea_status, 2, 0, 1, 2)
        #新增label_status

        #新增label_intro
        #設定scrollArea_intro
        self.scrollArea_intro = QScrollArea(self.row_NP)
        self.scrollArea_intro.setObjectName(u"scrollArea_intro")
        self.scrollArea_intro.setStyleSheet(u" QScrollBar:vertical {\n"
                                                "background: rgb(52, 59, 72);\n"  #scroll bar的背景顏色
                                                "}\n"
                                                " QScrollBar:horizontal {\n"
                                                "    background: rgb(52, 59, 72);\n"
                                                " }\n"
                                                "QScrollArea{\n"  #QScrollArea的背景顏色
                                                "background: rgb(33, 37, 43);"
                                                "border-radius: 10px;\n"
                                                "}\n"
                                                )

        self.scrollArea_intro.setFrameShape(QFrame.NoFrame)
        self.scrollArea_intro.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_intro.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_intro.setWidgetResizable(True)
        #設定scrollArea_intro

        #設定scrollArea_WidgetContents_intro
        self.scrollArea_WidgetContents_intro = QWidget()
        self.scrollArea_WidgetContents_intro.setObjectName(u"scrollArea_WidgetContents_intro")
        self.scrollArea_WidgetContents_intro.setGeometry(QRect(0, 0, 218, 218))
        self.scrollArea_WidgetContents_intro.setStyleSheet(u" QScrollBar:vertical {\n"
                                                                "	border: none;\n"
                                                                "    background: rgb(0, 0, 0);\n"
                                                                "    width: 14px;\n"
                                                                "    margin: 21px 0 21px 0;\n"
                                                                "	border-radius: 0px;\n"
                                                                " }")
        #原本顏色為background: rgb(52, 59, 72)
        #設定scrollArea_WidgetContents_intro

        self.horizontalLayout_intro = QHBoxLayout(self.scrollArea_WidgetContents_intro)
        self.horizontalLayout_intro.setObjectName(u"horizontalLayout_intro")


        self.label_intro = QLabel(self.scrollArea_WidgetContents_intro)
        self.label_intro.setObjectName(u"label_video")
        self.label_intro.setAlignment(Qt.AlignCenter)
        self.label_intro.setText(QCoreApplication.translate("MainWindow", u"SHOW INTRODUCTION", None))
        self.label_intro.setMinimumSize(QSize(700, 200))
        self.horizontalLayout_intro.addWidget(self.label_intro)

        self.scrollArea_intro.setWidget(self.scrollArea_WidgetContents_intro)
        self.gridLayout_NP.addWidget(self.scrollArea_intro, 3, 0, 1, 2)
        #新增label_intro

        #新增tableWidget_NP
        self.tableWidget_NP = QTableWidget(self.row_home)  #表格

        #設定col的數目
        if (self.tableWidget_NP.columnCount() < 2):
            self.tableWidget_NP.setColumnCount(2)
        #設定col的數目

        #設定row的數目
        #print("self.tableWidget_NP.rowCount() : {}".format(self.tableWidget_NP.rowCount()))
        if (self.tableWidget_NP.rowCount() < 20):
            self.tableWidget_NP.setRowCount(20)
        #設定row的數目

        #設定顏色
        palette_NP = QPalette()  #調色盤
        #QColor(R, G, B, lightness)  //lightness : 數字愈大愈亮
        #QBrush  //設定筆刷
        brush_NP = QBrush(QColor(221, 221, 221, 255))  #設定筆刷顏色
        brush_NP.setStyle(Qt.SolidPattern)  #背景圖案
        palette_NP.setBrush(QPalette.Inactive, QPalette.WindowText, brush_NP)  #設定背景文字顏色

        brush_NP1 = QBrush(QColor(0, 0, 0, 0))
        brush_NP1.setStyle(Qt.SolidPattern)
        palette_NP.setBrush(QPalette.Active, QPalette.Button, brush_NP1)  #設定button外框顏色
        palette_NP.setBrush(QPalette.Active, QPalette.Text, brush_NP)  #設定背景文字顏色
        palette_NP.setBrush(QPalette.Active, QPalette.ButtonText, brush_NP)  #設定button的文字顏色

        brush_NP2 = QBrush(QColor(0, 0, 0, 255))
        brush_NP2.setStyle(Qt.NoBrush)
        palette_NP.setBrush(QPalette.Active, QPalette.Base, brush_NP2)  #設定框內背景顏色
        palette_NP.setBrush(QPalette.Active, QPalette.Window, brush_NP1)  #設定背景顏色

#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette_NP.setBrush(QPalette.Active, QPalette.PlaceholderText, brush_NP)
#endif
        palette_NP.setBrush(QPalette.Inactive, QPalette.WindowText, brush_NP)
        palette_NP.setBrush(QPalette.Inactive, QPalette.Button, brush_NP1)
        palette_NP.setBrush(QPalette.Inactive, QPalette.Text, brush_NP)
        palette_NP.setBrush(QPalette.Inactive, QPalette.ButtonText, brush_NP)

        brush_NP3 = QBrush(QColor(0, 0, 0, 255))
        brush_NP3.setStyle(Qt.NoBrush)
        palette_NP.setBrush(QPalette.Inactive, QPalette.Base, brush_NP3)
        palette_NP.setBrush(QPalette.Inactive, QPalette.Window, brush_NP1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette_NP.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush_NP)
#endif
        palette_NP.setBrush(QPalette.Disabled, QPalette.WindowText, brush_NP)
        palette_NP.setBrush(QPalette.Disabled, QPalette.Button, brush_NP1)
        palette_NP.setBrush(QPalette.Disabled, QPalette.Text, brush_NP)
        palette_NP.setBrush(QPalette.Disabled, QPalette.ButtonText, brush_NP)

        brush_NP4 = QBrush(QColor(0, 0, 0, 255))
        brush_NP4.setStyle(Qt.NoBrush)
        palette_NP.setBrush(QPalette.Disabled, QPalette.Base, brush_NP4)
        palette_NP.setBrush(QPalette.Disabled, QPalette.Window, brush_NP1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette_NP.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush_NP)
#endif
        #設定顏色
        
        #設定tableWidget_NP
        self.tableWidget_NP.setPalette(palette_NP)
        self.tableWidget_NP.setFrameShape(QFrame.NoFrame)
        self.tableWidget_NP.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_NP.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_NP.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_NP.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_NP.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_NP.setShowGrid(True)
        self.tableWidget_NP.setGridStyle(Qt.SolidLine)
        self.tableWidget_NP.setSortingEnabled(False)
        self.tableWidget_NP.horizontalHeader().setVisible(False)
        self.tableWidget_NP.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_NP.horizontalHeader().setDefaultSectionSize(100)  #設定第一個col的寬度
        self.tableWidget_NP.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_NP.verticalHeader().setVisible(False)
        self.tableWidget_NP.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_NP.verticalHeader().setDefaultSectionSize(100)  #設定每個row的寬度
        self.tableWidget_NP.verticalHeader().setHighlightSections(False)
        self.tableWidget_NP.verticalHeader().setStretchLastSection(True)

        #設定tableWidget_NP

        self.gridLayout_NP.addWidget(self.tableWidget_NP, 0, 2, 4, 1)

        #設定gridLayout_NP的row和col的比例
        
        #設定各別row所占的比例
        self.gridLayout_NP.setRowStretch(0, 1)
        self.gridLayout_NP.setRowStretch(1, 1)
        self.gridLayout_NP.setRowStretch(2, 1)
        self.gridLayout_NP.setRowStretch(3, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        self.gridLayout_NP.setColumnStretch(0, 1)  
        self.gridLayout_NP.setColumnStretch(1, 1)
        self.gridLayout_NP.setColumnStretch(2, 1)
        #設定各別col所占的比例
        
        #設定gridLayout_NP的row和col的比例
       
        #新增tableWidget_NP


        self.verticalLayout_NP2.addLayout(self.gridLayout_NP)
        self.verticalLayout_NP.addWidget(self.row_NP)
        
        #設定label

        self.stackedWidget.addWidget(self.new_page)


        #new_page的GUI


        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        #extraRightBox
        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        #extraRightBox

        #verticalLayout_7
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        #verticalLayout_7

        #themeSettingsTopDetail
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)
        #themeSettingsTopDetail

        #contentSettings
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        #contentSettings

        #verticalLayout_13
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        #verticalLayout_13

        #topMenus
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        #topMenus

        #verticalLayout_14
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        #verticalLayout_14

        #btn_logout
        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)
        #btn_logout

        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)



        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PPS", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Still cool~", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        #self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))  #widgets的GUI
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))  #toggleLeftBox
#        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        #self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        #self.extraCloseColumnBtn.setText("")
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Jeff", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi