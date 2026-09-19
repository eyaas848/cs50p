class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def main():
    shapes = [Circle(5), Rectangle(4, 6)]
    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
