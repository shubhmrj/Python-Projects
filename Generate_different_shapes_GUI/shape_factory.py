from abc import ABC, abstractmethod

# Shape interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete shapes
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Factory
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        shape_type = shape_type.lower()
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        elif shape_type == 'rectangle':
            return Rectangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Demo usage
if __name__ == "__main__":
    factory = ShapeFactory()
    for shape_name in ['circle', 'square', 'rectangle', 'triangle']:
        try:
            shape = factory.create_shape(shape_name)
            print(f"{shape_name.title()}: {shape.draw()}")
        except Exception as e:
            print(f"{shape_name.title()}: {e}")
