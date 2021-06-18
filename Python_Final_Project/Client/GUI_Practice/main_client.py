from SocketClient.Socket_Client import SocketClient
from test_function.AddUser import AddUser
from test_function.Get_Movie_RS import Get_Movie_RS
from test_function.Rating import Rating
from test_function.QueryMovie import QueryMovie
from test_function.QueryUser import QueryUser

action_list = {
    "add": AddUser,
    "RS" : Get_Movie_RS,
    "rating": Rating,
    "QueryMovie": QueryMovie,
    "QU" : QueryUser
}

#======================================================================
def print_menu():
        print()
        print("add: Add a user's name")
        print("RS: Get Movie Recommemdation")
        print("rating: rating a Movie")
        print("QueryMovie: Query a Movie")
        print("QU : Query user")
        print("exit: Exit")
        selection = input("Please select: ")

        return selection
#================================================================

def main():

    client = SocketClient()
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](client).execute()
        except:
            pass

    client.client_socket.close()

main()