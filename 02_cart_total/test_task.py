from task import cart_total


def run_tests():
    assert cart_total(10, 20, 5) == "Total: $35"
    assert cart_total() == "Total: $0"
    assert cart_total(99) == "Total: $99"


if __name__ == "__main__":
    run_tests()
    print("All tests passed! ✅")
