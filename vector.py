#! /usr/bin/env python

"""
functions to work with vectors

 - add
 - subtract
 - scale
 - dot

if run when __name__ == "__main__"
input
  None
output
  None if tests passed, exception if tests not passed
"""

from typing import List

# create Vector type for type hinting
Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    "add two vectors"
    assert len(v) == len(w), "vectors must be the same length!"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    "subtract two vectors"
    assert len(v) == len(w), "vectors must be the same length!"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def scale(c: float, v: Vector) -> Vector:
    "scale a vector v by a scalar c"
    assert isinstance(c, (int, float)), "need a scalar!"
    return [c * v_i for v_i in v]


def dot(v: Vector, w: Vector) -> float:
    "compute dot product of 2 vectors"
    assert len(v) == len(w), "vectors must be the same lenght!"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


if __name__ == "__main__":
    print("Running tests")
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    assert add(v1, v2) == [5, 7, 9], "something wrong with add"
    assert subtract(v1, v2) == [-3, -3, -3], "something wrong with subtract"
    assert scale(2, v1) == [2, 4, 6], "something wrong with scale"
    assert dot(v1, v1) == 14, "something wrong with dot"
    print("tests now finished")
