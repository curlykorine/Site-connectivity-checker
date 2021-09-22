from abc import ABC, abstractmethod
from checker.Client import Client
class Observer(ABC):
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