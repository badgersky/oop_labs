import math
from vector2d import Vector2D
from vector3ddecorator import Vector3DDecorator
from vector3d import Vector3D
from vector2dpolar import Vector2DPolar
from vector_adapter import VectorAdapter

v1 = VectorAdapter(Vector2D(3, 4))
v2 = VectorAdapter(Vector2DPolar(5, math.pi / 3))
v3 = VectorAdapter(Vector3D(1, 2, 3))

vectors = [v1, v2, v3]

print("Wektory:")
for i, v in enumerate(vectors, 1):
    x, y, z = v.get_components()
    polar = v.polar_coords()        
    if len(polar) == 2:
        r, theta = polar
        print(f"v{i} - kartezjańskie: ({x:.2f}, {y:.2f}, {z:.2f}), biegunowe: (r={r:.2f}, theta={theta:.2f} rad)")
    else:
        r, theta, phi = polar
        print(f"v{i} - kartezjańskie: ({x:.2f}, {y:.2f}, {z:.2f}), biegunowe: (r={r:.2f}, theta={theta:.2f} rad, phi={phi:.2f})")

print("\nIloczyny:")
for i in range(len(vectors)):
    for j in range(i+1, len(vectors)):
        vi = vectors[i]
        vj = vectors[j]
        dot = vi.cdot(vj)
        cross = vi.cross(vj).get_components()
        print(f"v{i+1} · v{j+1} = {dot}")
        print(f"v{i+1} × v{j+1} = {cross}\n")
