from abc import ABC, abstractmethod


class Estado(ABC):

    @abstractmethod
    def mouse_press(self, controlador, event):
        pass

    @abstractmethod
    def mouse_move(self, controlador, event):
        pass

    @abstractmethod
    def mouse_release(self, controlador, event):
        pass