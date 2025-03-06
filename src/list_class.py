class List:
    def __init__(self):
        self.data = []

    def append(self, element: chr) -> None:
        self.data.append(element)

    def __repr__(self):
        return f"{self.data}"
