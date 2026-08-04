def find_pair(numbers, target):
    """
    Приймає список чисел numbers і число target.
    Повертає ПЕРШУ знайдену пару чисел (як tuple з двох елементів,
    з різних позицій списку), сума яких дорівнює target.
    Якщо такої пари немає - повертає None.

    Приклади:
    find_pair([2, 7, 4, 6, 3], 10) -> (7, 3)
    find_pair([1, 2, 3], 100) -> None
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j]) 
    return None

print(find_pair([2, 7, 4, 6, 3], 10))
print(find_pair([1, 2, 3], 100)) 

