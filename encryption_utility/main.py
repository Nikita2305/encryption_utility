from config import *
from commands import *


def user_loop():
    commands = {
        "encrypt": encrypt,
        "decrypt": decrypt,
        "exit": exit,
        "wrong_query": wrong_query
    }
    while (is_active()):
        print("Waiting for the query:")
        query_string = ' '.join(input().split())
        query_arr = query_string.split()
        query = query_arr[0]
        args = query_arr[1:]
        if (not (query in commands.keys())):
            query = "wrong_query"
            args = [commands.keys()]
        response = commands[query](*args)
        print_response(response)
        print()

user_loop()
