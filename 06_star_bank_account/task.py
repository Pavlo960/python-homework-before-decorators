def make_bank_account(starting_balance):
    """
    Повертає функцію deposit(amount).
    Кожен виклик deposit(amount) додає amount до балансу рахунку
    і повертає рядок у форматі "Balance: $X", де X - новий баланс.

    Кожен виклик make_bank_account створює СВІЙ ВЛАСНИЙ, незалежний
    рахунок - баланс одного рахунку не впливає на інший.

    Приклад:
    account = make_bank_account(100)
    account(50) -> "Balance: $150"
    account(20) -> "Balance: $170"
    """
    
    def deposit(amount):
        nonlocal starting_balance
        starting_balance += amount
        return f"Balance: ${starting_balance}"
    
    return (deposit)

account = make_bank_account(100)
account(50)
account(20)
