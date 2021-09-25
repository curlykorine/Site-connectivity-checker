from abc import ABC, abstractmethod
class Client(ABC):
    @abstractmethod
    def get_notification(self, site, c, conn):
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
    def update_not_to_check(self, site, c, cour):
        pass

    @abstractmethod
    def get_check_list(self, c):
        pass

    @abstractmethod
    def open_link(self):
        pass