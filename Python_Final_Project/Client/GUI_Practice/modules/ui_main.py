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
        icon1.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
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
        amount_col = 2
        if (self.tableWidget_home.columnCount() < amount_col):
            self.tableWidget_home.setColumnCount(amount_col)
        #設定col的數目

        #設定row的數目
        #print("self.tableWidget_home.rowCount() : {}".format(self.tableWidget_home.rowCount()))
        amount_row = 5
        if (self.tableWidget_home.rowCount() < amount_row):
            self.tableWidget_home.setRowCount(amount_row)
        #設定row的數目


        font_table = QFont()
        font_table.setFamily(u"Segoe UI")
        font_table.setPointSize(15)
        font_table.setBold(False)
        font_table.setItalic(False)

        #宣告一個item放進去table裡面

        #設置tableWidget_home的item
        for i in range(amount_row):
                item_intro = QTableWidgetItem()  #要先設置item，在放進去table
                item_intro.setText("")
                item_intro.setFont(font_table)
                self.tableWidget_home.setItem(i, 1, item_intro)

                item_play = QTableWidgetItem(QIcon(":/icons/images/icons/cil-media-play.png")," ")  #要先設置item，在放進去table
                item_play.setText("Play")
                item_play.setFont(font_table)
                self.tableWidget_home.setItem(i, 0, item_play)


        #設置tableWidget_home的item

        


        """
        photo_2 = QLabel()
        photo_2.resize(800,800)
        photo_2.setPixmap(QPixmap(":/icons/images/icons/cil-account-logout.png"))
        self.tableWidget_home.setCellWidget(1, 0, photo_2)

        btn_play = QPushButton()
        btn_play.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")
        self.tableWidget_home.setCellWidget(2, 0, btn_play)
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
        self.tableWidget_home.horizontalHeader().setDefaultSectionSize(150)  #設定第一個col的寬度
        self.tableWidget_home.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_home.verticalHeader().setVisible(False)
        self.tableWidget_home.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_home.verticalHeader().setDefaultSectionSize(150)  #設定每個row的寬度
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
        #self.label_video.setStyleSheet(u"background-image: url(:images/images/messageImage_1624019018217.jpg);")
        #self.label_video.setPixmap(QPixmap("./images/messageImage_1624019018217.jpg"))
        self.label_video.setPixmap(QPixmap("./GUI_Practice/images/images/messageImage_1624019018217.jpg"))
        self.label_video.setScaledContents(True)
        self.label_video.setMinimumSize(QSize(561, 355.8))
        
        self.gridLayout_NP.addWidget(self.label_video, 0, 0, 1, 5)
        #新增label_video

        #新增label_rating
        self.label_rating = QLabel(self.row_NP)
        self.label_rating.setObjectName(u"label_rating")
        self.label_rating.setAlignment(Qt.AlignCenter)
        self.label_rating.setText(QCoreApplication.translate("MainWindow", u"Rating :", None))

        self.gridLayout_NP.addWidget(self.label_rating, 1, 0, 1, 1)
        #新增label_rating

        #新增lineEdit_rating
        self.lineEdit_rating = QLineEdit(self.row_NP)
        self.lineEdit_rating.setObjectName(u"lineEdit_rating")
        self.lineEdit_rating.setMinimumSize(QSize(40, 30))
        self.lineEdit_rating.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_rating.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your rating", None))
        self.gridLayout_NP.addWidget(self.lineEdit_rating, 1, 1, 1, 1)
        #新增lineEdit_rating
        font_rating = QFont()
        font_rating.setFamily(u"Segoe UI")
        font_rating.setPointSize(15)
        font_rating.setBold(False)
        font_rating.setItalic(False)

        #btn_rating
        self.btn_rating = QPushButton(self.row_NP)
        self.btn_rating.setObjectName(u"btn_rating")
        sizePolicy.setHeightForWidth(self.btn_rating.sizePolicy().hasHeightForWidth())
        self.btn_rating.setSizePolicy(sizePolicy)
        self.btn_rating.setMinimumSize(QSize(0, 45))
        self.btn_rating.setFont(font_rating)
        self.btn_rating.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rating.setLayoutDirection(Qt.LeftToRight)
        self.btn_rating.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.gridLayout_NP.addWidget(self.btn_rating, 1, 2, 1, 1)
        #btn_rating


        #新增label_rPA
        self.label_rPA = QLabel(self.row_NP)
        self.label_rPA.setObjectName(u"label_rPA")
        self.label_rPA.setAlignment(Qt.AlignCenter)
        self.label_rPA.setText(QCoreApplication.translate("MainWindow", u"", None))

        self.gridLayout_NP.addWidget(self.label_rPA, 1, 3, 1, 1)
        #新增label_rPA





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
                                                                "border: none;\n"
                                                                "background: rgb(0, 0, 0);\n"
                                                                "width: 14px;\n"
                                                                "margin: 21px 0 21px 0;\n"
                                                                "border-radius: 0px;\n"
                                                                " }")
        #原本顏色為background: rgb(52, 59, 72)
        #設定scrollArea_WidgetContents_intro

        self.horizontalLayout_intro = QHBoxLayout(self.scrollArea_WidgetContents_intro)
        self.horizontalLayout_intro.setObjectName(u"horizontalLayout_intro")


        # font_label = QFont()
        # font_label.setFamily(u"Segoe UI")
        # font_label.setPointSize(100)
        # font_label.setBold(False)
        # font_label.setItalic(False)

        self.label_intro = QLabel(self.scrollArea_WidgetContents_intro)
        #self.label_intro.setFont(font_label)  #字體大小無法改
        self.label_intro.setObjectName(u"label_video")
        self.label_intro.setWordWrap(True)  #有時會自動換行，有時不會
        self.label_intro.setText("Show description of movie.")
        self.label_intro.setStyleSheet("font-size:20px;") 
        #self.label_intro.setAlignment(Qt.AlignCenter)
        #self.label_intro.setText(QCoreApplication.translate("MainWindow", u"SHOW INTRODUCTION", None))
        self.label_intro.setMinimumSize(QSize(700, 100))
        self.horizontalLayout_intro.addWidget(self.label_intro)

        self.scrollArea_intro.setWidget(self.scrollArea_WidgetContents_intro)
        self.gridLayout_NP.addWidget(self.scrollArea_intro, 2, 0, 1, 5)
        #新增label_intro

        #新增tableWidget_NP
        self.tableWidget_NP = QTableWidget(self.row_home)  #表格

        #設定col的數目
        if (self.tableWidget_NP.columnCount() < amount_col):
            self.tableWidget_NP.setColumnCount(amount_col)
        #設定col的數目

        #設定row的數目
        #print("self.tableWidget_NP.rowCount() : {}".format(self.tableWidget_NP.rowCount()))
        if (self.tableWidget_NP.rowCount() < amount_row):
            self.tableWidget_NP.setRowCount(amount_row)
        #設定row的數目


        #設置tableWidget_home的item
        for i in range(amount_row):
                item_intro = QTableWidgetItem()  #要先設置item，在放進去table
                item_intro.setText("")
                item_intro.setFont(font_table)
                self.tableWidget_NP.setItem(i, 1, item_intro)

                item_play = QTableWidgetItem(QIcon(":/icons/images/icons/cil-media-play.png")," ")  #要先設置item，在放進去table
                item_play.setText("Play")
                item_play.setFont(font_table)
                self.tableWidget_NP.setItem(i, 0, item_play)
        #設置tableWidget_home的item

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

        self.gridLayout_NP.addWidget(self.tableWidget_NP, 0, 5, 3, 1)

        #設定gridLayout_NP的row和col的比例

        #設定各別row所占的比例
        self.gridLayout_NP.setRowStretch(0, 3)  
        self.gridLayout_NP.setRowStretch(1, 1)
        self.gridLayout_NP.setRowStretch(2, 3)
        #設定各別row所占的比例
        
        #設定各別col所占的比例
        self.gridLayout_NP.setColumnStretch(0, 1)
        self.gridLayout_NP.setColumnStretch(1, 2)
        self.gridLayout_NP.setColumnStretch(2, 1)
        self.gridLayout_NP.setColumnStretch(3, 2)
        self.gridLayout_NP.setColumnStretch(4, 2)
        self.gridLayout_NP.setColumnStretch(5, 4)
        #設定各別col所占的比例
        
        #設定gridLayout_NP的row和col的比例
       
        #新增tableWidget_NP


        self.verticalLayout_NP2.addLayout(self.gridLayout_NP)
        self.verticalLayout_NP.addWidget(self.row_NP)
        
        #設定label

        self.stackedWidget.addWidget(self.new_page)


        #new_page的GUI

        #loading_page的GUI
        self.loading_page = QWidget()
        self.loading_page.setObjectName(u"loading_page")
        self.verticalLayout_loading = QVBoxLayout(self.loading_page)
        self.verticalLayout_loading.setObjectName(u"verticalLayout_loading")
        self.label_loading = QLabel(self.loading_page)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_loading.setStyleSheet("font-size:50px")

        self.verticalLayout_loading.addWidget(self.label_loading)
        self.label_loading.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))

        self.stackedWidget.addWidget(self.loading_page)
        #loading_page的GUI




        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        #extraRightBox
        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))  #(寬，長)
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

        #stackedWidget_setting
        self.stackedWidget_setting = QStackedWidget(self.topMenus)
        self.stackedWidget_setting.setObjectName(u"stackedWidgetSetting")
        #stackedWidget_setting

        #btn_login
        self.btn_login = QPushButton(self.topMenus)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(0, 45))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setLayoutDirection(Qt.LeftToRight)
        self.btn_login.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-input.png);")
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))

        self.stackedWidget_setting.addWidget(self.btn_login)
        #btn_login

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
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))

        self.stackedWidget_setting.addWidget(self.btn_logout)
        #btn_logout

        #login_page的GUI
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")

        #一組
        self.verticalLayout_login = QVBoxLayout(self.login_page)
        self.verticalLayout_login.setObjectName(u"verticalLayout_login")

        
        #設定row_login
        self.row_login = QFrame(self.login_page)
        self.row_login.setObjectName(u"row_login")
        #self.row_login.setMinimumSize(QSize(400, 150))
        self.row_login.setFrameShape(QFrame.StyledPanel)
        self.row_login.setFrameShadow(QFrame.Raised)
        #設定row_login

        #用垂直的排列
        self.verticalLayout_login2 = QVBoxLayout(self.row_login)
        self.verticalLayout_login2.setObjectName(u"verticalLayout_login2")
        #用垂直的排列

        #新增gridLayout_NP
        self.gridLayout_login = QGridLayout()
        self.gridLayout_login.setObjectName(u"gridLayout_login")
        #新增gridLayout_NP
        #一組


        #login_page中的widgets
        font_login = QFont()
        font_login.setFamily(u"Segoe UI")
        font_login.setPointSize(15)
        font_login.setBold(False)
        font_login.setItalic(False)


        self.label_PA2 = QLabel(self.row_login)
        self.label_PA2.setObjectName(u"label_PA2")
        self.label_PA2.setFont(font_login)
        self.label_PA2.setStyleSheet(u"")
        self.label_PA2.setText("")
        self.gridLayout_login.addWidget(self.label_PA2, 0, 0, 1, 2)

        self.label_accout = QLabel(self.row_login)
        self.label_accout.setObjectName(u"label_accout")
        self.label_accout.setFont(font_login)
        self.label_accout.setStyleSheet(u"")
        self.label_accout.setText("Account")
        self.gridLayout_login.addWidget(self.label_accout, 1, 0, 1, 2)

        self.lineEdit_account = QLineEdit(self.row_login)
        self.lineEdit_account.setObjectName(u"lineEdit_account")
        self.lineEdit_account.setMinimumSize(QSize(0, 30))
        self.lineEdit_account.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_account.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your accout", None))
        self.gridLayout_login.addWidget(self.lineEdit_account, 2, 0, 1, 3)


        self.label_password = QLabel(self.row_login)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font_login)
        self.label_password.setStyleSheet(u"")
        self.label_password.setText("Password")
        self.gridLayout_login.addWidget(self.label_password, 4, 0, 1, 2)

        self.lineEdit_password = QLineEdit(self.row_login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 30))
        self.lineEdit_password.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your password", None))
        self.gridLayout_login.addWidget(self.lineEdit_password, 5, 0, 1, 3)


        #btn_login_2
        self.btn_login_2 = QPushButton(self.row_login)
        self.btn_login_2.setObjectName(u"btn_login_2")
        sizePolicy.setHeightForWidth(self.btn_login_2.sizePolicy().hasHeightForWidth())
        self.btn_login_2.setSizePolicy(sizePolicy)
        self.btn_login_2.setMinimumSize(QSize(0, 45))
        self.btn_login_2.setFont(font_login)
        self.btn_login_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login_2.setLayoutDirection(Qt.LeftToRight)
        #self.btn_login_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-input.png);")
        self.btn_login_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.gridLayout_login.addWidget(self.btn_login_2, 6, 1, 1, 2)
        #btn_login_2
        #login_page中的widgets


        #一組
        #設定gridLayout_login的row和col的比例
        
        #設定各別row所占的比例
        self.gridLayout_login.setRowStretch(0, 1)
        self.gridLayout_login.setRowStretch(1, 1)
        self.gridLayout_login.setRowStretch(2, 1)
        self.gridLayout_login.setRowStretch(3, 1)
        self.gridLayout_login.setRowStretch(4, 1)
        self.gridLayout_login.setRowStretch(5, 1)
        self.gridLayout_login.setRowStretch(6, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        self.gridLayout_login.setColumnStretch(0, 1)  
        self.gridLayout_login.setColumnStretch(1, 1)
        self.gridLayout_login.setColumnStretch(2, 1)
        #設定各別col所占的比例
        
        #設定gridLayout_login的row和col的比例


        self.verticalLayout_login2.addLayout(self.gridLayout_login)
        self.verticalLayout_login.addWidget(self.row_login)
        
        #設定label

        self.stackedWidget_setting.addWidget(self.login_page)
        #一組

        
        #login_page的GUI


        #announcement_page的GUI
        self.announcement_page = QWidget()
        self.announcement_page.setObjectName(u"announcement_page")


        #一組
        self.verticalLayout_AP = QVBoxLayout(self.announcement_page)
        self.verticalLayout_AP.setObjectName(u"verticalLayout_AP")

        
        #設定row_AP
        self.row_AP = QFrame(self.login_page)
        self.row_AP.setObjectName(u"row_AP")
        #self.row_AP.setMinimumSize(QSize(400, 150))
        self.row_AP.setFrameShape(QFrame.StyledPanel)
        self.row_AP.setFrameShadow(QFrame.Raised)
        #設定row_AP

        #用垂直的排列
        self.verticalLayout_AP2 = QVBoxLayout(self.row_AP)
        self.verticalLayout_AP2.setObjectName(u"verticalLayout_AP2")
        #用垂直的排列

        #新增gridLayout_NP
        self.gridLayout_AP = QGridLayout()
        self.gridLayout_AP.setObjectName(u"gridLayout_AP")
        #新增gridLayout_NP
        #一組

        #announcement_page中的widgets

        self.label_PA = QLabel(self.row_AP)
        self.label_PA.setObjectName(u"label_PA")
        self.label_PA.setFont(font_login)
        self.label_PA.setStyleSheet(u"")
        self.label_PA.setWordWrap(True)  #有時會自動換行，有時不會
        self.label_PA.setText("Incorrect account or password.")
        self.label_PA.setStyleSheet("color:rgb(196, 0, 0);"
                                        "font-size:15px;") 
        self.gridLayout_AP.addWidget(self.label_PA, 0, 0, 3, 3)


        #btn_return
        self.btn_return = QPushButton(self.row_AP)
        self.btn_return.setObjectName(u"btn_return")
        sizePolicy.setHeightForWidth(self.btn_return.sizePolicy().hasHeightForWidth())
        self.btn_return.setSizePolicy(sizePolicy)
        self.btn_return.setMinimumSize(QSize(0, 45))
        self.btn_return.setFont(font_login)
        self.btn_return.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_return.setLayoutDirection(Qt.LeftToRight)
        self.btn_return.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-left.png);")
        self.btn_return.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.gridLayout_AP.addWidget(self.btn_return, 3, 0, 1, 3)
        #btn_return

        #btn_sign_up
        self.btn_sign_up = QPushButton(self.row_AP)
        self.btn_sign_up.setObjectName(u"btn_sign_up")
        sizePolicy.setHeightForWidth(self.btn_sign_up.sizePolicy().hasHeightForWidth())
        self.btn_sign_up.setSizePolicy(sizePolicy)
        self.btn_sign_up.setMinimumSize(QSize(0, 45))
        self.btn_sign_up.setFont(font_login)
        self.btn_sign_up.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sign_up.setLayoutDirection(Qt.LeftToRight)
        self.btn_sign_up.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-hand-point-up.png);")
        self.btn_sign_up.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.gridLayout_AP.addWidget(self.btn_sign_up, 4, 0, 1, 3)
        #btn_sing_up


        #announcement_page中的widgets


        #一組
        #設定gridLayout_AP的row和col的比例
        
        #設定各別row所占的比例
        self.gridLayout_AP.setRowStretch(0, 1)
        self.gridLayout_AP.setRowStretch(1, 1)
        self.gridLayout_AP.setRowStretch(2, 1)
        self.gridLayout_AP.setRowStretch(3, 1)
        self.gridLayout_AP.setRowStretch(4, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        self.gridLayout_AP.setColumnStretch(0, 1)  
        self.gridLayout_AP.setColumnStretch(1, 1)
        self.gridLayout_AP.setColumnStretch(2, 1)
        #設定各別col所占的比例
        
        #設定gridLayout_AP的row和col的比例


        self.verticalLayout_AP2.addLayout(self.gridLayout_AP)
        self.verticalLayout_AP.addWidget(self.row_AP)
        
        #設定label

        self.stackedWidget_setting.addWidget(self.announcement_page)
        #一組

        #announcement_page的GUI

        #sign_up_page的GUI
        self.sign_up_page = QWidget()
        self.sign_up_page.setObjectName(u"sign_up_page")

        #一組
        self.verticalLayout_sign_up = QVBoxLayout(self.sign_up_page)
        self.verticalLayout_sign_up.setObjectName(u"verticalLayout_sign_up")

        
        #設定row_sign_up
        self.row_sign_up = QFrame(self.sign_up_page)
        self.row_sign_up.setObjectName(u"row_sign_up")
        #self.row_sign_up.setMinimumSize(QSize(400, 150))
        self.row_sign_up.setFrameShape(QFrame.StyledPanel)
        self.row_sign_up.setFrameShadow(QFrame.Raised)
        #設定row_sign_up

        #用垂直的排列
        self.verticalLayout_sign_up2 = QVBoxLayout(self.row_sign_up)
        self.verticalLayout_sign_up2.setObjectName(u"verticalLayout_sign_up2")
        #用垂直的排列

        #新增gridLayout_NP
        self.gridLayout_sign_up = QGridLayout()
        self.gridLayout_sign_up.setObjectName(u"gridLayout_sign_up")
        #新增gridLayout_NP
        #一組


        #sign_up_page中的widgets
        font_sign_up = QFont()
        font_sign_up.setFamily(u"Segoe UI")
        font_sign_up.setPointSize(15)
        font_sign_up.setBold(False)
        font_sign_up.setItalic(False)

        self.label_PA_2 = QLabel(self.row_sign_up)
        self.label_PA_2.setObjectName(u"label_PA_2")
        self.label_PA_2.setFont(font_sign_up)
        self.label_PA_2.setStyleSheet(u"")
        self.label_PA_2.setText("")
        self.label_PA_2.setStyleSheet("color:rgb(196, 0, 0);"
                                "font-size:15px;") 
        self.gridLayout_sign_up.addWidget(self.label_PA_2, 0, 0, 1, 3)

        self.label_accout2 = QLabel(self.row_sign_up)
        self.label_accout2.setObjectName(u"label_accout2")
        self.label_accout2.setFont(font_sign_up)
        self.label_accout2.setStyleSheet(u"")
        self.label_accout2.setText("Account")
        self.gridLayout_sign_up.addWidget(self.label_accout2, 1, 0, 1, 2)

        self.lineEdit_account2 = QLineEdit(self.row_sign_up)
        self.lineEdit_account2.setObjectName(u"lineEdit_account2")
        self.lineEdit_account2.setMinimumSize(QSize(0, 30))
        self.lineEdit_account2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_account2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your accout", None))
        self.gridLayout_sign_up.addWidget(self.lineEdit_account2, 2, 0, 1, 3)


        self.label_password2 = QLabel(self.row_sign_up)
        self.label_password2.setObjectName(u"label_password2")
        self.label_password2.setFont(font_sign_up)
        self.label_password2.setStyleSheet(u"")
        self.label_password2.setText("Password")
        self.gridLayout_sign_up.addWidget(self.label_password2, 4, 0, 1, 2)

        self.lineEdit_password2 = QLineEdit(self.row_sign_up)
        self.lineEdit_password2.setObjectName(u"lineEdit_password2")
        self.lineEdit_password2.setMinimumSize(QSize(0, 30))
        self.lineEdit_password2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_password2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your password", None))
        self.gridLayout_sign_up.addWidget(self.lineEdit_password2, 5, 0, 1, 3)

        self.label_password3 = QLabel(self.row_sign_up)
        self.label_password3.setObjectName(u"label_password3")
        self.label_password3.setFont(font_sign_up)
        self.label_password3.setStyleSheet(u"")
        self.label_password3.setText("Re-enter password")
        self.gridLayout_sign_up.addWidget(self.label_password3, 7, 0, 1, 2)

        self.lineEdit_password3 = QLineEdit(self.row_sign_up)
        self.lineEdit_password3.setObjectName(u"lineEdit_password3")
        self.lineEdit_password3.setMinimumSize(QSize(0, 30))
        self.lineEdit_password3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_password3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your password again", None))
        self.gridLayout_sign_up.addWidget(self.lineEdit_password3, 8, 0, 1, 3)


        #btn_sign_up_2
        self.btn_sign_up_2 = QPushButton(self.row_sign_up)
        self.btn_sign_up_2.setObjectName(u"btn_sign_up_2")
        sizePolicy.setHeightForWidth(self.btn_sign_up_2.sizePolicy().hasHeightForWidth())
        self.btn_sign_up_2.setSizePolicy(sizePolicy)
        self.btn_sign_up_2.setMinimumSize(QSize(0, 45))
        self.btn_sign_up_2.setFont(font_sign_up)
        self.btn_sign_up_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sign_up_2.setLayoutDirection(Qt.LeftToRight)
        #self.btn_sign_up_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-input.png);")
        self.btn_sign_up_2.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.gridLayout_sign_up.addWidget(self.btn_sign_up_2, 9, 1, 1, 2)
        #btn_sign_up_2
        #sign_up_page中的widgets


        #一組
        #設定gridLayout_sign_up的row和col的比例
        
        #設定各別row所占的比例
        self.gridLayout_sign_up.setRowStretch(0, 1)
        self.gridLayout_sign_up.setRowStretch(1, 1)
        self.gridLayout_sign_up.setRowStretch(2, 1)
        self.gridLayout_sign_up.setRowStretch(3, 1)
        self.gridLayout_sign_up.setRowStretch(4, 1)
        self.gridLayout_sign_up.setRowStretch(5, 1)
        self.gridLayout_sign_up.setRowStretch(6, 1)
        self.gridLayout_sign_up.setRowStretch(7, 1)
        self.gridLayout_sign_up.setRowStretch(8, 1)
        self.gridLayout_sign_up.setRowStretch(9, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        self.gridLayout_sign_up.setColumnStretch(0, 1)  
        self.gridLayout_sign_up.setColumnStretch(1, 1)
        self.gridLayout_sign_up.setColumnStretch(2, 1)
        #設定各別col所占的比例
        
        #設定gridLayout_sign_up的row和col的比例


        self.verticalLayout_sign_up2.addLayout(self.gridLayout_sign_up)
        self.verticalLayout_sign_up.addWidget(self.row_sign_up)
        
        #設定label

        self.stackedWidget_setting.addWidget(self.sign_up_page)
        #一組

        
        #sign_up_page的GUI





        self.verticalLayout_14.addWidget(self.stackedWidget_setting)


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
        
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Jeff", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi