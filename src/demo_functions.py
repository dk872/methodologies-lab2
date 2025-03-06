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


def demo_delete_all(lst: List):
    lst.delete_all('b')
    print("After deleting all 'b':", lst)


def demo_get(lst: List):
    element = lst.get(0)
    print("Element at index 0:", element)


def demo_clone(lst: List):
    cloned_list = lst.clone()
    print("Cloned list:", cloned_list)


def demo_reverse(lst: List):
    lst.reverse()
    print("After reversing:", lst)


def demo_find_first(lst: List):
    print("First index of 'c':", lst.find_first('c'))
