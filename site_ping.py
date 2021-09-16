import sqlite3
import sys
import time
import webbrowser
import requests
from win10toast_click import ToastNotifier
from uuid import getnode as get_mac
from abc import ABC, abstractmethod
toast = ToastNotifier()

class Client(ABC):
    @abstractmethod
    def get_notification(self, site):
        pass

    @abstractmethod
    def add_to_check_list(self, site):
        pass

    @abstractmethod
    def del_from_check_list(self, site):
        pass

    @abstractmethod
    def update_to_check(self, site):
        pass

    @abstractmethod
    def update_not_to_check(self, site):
        pass

    @abstractmethod
    def get_check_list(self):
        pass

    @abstractmethod
    def open_link(self):
        pass

class Wnidows_Client(Client):
    def __init__(self):
        self.conn = sqlite3.connect("./database/database")  # или :memory: чтобы сохранить в RAM
        self.cursor = self.conn.cursor()
        self._list_to_check = []
        self.site_to_open = ''

    def get_notification(self, site):
        self.site_to_open = site
        toast.show_toast(title=f"{site}", msg="Site is available", duration=3, icon_path="icon.ico", threaded=True,
                         callback_on_click=self.open_link)
        while toast.notification_active():
            time.sleep(0.1)
        self.update_not_to_check(site)

    def add_to_check_list(self, site):
        self.cursor.execute(f"""INSERT INTO sites
                                VALUES('{get_mac()}', '{site}', TRUE)""")
        self.conn.commit()

    def del_from_check_list(self, site):
        self.cursor.execute(f"""DELETE FROM sites
                                WHERE site = '{site}'""")
        self.conn.commit()

    def update_to_check(self, site):
        self.cursor.execute(f"""UPDATE sites 
                                SET to_check = TRUE 
                                WHERE site = '{site}'
                                AND client = '{get_mac()}'""")
        self.conn.commit()

    def update_not_to_check(self, site):
        self.cursor.execute(f"""UPDATE sites 
                                SET to_check = FALSE 
                                WHERE site = '{site}'
                                AND client = '{get_mac()}'""")
        self.conn.commit()

    def fetch_check_list(self):
        self.cursor.execute(f"""SELECT site FROM sites 
                                WHERE to_check = TRUE
                                AND client = '{get_mac()}'""")
        rows = self.cursor.fetchall()
        new_list_to_check = []
        for i in rows:
            new_list_to_check.append(i[0])
        self._list_to_check = new_list_to_check

    def get_check_list(self):
        self.fetch_check_list()
        return self._list_to_check

    def open_link(self):
        webbrowser.open_new(self.site_to_open)

class Observer(ABC):
    class Pinger:
        @abstractmethod
        def register(self, user: Client):
            pass

        @abstractmethod
        def remove(self, user: Client):
            pass

        @abstractmethod
        def ping_site(self, url:str):
            pass

        @abstractmethod
        def send_notification(self, reciver: Client, site:str):
            pass

class Pinger(Observer):
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
                for j in i.get_check_list():
                    status = self.ping_site(j)
                    if status:
                        self.send_notification(i,j)

    def send_notification(self, reciver:Client, site):
        reciver.get_notification(site)


user = Wnidows_Client()
service = Pinger()
service.register(user)
user.del_from_check_list("https://yandex.ru/")
user.add_to_check_list("https://yandex.ru/")
user.add_to_check_list("https://yandex.ru/")
user.update_not_to_check("https://yandex.ru/")
user.update_to_check("https://yandex.ru/")
service.run()


#url = https://stackoverflow.com/ - status_code = 200, Site is available

#url = https://stackoverflow.com/asd - status_code = 404, Site is not available

#run this programm as 'python ./site_ping.py <url>'