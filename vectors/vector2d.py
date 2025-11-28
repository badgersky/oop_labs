import math
from i_vector import IVector

class Vector2D(IVector):

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def abs(self) -> float:
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def cdot(self, v: IVector) -> float:
        x2, y2 = v.get_components()
        return self._x * x2 + self._y * y2

    def get_components(self) -> tuple[float, float]:
        return (self._x, self._y)