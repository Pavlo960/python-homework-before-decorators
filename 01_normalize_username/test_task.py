from task import normalize_username


def run_tests():
    assert normalize_username("  Oleh  ") == "oleh"
    assert normalize_username("MARIA") == "maria"
    assert normalize_username("boGDAN") == "bogdan"


if __name__ == "__main__":
    run_tests()
    print("All tests passed! ✅")
