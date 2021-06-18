from DB.User_info_Table import User_info_Table
class Server_IdentifyUser:
    
    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        has_item = False
        status = False
        user_dict = dict()
        user_list = list()
        try:
            for info in parameters:
                user_dict["userName"] = info["userName"]  #建立學生字典
                user_dict["userPassword"] = info["userPassword"]

                userId = User_info_Table().select_a_userId(info["userName"])
                if(len(userId)==0) :  #沒有這個學生
                    has_item = False
                    status = False

                else:  #有這個學生
                    userPassword = User_info_Table().select_a_userPassword(userId[0])
                    if(user_dict["userPassword"] == str(userPassword[0])) :  #確認密碼是否一樣
                        user_dict["userId"] = userId[0]
                        print("SQL student_id: {}".format(userId))
                        has_item = True
                        status = True

                    else :
                        status = False

                user_dict["userPassword"] = ""
                user_list.append(user_dict)

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True): 
            reply_msg = {'status': "OK", 'parameters': user_list}    #回傳欲query查詢的學生資訊 Nested Dictionary

        else:
            reply_msg = {'status': "Fail", 'parameters': user_list, 'reason': "Incorrect account or password."}

        return reply_msg
