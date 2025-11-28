from vector2d import Vector2D

class Vector3D(Vector2D):

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self._z = z

    def cdot(self, v: 'Vector3D') -> float:
        x2, y2, z2 = v.get_components()
        return self._x * x2 + self._y * y2 + self._z * z2

    def cross(self, v: 'Vector3D') -> 'Vector3D':
        x1, y1, z1 = self.get_components()
        x2, y2, z2 = v.get_components()
        cx = y1 * z2 - z1 * y2
        cy = z1 * x2 - x1 * z2
        cz = x1 * y2 - y1 * x2
        return Vector3D(cx, cy, cz)

    def get_components(self) -> tuple[float, float]:
        return (self._x, self._y, self._z)