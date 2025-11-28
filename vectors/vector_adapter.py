import math
from i_vector import IVector
from vector3d import Vector3D

class VectorAdapter(IVector):

    def __init__(self, vector: IVector):
        self._vector = vector

    def abs(self) -> float:
        x, y, z = self.get_components()
        return (x**2 + y**2 + z**2)**0.5

    def cdot(self, v: IVector) -> float:
        x1, y1, z1 = self.get_components()
        if isinstance(v, VectorAdapter):
            x2, y2, z2 = v.get_components()
        else:
            comps = v.get_components()
            x2, y2 = comps[:2]
            z2 = comps[2] if len(comps) > 2 else 0.0
        return x1 * x2 + y1 * y2 + z1 * z2

    def cross(self, v: IVector) -> 'VectorAdapter':
        x1, y1, z1 = self.get_components()
        if isinstance(v, VectorAdapter):
            x2, y2, z2 = v.get_components()
        else:
            comps = v.get_components()
            x2, y2 = comps[:2]
            z2 = comps[2] if len(comps) > 2 else 0.0
        cx = y1 * z2 - z1 * y2
        cy = z1 * x2 - x1 * z2
        cz = x1 * y2 - y1 * x2
        return VectorAdapter(Vector3D(cx, cy, cz))
    
    def polar_coords(self) -> tuple:
        x, y, z = self.get_components()
        r = math.sqrt(x**2 + y**2 + z**2)
        if z == 0 and r != 0:
            theta = math.atan2(y, x)
            return r, theta
        elif r != 0:
            theta = math.acos(z / r)
            phi = math.atan2(y, x)
            return r, theta, phi
        else:
            return 0.0, 0.0, 0.0

    def get_components(self) -> tuple[float, ...]:
        comps = self._vector.get_components()
        if len(comps) == 2:
            return (*comps, 0.0)
        return comps