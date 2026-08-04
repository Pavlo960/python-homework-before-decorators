def normalize_username(username):
    """
    Приймає рядок з іменем користувача (можливо, з зайвими пробілами
    з країв і в довільному регістрі).
    Повертає рядок без пробілів з країв, усі літери малі.

    Приклади:
    normalize_username("  Oleh  ") -> "oleh"
    normalize_username("MARIA") -> "maria"
    """
    result = username.strip().lower()
    return result

print(normalize_username("  Oleh  "))
print(normalize_username("MARIA"))
