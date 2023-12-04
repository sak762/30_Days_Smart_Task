# Visitor interface
class Visitor:
    def visit_circle(self, circle):
        pass

    def visit_square(self, square):
        pass

# ConcreteVisitor
class AreaCalculator(Visitor):
    def visit_circle(self, circle):
        print(f"Calculating area of Circle with radius {circle.radius}")

    def visit_square(self, square):
        print(f"Calculating area of Square with side {square.side}")

# Element interface
class Shape:
    def accept(self, visitor):
        pass

# ConcreteElement - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)

# ConcreteElement - Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def accept(self, visitor):
        visitor.visit_square(self)

# ObjectStructure
class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def accept_visitor(self, visitor):
        for shape in self.shapes:
            shape.accept(visitor)

# Usage
area_calculator = AreaCalculator()
shapes = ShapeCollection()
shapes.add_shape(Circle(5))
shapes.add_shape(Square(4))

shapes.accept_visitor(area_calculator)
