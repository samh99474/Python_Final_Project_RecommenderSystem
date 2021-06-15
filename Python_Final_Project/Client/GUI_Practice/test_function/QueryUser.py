import json
class QueryUser():
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self, userName = None):
        try:
            print("查詢用戶姓名")
            #userName = str(input("  Please input a user's name: "))
            has_item = False
            add_user_dict = dict()
            query_user_dict = dict()
            query_user_dict["userName"] = userName

            query_list_info = list()
            query_list_info.append(query_user_dict)

            #先查詢query是否存在用戶名稱
            self.socket_client.send_command("queryUser", query_list_info)
            print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("query", query_list_info))

            boolean, result = self.socket_client.wait_response()
            result = json.loads(result) # convert dictionary string to dictionary

            if result['status'] == "Fail":
                print("此名稱不存在，您可以新增此學生")
                add_user_dict["userName"] = userName  
                success = True
            else:
                print("此名稱存在，您不可以新增此學生")
                success = False
        
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            success = False
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            print("result : {}".format(result))
            return result