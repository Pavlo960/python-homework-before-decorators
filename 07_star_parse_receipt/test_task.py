from task import parse_receipt


def run_tests():
    assert parse_receipt(["apple:10", "bread:5", "apple:10"]) == {"apple": 20, "bread": 5}
    assert parse_receipt(["milk:3"]) == {"milk": 3}


if __name__ == "__main__":
    run_tests()
    print("All tests passed! ✅")
