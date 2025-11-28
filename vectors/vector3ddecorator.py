from vector2d import Vector2D

class Vector3DDecorator(Vector2D):

    def __init__(self, base_vector: Vector2D, z: float):
        self._base = base_vector
        self._z = z

    def abs(self) -> float:
        x, y, z = self.get_components_3d()
        return (x**2 + y**2 + z**2)**0.5

    def get_components(self) -> tuple[float, float, float]:
        return (self.get_x(), self.get_y(), self._z)

    def cdot(self, other: 'Vector3DDecorator') -> float:
        x1, y1, z1 = self.get_components()
        x2, y2, z2 = other.get_components()
        return x1 * x2 + y1 * y2 + z1 * z2

    def cross(self, other: 'Vector3DDecorator') -> 'Vector3DDecorator':
        x1, y1, z1 = self.get_components()
        x2, y2, z2 = other.get_components()
        cx = y1 * z2 - z1 * y2
        cy = z1 * x2 - x1 * z2
        cz = x1 * y2 - y1 * x2
        return Vector3DDecorator(self._base.__class__(cx, cy), cz)