# Class Inheritance: Inheriting attributes and methods from one class to another
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhales, exhales")


class Fish(Animal):
    def __init__(self, name):
        super().__init__()
        self.num_eyes = 4

    def breathe(self):
        super().breathe()
        print(f"doing this under water...")

    def swim(self):
        print(f"Now has {self.num_eyes} and is swimming")


charlie = Fish("Charlie")
charlie.swim()
charlie.breathe()
