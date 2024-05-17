import math
from abc import ABC, abstractmethod, abstractproperty


class GeometricShape(ABC):
    @abstractmethod
    def find_area(self) -> float:
        pass

    @abstractproperty
    def shape_name(self):
        pass


class Circle(GeometricShape):
    def __init__(self, radius=0.0):
        super().__init__()  # good practice
        self.radius = radius

    def find_area(self) -> float:
        return math.pi * self.radius * self.radius

    @property
    def shape_name(self):
        return "circle"


class Triangle(GeometricShape):
    def __init__(self, base=0.0, height=0.0):
        super().__init__()
        self.base = base
        self.height = height

    def find_area(self) -> float:
        return 0.5 * self.base * self.height

    @property
    def shape_name(self):
        return "triangle"


# polymorphic method
def process_shape(shape: GeometricShape):
    if not isinstance(shape, GeometricShape):
        raise TypeError('expecting GeometricShape object, but got a different one')

    # todo: process the shape
    area = shape.find_area()
    print(f'area of the given {shape.shape_name} is {area}')


if __name__ == '__main__':
    c1 = Circle(23.45)
    t1 = Triangle(23, 45)

    process_shape(c1)
    process_shape(t1)
