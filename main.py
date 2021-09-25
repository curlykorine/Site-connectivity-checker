from checker.Pinger import Pinger
from checker.WindowsClient import Windows_Client
from threading import Thread

user = Windows_Client()
service = Pinger()
service.register(user)
thread = Thread(target= service.run)
thread.start()

while True:
    command = input().split()
    #ex: add https://yandex.ru/
    if command[0].lower() == "add":
        user.add_to_check_list(command[1])

    #ex: delete https://www.google.ru/
    elif command[0].lower() == "delete":
        user.del_from_check_list(command[1])

    #ex: on https://docs.google.com/ - site should be in checklist
    elif command[0].lower() == "on":
        try:
            user.update_to_check(command[1])
        except:
            print("site not in checklist")

    # ex: off https://docs.google.com/ - site should be in checklist
    elif command[0].lower() == "off":
        try:
            user.update_not_to_check(command[1], user.conn, user.cursor)
        except:
            print("site not in checklist")

    # ex: checklist        
    elif command[0].lower() == "checklist":
        print("List of sites:",user.get_check_list(user.cursor))
        
    # ex: quit
    elif command[0].lower() == "quit":
        break
