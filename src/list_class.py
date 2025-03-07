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
        self.data = [e for e in self.data if e != element]

    def get(self, index: int) -> chr:
        if self.head is None:
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
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == element:
                return i
        return -1

    def clear(self) -> None:
        self.data.clear()

    def extend(self, elements: "List") -> None:
        self.data.extend(elements.data.copy())

    def __repr__(self):
        return f"{self.data}"
