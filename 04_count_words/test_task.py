from task import count_words


def run_tests():
    assert count_words("cat dog cat bird dog cat") == {"cat": 3, "dog": 2, "bird": 1}
    assert count_words("hi") == {"hi": 1}


if __name__ == "__main__":
    run_tests()
    print("All tests passed! ✅")
