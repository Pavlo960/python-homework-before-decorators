def cart_total(*prices):
    """
    Приймає довільну кількість цін товарів (числа) і повертає рядок
    у форматі "Total: $X", де X - сума всіх цін.

    Приклади:
    cart_total(10, 20, 5) -> "Total: $35"
    cart_total() -> "Total: $0"
    """
    total = sum(prices)
    return f"Total: ${total}"

print(cart_total(10, 20, 5))
print(cart_total())


