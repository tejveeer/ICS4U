from random import randint
from typing import Callable, TypeVar

from pprint import pprint
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
def binsearch(items: Persons, item: Person) -> bool:
    left, right = 0, len(items) - 1

    while left <= right:
        middle = (left + right) // 2

        if items[middle] == item:
            return True

        if items[middle] < item:
            left = middle + 1
        elif items[middle] > item:
            right = middle - 1
    
    return False

def linsearch(items: Persons, item: Person) -> bool:    
    for it in items:
        if it == item:
            return True
    return False

if __name__ == '__main__':
    def generate_ps(length: int) -> Persons:
        """Given a length, this function generates a list of Persons"""
        return [Person('t', randint(1, 100)) for _ in range(length)]

    RT = TypeVar('RT')    
    def get_average(runs: int, fn: Callable[..., RT], *args) -> tuple[RT, float]:
        """Given a function, its respective arguments, and the amount of times to run the function, this function collects the average amount of time taken for the computation of the provided function."""
        store = []
        res = None

        for _ in range(runs):
            start = time()
            r = fn(args[0].copy())
            end = time()

            store.append(end - start)

            if not res:
                res = r
        
        return (res, sum(store) / len(store))

    def data_collector(arrays: list[Persons], fn: Callable[..., RT]) -> list[tuple[RT, float]]:
        """Given an array of Persons (which would be list of Person) and a function, this function will iterate through all the arrays within the given arrays and get the average time it takes to run them as well as the result."""
        return [
            get_average(5, fn, array)
            for array in arrays
        ]
    
    def data_saver(file_name: str, av_times: list[float]) -> None:
        """Given a file name and a set of average times, this function will construct a CSV file."""

        with open('python_exercises/sorting_assignment/' + file_name, 'w') as f:
            f.writelines(['length, time\n'] + 
                         [f"{length}, {av_time}\n" for (length, av_time) in zip(lengths, av_times)])
    
    def get_second(L: list[tuple]):
        """
        Gets all the second elements in the tuples

        ((1, 2), (3, 4)) --> [2, 4]
        """
        return [b for (_, b) in L]
    
    def generate_files(time_data: dict[str, list[tuple[RT, float]]]) -> None:
        """Given a dictionary which stores computed data of the functions (insertion, sorted, binary, linear), this function will generate the respective files for that function's data."""

        for name, data in time_data.items():
            if '|' not in name:
                file_name = name + '.csv'
            else:
                left, right = [sentence.split() for sentence in name.split('|')]
                file_name = ''.join(word[0] for word in left) + ' ' + '_'.join(right) + '.csv'

            times = get_second(data)
            data_saver(file_name, times)

    # time to do the dirty work
    lengths = [5, 10, 100, 1_000, 10_000, 30_000, 50_000, 75_000]
    arrays = [generate_ps(length) for length in lengths]

    sort_times = {
        'insertion sort': data_collector(arrays, insertion_sort),
        'python builtin': data_collector(arrays, sorted)
    }

    generate_files(sort_times)
    
    # collect the sorted arrays from the `sort_times` so that it can be used later
    s_arrays = [result for (result, _) in sort_times['python builtin']]

    # a person with age=10000 doesn't exist in the arrays since the generation is limited to [1, 100]
    not_exist = Person('t', 10000)
    search_times = {
        'linear search before sort | exists': data_collector(arrays, lambda ps: linsearch(ps, ps[-1])),
        'linear search before sort | not exists': data_collector(arrays, lambda ps: linsearch(ps, not_exist)),

        'linear search after sort | exists': data_collector(s_arrays, lambda ps: linsearch(ps, ps[-1])),
        'linear search after sort | not exists': data_collector(s_arrays, lambda ps: linsearch(ps, not_exist)),

        'binary search after sort | exists': data_collector(s_arrays, lambda ps: binsearch(ps, ps[-1])),
        'binary search after sort | not exists': data_collector(s_arrays, lambda ps: binsearch(ps, not_exist)),
    }

    generate_files(search_times)