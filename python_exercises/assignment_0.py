
# question 1
def shipping_cost(weight: int) -> float:
    extra = 0

    if 25 <= weight < 50:
        extra = 10
    elif 50 <= weight < 100:
        extra = 15
    elif 100 <= weight:
        extra = 30
    
    return extra + (0.1 * weight)

# question 2
def even_odd(array: list[int]) -> tuple[int, int]:
    return (
        sum(i for i in array if i % 2 == 0),
        sum(i for i in array if i % 2 == 1)
    )

# alternate implementation of question 2
def even_odd_alternate(array: list[int]) -> tuple[int, int]:
    esum, osum = 0, 0
    
    n = 0
    while n < len(array):
        am = array[n]

        if   am % 2 == 0: esum += am
        elif am % 2 == 1: osum += am
    
        n += 1
    
    return esum, osum

# question 3:
class Item:
    def __init__(self, name: str, section: str, price: float) -> None:
        # private attributes (can use double underscore for more safety, but unnecessary)
        self._name = name
        self._section = section
        self._price = price
    
    def __imul__(self, other: float):
        self._price *= other
        return self
    
    def __iadd__(self, other: float):
        self._price += other
        return self
    
    def __str__(self) -> str:
        capitalized_name = self._name.capitalize()
        return f"{capitalized_name} costs {self._price} and can be found in {self._section}."

# test cases
if __name__ == '__main__':
    # question 1
    print(*(
        f"{amount} pound -> ${shipping_cost(amount)}"
        for amount in (30, 56, 110)
    ), sep='\n')

    # question 2
    print('\n', *(
        f"{ls} -> {even_odd(ls)}"
        for ls in (
            [1, 4, 3, 6, 2],
            [2, 6, 1, 3, 5]
        )
    ), sep='\n')

    # question 3
    percent = lambda n: n / 100
    milk = Item('milk', 'groceries', 4.99)
    
    milk += 10 # adds 10 dollars
    milk *= percent(120) # increases by 120 percent

    print(milk)
