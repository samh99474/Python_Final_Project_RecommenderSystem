from DB.Ratings_Table import Ratings_Table

class Server_Rating:

    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        status = False
        try:
            for info in parameters:
                msg_return = Ratings_Table().select_a_rating(info["userId"], info["movieId"])
                print("msg_return : {}".format(msg_return))
                if len(msg_return) > 0 :
                    Ratings_Table().update_a_rating(info["userId"], info["movieId"], info["rating"], timestamp=1064891129)
                
                else :
                    Ratings_Table().insert_a_rating(info["userId"], info["movieId"], info["rating"], timestamp=1064891129)
                status = True

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True):
            #StudentInfoProcessor().restore_student_file(self.student_dict)   #新資料結合舊資料成功後，存檔
            reply_msg = {'status': "OK", 'parameters': parameters}
        else:
            reply_msg = {'status': "Fail", 'parameters': parameters, 'reason': "Rating error!"}
        return reply_msg