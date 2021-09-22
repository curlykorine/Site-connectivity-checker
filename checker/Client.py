from abc import ABC, abstractmethod
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