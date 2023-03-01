
def binsearch(items: list[int], item: int) -> bool:
    while (item_len := len(items)):
        half = item_len // 2
        
        if   item > items[half]: items = items[half+1:]
        elif item < items[half]: items = items[:half]
        else:                    return True
    return False