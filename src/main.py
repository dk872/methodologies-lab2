from list_class import List
from demo_functions import demo_append, demo_insert

def main():
    lst = List()
    print("Initial list:", lst)

    demo_append(lst)
    demo_insert(lst)


if __name__ == "__main__":
    main()
