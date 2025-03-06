from list_class import List
from demo_functions import (
    demo_append, demo_insert, demo_length, demo_delete,
    demo_delete_all, demo_get, demo_clone)


def main():
    lst = List()
    print("Initial list:", lst)

    demo_append(lst)
    demo_insert(lst)
    demo_length(lst)
    demo_delete(lst)
    demo_delete_all(lst)
    demo_get(lst)
    demo_clone(lst)


if __name__ == "__main__":
    main()
