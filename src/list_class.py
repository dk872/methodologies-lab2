class Node:
    def __init__(self, value: chr):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def length(self) -> int:
        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def append(self, element: chr) -> None:
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert(self, element: chr, index: int) -> None:
        if index < 0 or index > self.length():
            raise IndexError("Index out of range")

        new_node = Node(element)

        if index == 0:
            if not self.head:
                self.head = new_node
                self.head.next = self.head
            else:
                new_node.next = self.head
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = new_node
                self.head = new_node
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete(self, index: int) -> chr:
        if index < 0 or index >= self.length():
            raise IndexError("Index out of range")

        current = self.head

        if index == 0:
            if self.head.next == self.head:
                removed_value = self.head.value
                self.head = None
                return removed_value

            while current.next != self.head:
                current = current.next
            removed_value = self.head.value
            current.next = self.head.next
            self.head = self.head.next
            return removed_value

        prev = None
        for _ in range(index):
            prev = current
            current = current.next

        removed_value = current.value
        prev.next = current.next
        return removed_value

    def delete_all(self, element: chr) -> None:
        if not self.head:
            return

        while self.head and self.head.value == element:
            if self.head.next == self.head:
                self.head = None
                return
            self.head = self.head.next

        current = self.head

        while current and current.next != self.head:
            if current.next.value == element:
                current.next = current.next.next
            else:
                current = current.next

    def get(self, index: int) -> chr:
        if self.head is None or index < 0:
            raise IndexError("Index out of range")

        current = self.head
        count = 0

        while count < index:
            current = current.next
            count += 1

            if current == self.head:
                raise IndexError("Index out of range")

        return current.value

    def clone(self) -> "List":
        new_list = List()
        if not self.head:
            return new_list

        current = self.head
        while True:
            new_list.append(current.value)
            current = current.next
            if current == self.head:
                break

        return new_list

    def reverse(self) -> None:
        if not self.head or self.head.next == self.head:
            return

        prev = None
        current = self.head
        first = self.head

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == first:
                break

        self.head.next = prev
        self.head = prev

    def find_first(self, element: chr) -> int:
        if not self.head:
            return -1

        current = self.head
        index = 0

        while True:
            if current.value == element:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break

        return -1

    def find_last(self, element: chr) -> int:
        if not self.head:
            return -1

        current = self.head
        last_index = -1
        count = 0

        while True:
            if current.value == element:
                last_index = count
            current = current.next
            count += 1
            if current == self.head:
                break

        return last_index

    def clear(self) -> None:
        self.head = None

    def extend(self, elements: "List") -> None:
        if not elements.head:
            return

        current = elements.head
        while True:
            self.append(current.value)
            current = current.next
            if current == elements.head:
                break

    def __repr__(self):
        if self.head is None:
            return "[]"

        elements = []
        current = self.head

        while True:
            elements.append(repr(current.value))
            current = current.next
            if current == self.head:
                break

        return "[" + " -> ".join(elements) + "]"

