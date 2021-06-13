import numpy as np

from utils import Display


class Ship(Display):
    size: int
    position: np.ndarray
    is_horizontal: bool

    def __init__(self, size: int, position: np.ndarray):
        self.size = size
        self.position = position
        self.is_horizontal = True

    def move(self, vector: np.ndarray):
        self.position += vector

    def _get_vector(self) -> np.ndarray:
        vector = np.array([0, 0])

        if self.is_horizontal:
            vector[0] = 1
        else:
            vector[1] = 1

        return vector

    def get_all_coords(self) -> np.ndarray:
        vector = self._get_vector()

        positions = np.ndarray([
            vector * i + self.position
            for i in range(self.size)
        ])

        return positions

    def get_padding_coords(self) -> np.ndarray:
        vector = self._get_vector()

        vector_v = np.array([0, 1])
        vector_h = np.array([1, 0])

        padding_positions = []

        for i in range(-1, self.size + 1):
            for j in range(-1, 1 + 1):
                if self.is_horizontal:
                    vector_v * j + vector_h * i + self.position
                else:
                    vector_v * i + vector_h * j + self.position

        padding_positions = np.ndarray(padding_positions)

        return padding_positions
