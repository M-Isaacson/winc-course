def main():
    test_dict = {"a": 2, "b": 4, "c": {"d": 1, "e": 3}, "f": 5, "g": {"h": 6, "i": {"j": 7, "k": 8, "l": {"m": 9}}}}
    print(flatten_dict(test_dict))


def get_none():
    return None


def flatten_dict(my_dict: dict) -> list:
    the_list = []

    def do_flatten_dict(my_dict):
        for value in my_dict.values():
            if isinstance(value, dict):
                do_flatten_dict(value)
            else:
                the_list.append(value)

    do_flatten_dict(my_dict)
    return the_list


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    main()
