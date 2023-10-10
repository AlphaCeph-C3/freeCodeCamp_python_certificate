class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(0, self.height):
            picture += f"{'*'*self.width}\n"
        return picture

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, new_side):
        super().set_width(new_side)
        super().set_height(new_side)
        self.side = new_side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_height(height)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(side={self.side})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
