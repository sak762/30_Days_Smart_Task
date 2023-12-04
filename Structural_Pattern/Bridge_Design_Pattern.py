from abc import ABC, abstractmethod


# Abstraction
class Shape(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def draw(self):
        pass

# Concrete Abstraction
class Circle(Shape):
    def draw(self):
        print(f"Drawing a Circle with color {self._color.fill()}")

class Square(Shape):
    def draw(self):
        print(f"Drawing a Square with color {self._color.fill()}")

# Implementor
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

# Concrete Implementor
class RedColor(Color):
    def fill(self):
        return "Red"

class BlueColor(Color):
    def fill(self):
        return "Blue"

# Client code
red_color = RedColor()
blue_color = BlueColor()

circle = Circle(red_color)
circle.draw()

square = Square(blue_color)
square.draw()
