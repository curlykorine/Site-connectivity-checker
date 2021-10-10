import pytest
from checker.Pinger import Pinger
from checker.WindowsClient import Windows_Client
import sqlite3
import os
from uuid import getnode as get_mac


class TestPinger():
    @pytest.mark.parametrize('url', ['https://www.microsoft.com/'])
    def test_ping_url(self, url):
        pinger = Pinger()
        assert pinger.ping_site(url=url) == True

    @pytest.mark.parametrize('url', ['https://www.microsoft.com/'])
    def test_get_notification(self, url):
        pinger = Pinger()
        client = Windows_Client()
        pinger.send_notification(client, url)

    def test_register(self):
        pinger = Pinger()
        client = Windows_Client()
        pinger.register(client)
        assert pinger._client_list.__len__() == 1

    def test_remove(self):
        pinger = Pinger()
        client = Windows_Client()
        pinger.register(client)
        pinger.remove(client)
        assert pinger._client_list.__len__() == 0


class TestClient():
    @pytest.fixture(scope='function')
    def define_db(self):
        path = "./mock_db"
        my_file = open(path, "w")
        my_file.close()
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE sites(
           client TEXT,
           site TEXT,
           to_check BOOLEAN);
        """)
        cursor.execute(f"""INSERT INTO sites
                        VALUES('{get_mac()}', 'https://pythonru.com/', TRUE)""")
        conn.commit()
        cursor.execute(f"""INSERT INTO sites
                                        VALUES('{get_mac()}', 'https://moodle_fake_test.com/', TRUE)""")
        conn.commit()
        cursor.execute(f"""INSERT INTO sites
                                        VALUES('{get_mac()}', 'https://habr.com/', FALSE )""")
        conn.commit()
        yield path
        conn.close()
        os.remove("./mock_db")

    def test_add_to_check_list_valid(self, define_db):
        conn = sqlite3.connect(define_db)
        cursor = conn.cursor()
        client = Windows_Client(path=define_db)
        cursor.execute(f"""SELECT site FROM sites 
                                                WHERE client = '{get_mac()}'""")
        length = cursor.fetchall().__len__()
        client.add_to_check_list(site='https://www.youtube.com/')
        cursor.execute(f"""SELECT site FROM sites 
                                                    WHERE client = '{get_mac()}'""")
        assert cursor.fetchall().__len__() == length + 1

    def test_delete_to_check_list_valid(self, define_db):
        conn = sqlite3.connect(define_db)
        cursor = conn.cursor()
        client = Windows_Client(path=define_db)
        cursor.execute(f"""SELECT site FROM sites 
                                                WHERE client = '{get_mac()}'""")
        length = cursor.fetchall().__len__()
        client.del_from_check_list(site='https://pythonru.com/')
        cursor.execute(f"""SELECT site FROM sites 
                                                    WHERE client = '{get_mac()}'""")
        assert cursor.fetchall().__len__() == length - 1

    def test_mark_site_to_check_valid(self, define_db):
        conn = sqlite3.connect(define_db)
        cursor = conn.cursor()
        client = Windows_Client(path=define_db)
        cursor.execute(f"""SELECT site FROM sites 
                                                WHERE client = '{get_mac()}'
                                                AND to_check = TRUE""")
        length = cursor.fetchall().__len__()
        client.update_to_check(site='https://habr.com/')
        cursor.execute(f"""SELECT site FROM sites 
                                                    WHERE client = '{get_mac()}'
                                                    AND to_check = TRUE""")
        assert cursor.fetchall().__len__() == length + 1

    def test_mark_site_not_to_check_valid(self, define_db):
        conn = sqlite3.connect(define_db)
        cursor = conn.cursor()
        client = Windows_Client(path=define_db)
        cursor.execute(f"""SELECT site FROM sites 
                                                    WHERE client = '{get_mac()}'
                                                    AND to_check = FALSE""")
        length = cursor.fetchall().__len__()
        client.update_not_to_check(site='https://pythonru.com/')
        cursor.execute(f"""SELECT site FROM sites 
                                                        WHERE client = '{get_mac()}'
                                                        AND to_check = FALSE""")
        assert cursor.fetchall().__len__() == length + 1

    def test_get_check_list(self, define_db):
        client = Windows_Client(path=define_db)
        array = client.get_check_list(True)
        length = array.__len__()
        assert length == 2

    def test_get_site_list(self, define_db):
        client = Windows_Client(path=define_db)
        array = client.get_check_list(False)
        length = array.__len__()
        assert length == 3
