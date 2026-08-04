def count_words(sentence):
    """
    Приймає речення (рядок), повертає словник, де ключ - слово,
    значення - скільки разів це слово зустрічається у реченні.
    Слова розділені пробілами.

    Приклад:
    count_words("cat dog cat bird dog cat") -> {"cat": 3, "dog": 2, "bird": 1}
    """
    counts = {}
    result = sentence.split()
    for word in result:
        if word in counts:
            counts[word] += 1
        else: counts[word] = 1
    return counts

print(count_words("cat dog cat bird dog cat"))
            
