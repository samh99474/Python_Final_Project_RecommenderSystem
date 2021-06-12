from DB.MovieData_Table import MovieData_Table
from DB.MovieID_map_Table import MovieID_map_Table

class Server_QueryMovie:
    
    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        has_item = False
        status = False
        Movie_dict = dict()
        movie_list = list()
        try:
            for info in parameters:
                """MovieData = MovieData_Table().select_a_movie_all_info(info["movieId"])
                for MovieData_Dict in MovieData:
                    MovieData_Dict["movieId"] = info["movieId"]"""

                movieName = MovieData_Table().select_a_Movie_Name(info["id"])
                movie_movieId = MovieID_map_Table().select_a_movieId(info["id"])
                Movie_VoteAverage = MovieData_Table().select_a_Movie_VoteAverage(info["id"])
                Movie_VoteCount = MovieData_Table().select_a_Movie_VoteCount(info["id"])
                Movie_Overview = MovieData_Table().select_a_Movie_Overview(info["id"])
                Movie_Genres = MovieData_Table().select_a_Movie_Genres(info["id"])
                Movie_release_date = MovieData_Table().select_a_Movie_release_date(info["id"])
                Movie_Cast = MovieData_Table().select_a_Movie_Cast(info["id"])
                Movie_Crew = MovieData_Table().select_a_Movie_Crew(info["id"])
                
                Movie_dict["id"] = info["id"] # Movie's id (from MovieData_Table)
                Movie_dict["movieId"] = movie_movieId[0]# Movie's movieId (from Ratings_Table、MovieID_map_Table)
                Movie_dict["movieName"] = movieName[0]
                Movie_dict["vote_average"] = Movie_VoteAverage[0]
                Movie_dict["vote_count"] = Movie_VoteCount[0]
                Movie_dict["overview"] = Movie_Overview[0]
                Movie_dict["genres"] = Movie_Genres[0]
                Movie_dict["release_date"] = Movie_release_date[0]
                Movie_dict["cast"] = Movie_Cast[0]
                Movie_dict["crew"] = Movie_Crew[0]
                
                

                movie_list.append(Movie_dict)
                status = True
            print(movie_list)

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True): 
            reply_msg = {'status': "OK", 'parameters': movie_list}    #回傳欲query查詢的學生資訊 Nested Dictionary
        else:
            reply_msg = {'status': "Fail", 'parameters': movie_list, 'reason': "The id is not found."}
        return reply_msg
