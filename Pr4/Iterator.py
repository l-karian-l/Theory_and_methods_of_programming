class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = self.data[self.index]
        self.index += 1
        return value


class MyCollection:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def __iter__(self):
        return MyIterator(self.data)


# Пример использования

collection = MyCollection()
collection.add_item("Apple")
collection.add_item("Banana")
collection.add_item("Cherry")

print("Items in collection:")
for item in collection:
    print(item)