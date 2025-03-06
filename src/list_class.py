class List:
    def __init__(self):
        self.data = []

    def append(self, element: chr) -> None:
        self.data.append(element)

    def insert(self, element: chr, index: int) -> None:
        if not (0 <= index <= len(self.data)):
            raise IndexError("Index out of range")
        self.data.insert(index, element)

    def __repr__(self):
        return f"{self.data}"
