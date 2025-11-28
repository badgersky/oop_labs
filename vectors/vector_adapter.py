from i_vector import IVector

class VectorAdapter(IVector):

    def __init__(self, vector: IVector):
        self._vector = vector

    def abs(self) -> float:
        return self._vector.abs()

    def cdot(self, v: IVector) -> float:
        x1, y1 = self._vector.get_components()
        x2, y2 = v.get_components()
        return x1 * x2 + y1 * y2

    def get_components(self) -> tuple[float, float]:
        return self._vector.get_components()