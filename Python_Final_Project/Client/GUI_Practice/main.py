# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

#
# 目前有bug
# 需要用到執行續?
# 已經資料出來才跳畫面
#

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


from SocketClient.Socket_Client import SocketClient
from test_function.AddUser import AddUser
from test_function.Get_Movie_RS import Get_Movie_RS
from test_function.Rating import Rating
from test_function.QueryMovie import QueryMovie
from test_function.QueryUser import QueryUser
from test_function.AnalyzeData import AnalyzeData
from test_function.IdentifyUser import IdentifyUser

action_list = {
    "add": AddUser,
    "RS" : Get_Movie_RS,
    "rating": Rating,
    "QueryMovie": QueryMovie,
    "QU" : QueryUser,
    "IU" : IdentifyUser
}


# SET AS GLOBAL WIDGETS
widgets = None
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self = QMainWindow

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.user_name = None
        self.user_id = None
        self.movieId = None

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "PyDracula - Modern GUI"
        description = "Python Class - Recommendation System"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.tableWidget_home.cellClicked.connect(self.click_tableWidget_home)
        widgets.tableWidget_NP.cellClicked.connect(self.click_tableWidget_NP)
        """
        item_test = QTableWidgetItem()  #要先設置item，在放進去table
        item_test.setText("123")
        widgets.tableWidget_home.setItem(0, 0, item_test)
        """


        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
            if self.user_name == None and self.user_id == None :
                widgets.stackedWidget_setting.setCurrentWidget(widgets.btn_login)
            
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        #Setting function
        widgets.btn_login.clicked.connect(self.buttonClick_setting)
        widgets.btn_logout.clicked.connect(self.buttonClick_setting)
        widgets.btn_login_2.clicked.connect(self.buttonClick_setting)
        widgets.btn_return.clicked.connect(self.buttonClick_setting)
        widgets.btn_sign_up.clicked.connect(self.buttonClick_setting)
        widgets.btn_sign_up_2.clicked.connect(self.buttonClick_setting)
        #Setting function

        #rating function
        widgets.btn_rating.clicked.connect(self.buttonClick_setting)
        #rating function


        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        #先切到loading的畫面
        widgets.stackedWidget.setCurrentWidget(widgets.loading_page)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        #先切到loading的畫面
        

        #先不要，會很慢
        client = SocketClient()
        result = action_list["RS"](client).execute()
        print("result : {}".format(result))
        #home的初始化畫面
        #parameters
        #title
        #vote_average
        #genres
        result_REC = result["parameters"]
        print(len(result))
        for i in range(len(result_REC)) :
            dict_movie = result_REC[i]
            """
            print("\nMovie {}".format(i))
            print("Movie : {}".format(dict_movie["title"]))
            print("Vote average : {}".format(dict_movie["vote_average"]))
            print("Genres : {}".format(dict_movie["genres"]))
            """
            #text_show_movie_info = "Movie {}".format(i)
            text_show_movie_info = "Num. {}".format(dict_movie["id"])
            text_show_movie_info += "\nMovie : {}".format(dict_movie["title"])
            text_show_movie_info += "\nVote average : {}".format(dict_movie["vote_average"])
            text_show_movie_info += "\nGenres : {}".format(dict_movie["genres"])
            print(text_show_movie_info)
            widgets.tableWidget_home.item(i, 1).setText(text_show_movie_info)
        #home的初始化畫面
        #先不要，會很慢
        
        #等到好了再切到home畫面
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        #等到好了再切到home畫面
        


    # BUTTONS CLICK 

    # Post here your functions for clicked buttons
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

            widgets.lineEdit_rating.clear()
            widgets.label_rPA.setText("")

        if btnName == "btn_save":
            print("Save BTN clicked!")

        if btnName == "btn_exit":
             print("Exit BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    #增加新功能
    def click_tableWidget_home(self, row, col):
        #print("cool~")
        #cellContent = item
        #print(row) # test 
        sf = "You clicked on [{},{}]".format(row,col) 
        print(sf) 
        
        text = widgets.tableWidget_home.item(row, 1).text()
        
        print(text)
        text_splited = text.split('\n')
        print("text_splited : {}".format(text_splited))
        id_movie = AnalyzeData().catch_data_back(text_splited[0], "Num. ")
        print("id_movie : {}".format(id_movie))

        #widgets.tableWidget_home.item(row, col).setText("456")
        #點按鈕才跳畫面
        if col == 0 :
            #切換loading_page頁面
            print("1")
            widgets.stackedWidget.setCurrentWidget(widgets.loading_page) # SET PAGE
            UIFunctions.resetStyle(self, "btn_new") # RESET ANOTHERS BUTTONS SELECTED
            widgets.btn_new.setStyleSheet(UIFunctions.selectMenu(widgets.btn_new.styleSheet())) # SELECT MENU
            print("2")
            #切換loading_page頁面

            
            self.show_new_page(int(id_movie[0]))

            print("3")
            #切換new_page頁面
            # widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            # UIFunctions.resetStyle(self, "btn_new") # RESET ANOTHERS BUTTONS SELECTED
            # widgets.btn_new.setStyleSheet(UIFunctions.selectMenu(widgets.btn_new.styleSheet())) # SELECT MENU
            #切換new_page頁面
            print("4")
            

        #點按鈕才跳畫面
    def show_new_page(self, id_movie) :
        
        #都先抓好資料再轉換頁面
        client = SocketClient()
        result= action_list["QueryMovie"](client).execute(int(id_movie))
        print("result : {}".format(result))
        list_movie = result["parameters"]
        dict_movie = list_movie[0]
        self.movieId = dict_movie["movieId"]

        self.update_label_intro(dict_movie)
        self.update_tableWidget_NP(name_movie = dict_movie["movieName"], id_movie = dict_movie["id"])

        widgets.lineEdit_rating.clear()
        widgets.label_rPA.setText("")
        #都先抓好資料再轉換頁面
        


    def update_label_intro(self, dict_movie):
        #label_intro
        text_show_movie_info = "Num. {}".format(dict_movie["id"])
        text_show_movie_info += "\nMovie : {}".format(dict_movie["movieName"])
        text_show_movie_info += "\nVote average : {}".format(dict_movie["vote_average"])
        text_show_movie_info += "\nGenres : {}".format(dict_movie["genres"])
        text_show_movie_info += "\nOverview : {}".format(dict_movie["overview"])

        widgets.label_intro.setText(text_show_movie_info)
        #label_intro

    def update_tableWidget_NP(self, name_movie = None, id_movie = None):
        client = SocketClient()
        if self.user_name != None and self.user_id != None :
            print("user_name : {}, user_id : {}".format(self.user_name, self.user_id))
            result = action_list["RS"](client).execute(userName = self.user_name, userId = self.user_id, movieTitle = name_movie, id = int(id_movie))
        
        else :
            print("user_name : {}, user_id : {}".format(self.user_name, self.user_id))
            result = action_list["RS"](client).execute(movieTitle = name_movie, id = int(id_movie))

        print("result : {}".format(result))
        #tableWidget_NP的初始化畫面
        #parameters
        #title
        #vote_average
        #genres
        result_REC = result["parameters"]
        print(len(result))
        for i in range(len(result_REC)) :
            dict_movie = result_REC[i]
            """
            print("\nMovie {}".format(i))
            print("Movie : {}".format(dict_movie["title"]))
            print("Vote average : {}".format(dict_movie["vote_average"]))
            print("Genres : {}".format(dict_movie["genres"]))
            """
            #text_show_movie_info = "Movie {}".format(i)
            text_show_movie_info = "Num. {}".format(dict_movie["id"])
            text_show_movie_info += "\nMovie : {}".format(dict_movie["title"])
            text_show_movie_info += "\nVote average : {}".format(dict_movie["vote_average"])
            text_show_movie_info += "\nGenres : {}".format(dict_movie["genres"])
            print(text_show_movie_info)
            widgets.tableWidget_NP.item(i, 1).setText(text_show_movie_info)
        #tableWidget_NP的初始化畫面
    
    def click_tableWidget_NP(self, row, col):
        sf = "You clicked on [{},{}]".format(row,col) 
        print(sf) 

        client = SocketClient()

        #取出tableWidget_NP的資訊
        text = widgets.tableWidget_NP.item(row, 1).text()
        print(text)
        text_splited = text.split('\n')
        print("text_splited : {}".format(text_splited))
        id_movie = AnalyzeData().catch_data_back(text_splited[0], "Num. ")
        name_movie = AnalyzeData().catch_data_back(text_splited[1], "Movie : ")
        print("id_movie : {}".format(id_movie))
        print("name_movie : {}".format(name_movie))
        #取出tableWidget_NP的資訊

        if col == 0 :
            #更新label_intro
            result= action_list["QueryMovie"](client).execute(str(id_movie[0]))
            print("result : {}".format(result))

            list_movie = result["parameters"]
            dict_movie = list_movie[0]
            text_show_movie_info = "Num. {}".format(dict_movie["id"])
            text_show_movie_info += "\nMovie : {}".format(dict_movie["movieName"])
            text_show_movie_info += "\nVote average : {}".format(dict_movie["vote_average"])
            text_show_movie_info += "\nGenres : {}".format(dict_movie["genres"])
            text_show_movie_info += "\nOverview : {}".format(dict_movie["overview"])

            widgets.label_intro.setText(text_show_movie_info)
            #更新label_intro
            widgets.lineEdit_rating.clear()
            self.update_tableWidget_NP(name_movie[0], dict_movie["id"])
            

    def test(self):
        print("HI")
        widgets.stackedWidget_setting.setCurrentWidget(widgets.btn_login) # SET PAGE

    def buttonClick_setting(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        client = SocketClient()

        #btn_login
        if btnName == "btn_login":
            widgets.stackedWidget_setting.setCurrentWidget(widgets.login_page)

        #btn_login_2
        if btnName == "btn_login_2":
            text_accout = widgets.lineEdit_account.text()
            text_password = widgets.lineEdit_password.text()
            
            if text_accout == "" :
                widgets.label_PA2.setText("Please input account.")
                widgets.label_PA2.setStyleSheet("color:rgb(196, 0, 0);"
                                                "font-size:15px;") 

            elif text_password == "" :
                widgets.label_PA2.setText("Please input password.")
                widgets.label_PA2.setStyleSheet("color:rgb(196, 0, 0);"
                                                "font-size:15px;") 

            else :
                result = action_list["IU"](client).execute(text_accout, text_password)
                
            parameters = result["parameters"][0]
            if result["status"] == "OK" :
                self.user_name = parameters["userName"]
                self.user_id = parameters["userId"]
                #print("user_name : {}, user_id : {}".format(self.user_name, self.user_id))
                widgets.stackedWidget_setting.setCurrentWidget(widgets.btn_logout)
                widgets.lineEdit_account.clear()
                widgets.lineEdit_password.clear()
                widgets.label_PA2.setText("")

                #等到好了再切到home畫面
                widgets.stackedWidget.setCurrentWidget(widgets.home)
                UIFunctions.resetStyle(self, "btn_home") # RESET ANOTHERS BUTTONS SELECTED
                widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
                #等到好了再切到home畫面
                
            else :
                widgets.stackedWidget_setting.setCurrentWidget(widgets.announcement_page)
                widgets.lineEdit_account.clear()
                widgets.lineEdit_password.clear()
                widgets.label_PA2.setText("")

        #btn_return
        if btnName == "btn_return":
            widgets.stackedWidget_setting.setCurrentWidget(widgets.login_page)
            

        #btn_sign_up
        if btnName == "btn_sign_up":
            widgets.stackedWidget_setting.setCurrentWidget(widgets.sign_up_page)
            widgets.lineEdit_account2.clear()
            widgets.lineEdit_password2.clear()
            widgets.lineEdit_password3.clear()

        #btn_sign_up_2
        if btnName == "btn_sign_up_2":

            text_account2 = widgets.lineEdit_account2.text()
            text_password2 = widgets.lineEdit_password2.text()
            text_password3 = widgets.lineEdit_password3.text()
            if text_account2 == "" :
                widgets.label_PA_2.setText("Please input account.")

            elif text_password2 == "" :
                widgets.label_PA_2.setText("Please input password.")
            
            elif text_password3 == "" :
                widgets.label_PA_2.setText("Please input password again.")

            elif text_password2 != text_password3 :
                widgets.label_PA_2.setText("Password confirms wrongly.")
               
            else :
                result = action_list["add"](client).execute(text_account2, text_password2)
            
    
            if result :
                widgets.stackedWidget_setting.setCurrentWidget(widgets.login_page)
                widgets.label_PA2.setText("Sign up completely.\nPlease login again.")
                widgets.label_PA2.setStyleSheet("color:rgb(135, 191, 67);"
                                                "font-size:15px;") 
                
            else :
                widgets.label_PA_2.setText("The account already exists.")
                widgets.lineEdit_account2.clear()
                widgets.lineEdit_password2.clear()
                widgets.lineEdit_password3.clear()
                

        #btn_logout
        if btnName == "btn_logout":
            widgets.stackedWidget_setting.setCurrentWidget(widgets.btn_login) # SET PAGE
            self.user_name = None
            self.user_id = None

            #等到好了再切到home畫面
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, "btn_home") # RESET ANOTHERS BUTTONS SELECTED
            widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
            #等到好了再切到home畫面

        if btnName == "btn_rating" :
            text_rating = widgets.lineEdit_rating.text()

            if self.user_name == None and self.user_id == None :
                widgets.lineEdit_rating.clear()
                widgets.label_rPA.setText("Please login first.")
                widgets.label_rPA.setStyleSheet("color:rgb(196, 0, 0);"
                                                "font-size:15px;") 
            
            elif text_rating == "" :
                widgets.label_rPA.setText("Please type your rating.")
                widgets.label_rPA.setStyleSheet("color:rgb(196, 0, 0);"
                                                "font-size:15px;")

            elif int(text_rating) < 0 or int(text_rating) > 5 :
                widgets.label_rPA.setText("Rating range from 0 to 5!")
                widgets.label_rPA.setStyleSheet("color:rgb(196, 0, 0);"
                                                "font-size:15px;")
                
            else :
                print("int(text_rating) : {}".format(int(text_rating)))


                result = action_list["rating"](client).execute(self.user_name, self.user_id, self.movieId, int(text_rating))
                
                print("result : {}".format(result))
                if result["status"] == "OK" :
                    widgets.label_rPA.setText("Rating completely.")
                    widgets.label_rPA.setStyleSheet("color:rgb(135, 191, 67);"
                                                "font-size:15px;")  
                else : 
                    widgets.label_rPA.setText("Rating unsuccessfully.")
                    widgets.label_rPA.setStyleSheet("color:rgb(196, 0, 0);"
                                                "font-size:15px;") 

                widgets.lineEdit_rating.clear()

                

            

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')



            


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
