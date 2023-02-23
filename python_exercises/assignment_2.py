#%%
from random import randint
from typing import Callable, Iterable 

from time import time

class Point:
    def __init__(self, x: int | float, y: int | float) -> None:
        self._x = x
        self._y = y

    @classmethod
    def generate_points(cls, amount: int) -> 'Points':
        return [
            cls(x=randint(1, 100), y=randint(1, 100))
            for _ in range(amount)
        ]

    # the comparison operator (op) is defined as follows:
    # [a b] op [c d] = `a op c` and `b op d`
    def __gt__(self, other) -> bool:
        return self._x > other._x and self._y > other._y

    def __lt__(self, other) -> bool:
        return self._x < other._x and self._y < other._y
    
    def __repr__(self) -> str:
        return f'[{self._x} {self._y}]'
    
Points = list[Point]
def data_collector(runs: int) -> Callable:
    def inner(f: Callable[..., Points]) -> Callable:
    
        def wrapper(ls: Points) -> tuple[Points, float]:
            store = []
            
            for _ in range(runs):
                start = time(); f(ls); end = time()
                store.append(end - start)
            
            avg = sum(store) / len(store)
            
            return (f(ls), avg)        
        return wrapper
    return inner

@data_collector(runs=100)
def bubble_sort(points: Points) -> Points:
    for _ in range(len(points) - 1):
        for i in range(len(points) - 1):
    
            if points[i + 1] < points[i]:
                points[i], points[i + 1] = points[i + 1], points[i]
    
    return points

@data_collector(runs=100)
def selection_sort(points: Points) -> Points:
    for marker in range(len(points)):
        min_index = marker

        for i in range(marker, len(points)):
            if points[i] < points[min_index]:
                min_index = i
        
        points[marker], points[min_index] = points[min_index], points[marker]
    
    return points

if __name__ == '__main__':
    from matplotlib import pyplot as plt

    def collect_for(arr_lens: Iterable[int], function: Callable[[Points], Points]) -> list[tuple]:
        return [
            (arr_len, function(Point.generate_points(arr_len))[1])
            for arr_len in arr_lens
        ]
    
    data = collect_for(range(200), selection_sort)
    x, y = zip(*data)

    plt.plot(x, y)
    plt.show()
# %%
