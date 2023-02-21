from random import randint
from typing import Callable
from pprint import pprint

from time import time

class Point:
    def __init__(self, x: int | float, y: int | float) -> None:
        self._x = x
        self._y = y

    # the comparison operator (op) is defined as follows:
    # [a b] op [c d] = `a op c` and `b op d`
    def __gt__(self, other) -> bool:
        return self._x > other._x and self._y > other._y

    def __lt__(self, other) -> bool:
        return self._x < other._x and self._y < other._y
    
    def __repr__(self) -> str:
        return f'[{self._x} {self._y}]'
    
Points = list[Point]

def data_collector(amount: int) -> Callable:
    def inner(f: Callable[..., Points]) -> Callable:
    
        def wrapper(ls: Points) -> tuple[Points, float]:
            store = []
            
            for _ in range(amount):
                start = time()
                sort = f(ls)
                end = time()

                store.append(end - start)
            
            avg = sum(store) / len(store)
            return (sort, avg)
        
        return wrapper
    return inner

@data_collector(amount=100)
def bubble_sort(points: Points) -> Points:
    for _ in range(len(points) - 1):
        for i in range(len(points) - 1):
            if points[i + 1] < points[i]:
                points[i], points[i + 1] = points[i + 1], points[i]
    return points

@data_collector(amount=100)
def selection_sort(points: Points) -> Points:
    for marker in range(len(points)):
        min_index = marker

        for i in range(marker, len(points)):
            if points[i] < points[min_index]:
                min_index = i
        
        points[marker], points[min_index] = points[min_index], points[marker]
    
    return points

def generate_random_points(amount: int) -> Points:
    return [
        Point(x=randint(1, 100), y=randint(1, 100))
        for _ in range(amount)
    ]

pprint(
    bubble_sort(generate_random_points(100)),
)