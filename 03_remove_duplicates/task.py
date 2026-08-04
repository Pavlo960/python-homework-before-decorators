def remove_duplicates(items):
    """
    Приймає список, повертає НОВИЙ список без дублікатів,
    зберігаючи порядок першого входження кожного елемента.

    Приклади:
    remove_duplicates([1, 2, 2, 3, 1]) -> [1, 2, 3]
    remove_duplicates(["a", "b", "a"]) -> ["a", "b"]
    """
    return list(dict.fromkeys(items))

print(remove_duplicates([1, 2, 2, 3, 1]))
print(remove_duplicates(["a", "b", "a"]))