class book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
    def __len__(self):
        return int(self.pages)

b = book("hello", 10000)

print(len(b))