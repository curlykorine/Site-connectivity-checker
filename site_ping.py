import sys
import time
import webbrowser

import requests
from win10toast_click import ToastNotifier
toast = ToastNotifier()

def ping_site(url):
    r = requests.head(url)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Site is available: {url}")
        return True
    else:
        return False

def open_link():
    webbrowser.open_new(i)

url = sys.argv[1]

check_list = []
check_list.append(url)
check_list.append("https://www.google.com")

while len(check_list) != 0:
    for i in check_list:
        status = ping_site(i)
        toast.show_toast(title=f"{i}", msg="Site is available", duration=3, icon_path="icon.ico", threaded=True, callback_on_click=open_link)
        while toast.notification_active():
            time.sleep(0.1)
        print(1)
        check_list.remove(i)
#url = https://stackoverflow.com/ - status_code = 200, Site is available

#url = https://stackoverflow.com/asd - status_code = 404, Site is not available

#run this programm as 'python ./site_ping.py <url>'