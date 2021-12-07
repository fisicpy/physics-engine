# import modules
from abc import ABC, abstractmethod


class AbstractObjectClass(ABC):
    @abstractmethod
    def draw(self):
        pass
