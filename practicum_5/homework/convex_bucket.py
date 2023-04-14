from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    clockwise_sorted_ch = []

    def right_turn(p1, p2, p3):
        return np.cross(p2 - p1, p3 - p1) <= 0

    def build_bucket(sorted_points):
        hull = []
        for point in sorted_points:
            while len(hull) >= 2 and right_turn(hull[-2], hull[-1], point):
                hull.pop()
            hull.append(point)
        return hull

    shell = build_bucket(sorted(points, key=lambda x: x[0]))
    return np.array(shell + shell[-2::-1])

if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"practicum_5/homework/points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
