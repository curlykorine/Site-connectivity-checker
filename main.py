from checker.Pinger import Pinger
from checker.WindowsClient import Windows_Client
from threading import Thread

user = Windows_Client()
service = Pinger()
service.register(user)
thread = Thread(target= service.run)
thread.start()

try:
    while True:
        command = input().split()
        #ex: add https://yandex.ru/
        if command[0].lower() == "add":
            user.add_to_check_list(command[1])

        #ex: del https://www.google.ru/
        elif command[0].lower() == "del":
            user.del_from_check_list(command[1])

        #ex: update_add https://docs.google.com/ - site should be in checklist
        elif command[0].lower() == "update_add":
            try:
                user.update_to_check(command[1])
            except:
                print("site not in checklist")

        # ex: update_remove https://docs.google.com/ - site should be in checklist
        elif command[0].lower() == "update_remove":
            try:
                user.update_not_to_check(command[1])
            except:
                print("site not in checklist")

        elif command[0].lower() == "checklist":
            print("List of sites:",user.get_check_list())

        #just quit
        elif command[0].lower() == "quit":
            break

except Exception as e:
    print(e)
