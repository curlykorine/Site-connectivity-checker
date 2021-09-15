import sys
import time
import webbrowser

import requests
from win10toast_click import ToastNotifier
toast = ToastNotifier()


class Client:
    def __init__(self):
        self._list_to_check = []

    def get_notification(self, site):
        toast.show_toast(title=f"{site}", msg="Site is available", duration=3, icon_path="icon.ico", threaded=True,
                         callback_on_click=self.send_notification)
        while toast.notification_active():
            time.sleep(0.1)
        self.del_from_check_list(site)

    def update_check_list(self, site):
        self._list_to_check.append(site)

    def del_from_check_list(self, site):
        self._list_to_check.remove(site)

    def get_check_list(self):
        pass

    def open_link(self):
        webbrowser.open_new(i)
    url = sys.argv[1]


class Pinger:
    def __init__(self):
        self._client_list = []

    def register(self, user:Client):
        self._client_list.append(user)

    def remove(self, user:Client):
        try:
            self._client_list.remove(user)
        except:
            print("No such user")

    def ping_site(self, url):
        r = requests.head(url)
        print(r.status_code)
        if r.status_code == 200:
            print(f"Site is available: {url}")
            return True
        else:
            return False

    def run(self):
        while len(self._client_list) != 0:
            for i in self._client_list:
                for j in range(len(i.get_check_list())):
                    status = self.ping_site(j)
                    if status:
                        self.send_notification(i, j)

    def send_notification(self, reciver:Client, site):
        reciver.get_notification(site)



check_list = []
check_list.append(url)
check_list.append("https://www.google.com")


#url = https://stackoverflow.com/ - status_code = 200, Site is available

#url = https://stackoverflow.com/asd - status_code = 404, Site is not available

#run this programm as 'python ./site_ping.py <url>'