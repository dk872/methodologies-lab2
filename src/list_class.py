class List:
    def __init__(self):
        self.data = []

    def length(self) -> int:
        return len(self.data)

    def append(self, element: chr) -> None:
        self.data.append(element)

    def insert(self, element: chr, index: int) -> None:
        if not (0 <= index <= len(self.data)):
            raise IndexError("Index out of range")
        self.data.insert(index, element)

    def delete(self, index: int) -> chr:
        if not (0 <= index < len(self.data)):
            raise IndexError("Index out of range")
        return self.data.pop(index)

    def delete_all(self, element: chr) -> None:
        self.data = [e for e in self.data if e == element]

    def get(self, index: int) -> chr:
        if not (0 <= index < len(self.data)):
            raise IndexError("Index out of range")
        return self.data[index]

    def clone(self) -> "List":
        new_list = List()
        new_list.data = self.data.copy()
        return new_list

    def reverse(self) -> None:
        self.data.reverse()

    def find_first(self, element: chr) -> int:
        try:
            return self.data.index(element)
        except ValueError:
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
