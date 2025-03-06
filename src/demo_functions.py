from list_class import List


def demo_append(lst: List):
    lst.append('a')
    lst.append('c')
    lst.append('b')
    lst.append('c')
    lst.append('b')
    print("After appending elements:", lst)


def demo_insert(lst: List):
    lst.insert('x', 1)
    print("After inserting 'x' at index 1:", lst)


def demo_length(lst: List):
    length = lst.length()
    print("The number of list items:", length)


def demo_delete(lst: List):
    removed = lst.delete(0)
    print(f"Deleted element at index 0: {removed}. Result:", lst)
