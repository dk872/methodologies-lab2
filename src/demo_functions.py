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
