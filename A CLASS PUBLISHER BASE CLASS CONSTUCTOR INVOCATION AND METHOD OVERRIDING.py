class publisher:
    def __init__(self):
        self.name="Prentice Hall"
    def display(self):
        print("\nPublisher : ",self.name)
class book(publisher):
    def __init__(self):
        self.title="Core Python Application Programing"
        self.author="Wesley J Chun"
    def display(self):
        super().__init__()
        super().display()
        print("\nTitle: ",self.title)
        print("\nAuthor: ",self.author)
class python(book):
    def __init__(self):
        self.price="650"
        self.pages="1136"
    def display(self):
        super().__init__()
        super().display()
        print("\nPrice: ",self.price)
        print("\nPages: ",self.pages)
obj1=python()
print("Book Details : ")
obj1.display()