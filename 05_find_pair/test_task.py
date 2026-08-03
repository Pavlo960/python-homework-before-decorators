from task import find_pair


def run_tests():
    assert find_pair([2, 7, 4, 6, 3], 10) == (7, 3)
    assert find_pair([1, 2, 3], 100) is None
    assert find_pair([5, 5], 10) == (5, 5)


if __name__ == "__main__":
    run_tests()
    print("All tests passed! ✅")
