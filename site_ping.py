from checker.Pinger import Pinger
from checker.WindowsClient import Windows_Client

user = Windows_Client()
service = Pinger()
service.register(user)
user.del_from_check_list("https://yandex.ru/")
user.del_from_check_list("https://www.google.ru/")
user.add_to_check_list("https://www.google.ru/")
user.add_to_check_list("https://www.overleaf.com/")
user.update_not_to_check("https://yandex.ru/")
service.run()


#url = https://stackoverflow.com/ - status_code = 200, Site is available

#url = https://stackoverflow.com/asd - status_code = 404, Site is not available

#run this programm as 'python ./site_ping.py <url>'