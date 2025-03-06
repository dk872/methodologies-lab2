from list_class import List


def demo_append(lst: List):
    lst.append('a')
    lst.append('c')
    lst.append('b')
    lst.append('c')
    lst.append('b')
    print("After appending elements:", lst)