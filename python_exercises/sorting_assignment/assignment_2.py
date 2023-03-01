from random import randint
from typing import Callable

from time import time

class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def __gt__(self, other) -> bool: return self._age > other._age
    def __lt__(self, other) -> bool: return self._age < other._age
    def __eq__(self, other) -> bool: return self._name == other._name and self._age == other._age

    def __repr__(self) -> str:
        return f"P({self._name}, {self._age})"

Persons = list[Person]
def insertion_sort(items: Persons) -> Persons:
    for i in range(1, len(items)): 

        key = items[i]
        j = i - 1

        while j >= 0 and key < items[j] :
            items[j + 1] = items[j]
            j -= 1
        
        items[j + 1] = key
    
    return items

# implementing the two searches
def binsearch(items: Persons, item: Person | Callable[..., Person]) -> bool:
    if callable(item):
        item = item(items)

    while (item_len := len(items)):
        half = item_len // 2
        
        if   item > items[half]: items = items[half+1:]
        elif item < items[half]: items = items[:half]
        else:                    return True
    return False

def linsearch(items: Persons, item: Person | Callable[..., Person]) -> bool:
    if callable(item):
        item = item(items)

    for it in items:
        if it == item:
            return True
    return False

def generate_ps(length: int) -> Persons:
    return [Person('t', randint(1, 100)) for _ in range(length)]

def collect_data(file_name: str, fn: Callable, lengths: list[int], tries: int = 5):
    # [(l1, [t1, t2, ..., tn], avg), ...]
    data: list[tuple[int, list[int], float]] = []
    
    for length in lengths:
        times = []
        for _ in range(tries):
            start = time()
            fn(generate_ps(length))
            end = time()

            times.append(end - start)
        
        avg = sum(times) / len(times)
        data.append((length, times, avg))
    
    with open("python_exercises/sorting_assignment/" + file_name, 'w') as f:
        f.writelines(f"{length}, {', '.join(map(str, times))}, {avg}\n" for (length, times, avg) in data)

if __name__ == '__main__':
    scheme = {
        'bs_ls_exist': lambda ps: linsearch(ps, lambda ps: ps[-3]),
        'bs_ls_nexist': lambda ps: linsearch(ps, Person('t', 1000)),

        'as_ls_exist': lambda ps: linsearch(insertion_sort(ps), lambda ps: ps[3]),
        'as_ls_nexist': lambda ps: linsearch(insertion_sort(ps), Person('t', 1000)),
    }

    for name, fn in scheme.items():
        collect_data(f'{name}.csv', fn, [5, 10, 100, 1_000, 10_000, 30_000, 50_000, 75_000])
