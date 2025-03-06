from list_class import List
from demo_functions import (
    demo_append, demo_insert, demo_length, demo_delete)


def main():
    lst = List()
    print("Initial list:", lst)

    demo_append(lst)
    demo_insert(lst)
    demo_length(lst)
    demo_delete(lst)


if __name__ == "__main__":
    main()
