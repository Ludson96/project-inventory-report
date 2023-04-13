from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data) -> None:
        self.data = data
        self.current = 0

    def __next__(self):
        product = self.data[self.current]

        if self.current == (len(self.data) - 1):
            raise StopIteration()

        self.current += 1
        return product
