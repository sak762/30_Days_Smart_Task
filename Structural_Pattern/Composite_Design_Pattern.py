from abc import ABC, abstractmethod


# Component interface
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf class (implements Component)
class Circle(Graphic):
    def draw(self):
        print("Drawing a circle")

# Leaf class (implements Component)
class Square(Graphic):
    def draw(self):
        print("Drawing a square")

# Composite class (implements Component and contains children)
class Picture(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)

    def draw(self):
        print("Drawing a picture")
        for graphic in self.graphics:
            graphic.draw()

# Client code
circle = Circle()
square = Square()

picture = Picture()
picture.add(circle)
picture.add(square)

picture.draw()
