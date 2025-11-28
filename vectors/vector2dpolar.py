import math
from vector2d import Vector2D

class Vector2DPolar(Vector2D):

    def __init__(self, r: float, theta: float):
        self._r = r
        self._theta = theta
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        super().__init__(x, y)

    def getAngle(self) -> float:
        return self._theta