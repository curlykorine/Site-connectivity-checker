from checker.Pinger import Pinger
from checker.WindowsClient import Windows_Client
from threading import Thread

user = Windows_Client()
service = Pinger(sleep=7)
service.register(user)
thread = Thread(target=service.run)
thread.start()

while True:
    try:
        command = input().split()
        # ex: add https://yandex.ru/
        if command[0].lower() == "add":
            user.add_to_check_list(command[1])

        # ex: delete https://www.google.ru/
        elif command[0].lower() == "delete":
            user.del_from_check_list(command[1])

        # ex: on https://docs.google.com/ - site has to be in the sitelist
        elif command[0].lower() == "on":
            try:
                user.update_to_check(command[1])
            except Exception:
                print("site in checklist")

        # ex: off https://docs.google.com/ - site has to be in the sitelist
        elif command[0].lower() == "off":
            try:
                user.update_not_to_check(command[1])
            except:
                print("site not in checklist")

        # shows sites which pinger is pinging
        elif command[0].lower() == "checklist":
            print("List of sites:", user.get_check_list(only_marked=True))

        # shows all sites added by user
        elif command[0].lower() == "sitelist":
            print("List of sites:", user.get_check_list(only_marked=False))

        # just quit
        elif command[0].lower() == "quit":
            service._to_check = False
            thread.join()
            break

        else:
            print("Incorrect command!")

    except KeyboardInterrupt:
        service._to_check = False
        thread.join()
        print("quit")
        break

    except Exception as e:
        print(e)
