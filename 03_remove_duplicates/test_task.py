from task import remove_duplicates


def run_tests():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
    assert remove_duplicates([]) == []


if __name__ == "__main__":
    run_tests()
    print("All tests passed! ✅")
