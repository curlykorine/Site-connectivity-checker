import sqlite3
import time
import subprocess, platform
from checker.Client import Client
from checker.Observer import Observer

class Pinger(Observer):
    def __init__(self, sleep = 5):
        self._to_check = True
        self._client_list = []
        self.loops_sleep = sleep

    #register user
    def register(self, user:Client):
        self._client_list.append(user)

    #remove user
    def remove(self, user:Client):
        try:
            self._client_list.remove(user)
        except:
            print("No such user")

    def ping_site(self, url):
        """
        ping site using ICMP
        :param url: valid url from database
        :return: status of pinging
        """
        #pinging site 1 time
        ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        args = "ping " + " " + ping_str + " " + url.split("/")[2]
        need_sh = False if platform.system().lower() == "windows" else True
        time.sleep(0.3)
        #if status code == 200, then write that it is available
        if subprocess.call(args, shell=need_sh) == 0:
            print(f"Site is available: {url.split('/')[2]}")
            return True
        #else print it's status code
        else:
            print(f"Site {url} is down")
            return False

    def run(self):
        print("Start to check user's checklist")
        while self._to_check:
            #iterate on each user
            for i in self._client_list:
                #iterate on each users's site
                for j in i.get_check_list():
                    #ping site
                    status = self.ping_site(j)
                    if status:
                        self.send_notification(i,j)
                print("")
                time.sleep(self.loops_sleep)

    def send_notification(self, reciver:Client, site):
        #call get_notification on Client side
        reciver.get_notification(site)