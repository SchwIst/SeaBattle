from abc import abstractmethod


class Input:
    @abstractmethod
    def react_to_keys(self, pressed_key: bytes):
        pass
