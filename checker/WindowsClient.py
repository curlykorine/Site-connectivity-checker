import sqlite3
import time
import webbrowser
from uuid import getnode as get_mac
from checker.Client import Client
from win10toast_click import ToastNotifier
import validators

class Windows_Client(Client):
    def __init__(self):
        self._list_to_check = []
        self.site_to_open = ''
        self.toast = ToastNotifier()

    def get_notification(self, site):
        conn = sqlite3.connect("./checker/database/database")
        self.site_to_open = site
        self.toast.show_toast(title=f"{site}", msg="Site is available", duration=3, icon_path="./checker/database/icon.ico", threaded=True,
                         callback_on_click=self.open_link)
        while self.toast.notification_active():
            time.sleep(0.1)
        conn.close()
        self.update_not_to_check(site)

    def add_to_check_list(self, site):
        try:
            if not validators.url(site):
                raise validators.ValidationFailure
            conn = sqlite3.connect("./checker/database/database")
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO sites
                                    VALUES('{get_mac()}', '{site}', TRUE)""")
            conn.commit()
            print(f"{site} was added to checklist")
            conn.close()
        except:
            print(f"{site} is incorrect URL!")

    def del_from_check_list(self, site):
        conn = sqlite3.connect("./checker/database/database")
        cursor = conn.cursor()
        cursor.execute(f"""DELETE FROM sites
                                WHERE site = '{site}'""")
        conn.commit()
        print(f"{site} was deleted from checklist")
        conn.close()

    def update_to_check(self, site):
        conn = sqlite3.connect("./checker/database/database")
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE sites 
                                SET to_check = TRUE 
                                WHERE site = '{site}'
                                AND client = '{get_mac()}'""")
        print(f"{site} will be checked from now")
        conn.commit()
        conn.close()

    def update_not_to_check(self, site):
        conn = sqlite3.connect("./checker/database/database")
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE sites 
                                SET to_check = FALSE 
                                WHERE site = '{site}'
                                AND client = '{get_mac()}'""")
        print(f"{site} will not be checked from now")
        conn.commit()
        conn.close()

    def get_check_list(self, only_marked = True):
        conn = sqlite3.connect("./checker/database/database")
        cursor = conn.cursor()
        if only_marked == True:
            to_check = "TRUE"
        else:
            to_check = "FALSE"
        cursor.execute(f"""SELECT site FROM sites 
                                WHERE to_check = {to_check}
                                AND client = '{get_mac()}'""")
        rows = cursor.fetchall()
        new_list_to_check = []
        for i in rows:
            new_list_to_check.append(i[0])
        self._list_to_check = new_list_to_check
        conn.close()
        return self._list_to_check

    def open_link(self):
        webbrowser.open_new(self.site_to_open)