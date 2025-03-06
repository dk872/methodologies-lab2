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
        self.data = [e for e in self.data if e != element]

    def __repr__(self):
        return f"{self.data}"
