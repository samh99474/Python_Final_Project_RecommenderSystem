import json
class IdentifyUser():
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self, userName = None, userPassword = None):
        try:
            print("確認使用者帳密是否正確")
            #userName = str(input("  Please input a user's name: "))
            has_item = False
            add_user_dict = dict()
            query_user_dict = dict()
            query_user_dict["userName"] = userName
            query_user_dict["userPassword"] = userPassword

            query_list_info = list()
            query_list_info.append(query_user_dict)

            #確認User身份
            self.socket_client.send_command("identifyUser", query_list_info)
            print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("identifyUser", query_list_info))

            boolean, result = self.socket_client.wait_response()
            result = json.loads(result) # convert dictionary string to dictionary

            if result['status'] == "Fail":
                print("帳號密碼錯誤")
                add_user_dict["userName"] = userName  
                success = True

            else:
                print("登入成功")
                success = False
        
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            success = False
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            print("result : {}".format(result))
            return result