from task import make_bank_account


def run_tests():
    account = make_bank_account(100)
    assert account(50) == "Balance: $150"
    assert account(20) == "Balance: $170"

    account2 = make_bank_account(0)
    assert account2(10) == "Balance: $10"
    # make sure accounts are independent of each other
    assert account(0) == "Balance: $170"


if __name__ == "__main__":
    run_tests()
    print("All tests passed! ✅")
