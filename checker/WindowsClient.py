import sqlite3
import time
import webbrowser
from uuid import getnode as get_mac
from checker.Client import Client
from win10toast_click import ToastNotifier

class Windows_Client(Client):
    def __init__(self):
        self.conn = sqlite3.connect("./checker/database/database")
        self.cursor = self.conn.cursor()
        self._list_to_check = []
        self.site_to_open = ''
        self.toast = ToastNotifier()

    def get_notification(self, site, c, cour):
        self.site_to_open = site
        self.toast.show_toast(title=f"{site}", msg="Site is available", duration=3, icon_path="./checker/database/icon.ico", threaded=True,
                         callback_on_click=self.open_link)
        while self.toast.notification_active():
            time.sleep(0.1)
        self.update_not_to_check(site, c, cour)

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

    def update_not_to_check(self, site, c , cour):
        cour.execute(f"""UPDATE sites 
                                SET to_check = FALSE 
                                WHERE site = '{site}'
                                AND client = '{get_mac()}'""")
        c.commit()

    def get_check_list(self, c):
        c.execute(f"""SELECT site FROM sites 
                                WHERE to_check = TRUE
                                AND client = '{get_mac()}'""")
        rows = c.fetchall()
        new_list_to_check = []
        for i in rows:
            new_list_to_check.append(i[0])
        self._list_to_check = new_list_to_check
        return self._list_to_check

    def open_link(self):
        webbrowser.open_new(self.site_to_open)