import sqlite3
import time

import requests
from checker.Client import Client
from checker.Observer import Observer

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
        #pinging site 1 time
        r = requests.head(url)
        time.sleep(0.5)
        #if status code == 200, then write that it is available
        if r.status_code == 200:
            print(f"Site is available: {url}")
            return True
        #else print it's status code
        else:
            print(f"Site {url} is not available, status code = {r.status_code}")
            return False

    def run(self):
        self.conn = sqlite3.connect("./checker/database/database")
        self.cursor = self.conn.cursor()
        while len(self._client_list) != 0:
            #iterate on each user
            for i in self._client_list:
                #iterate on each users's site
                for j in i.get_check_list(self.cursor):
                    #ping site
                    status = self.ping_site(j)
                    if status:
                        self.send_notification(i,j)
                time.sleep(3)

    def send_notification(self, reciver:Client, site):
        #call get_notification on Client side
        reciver.get_notification(site, self.conn, self.cursor)