import math


class Shape:
    def __init__(self):
        self.name = ""

    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, top_right_x, top_right_y, side):
        super().__init__()
        self.name = "Square"
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.side = side

    def calculate_perimeter(self):
        perimetr = self.side * 4
        return perimetr

    def calculate_area(self):
        area = self.side * self.side
        return area


class Rectangle(Shape):
    def __init__(self, top_right_x, top_right_y, bottom_left_x, bottom_left_y):
        super().__init__()
        self.name = "Rectangle"
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.bottom_left_x = bottom_left_x
        self.bottom_left_y = bottom_left_y

    def calculate_perimeter(self):
        perimetr = 2 * (abs(self.top_right_x - self.bottom_left_x) + abs(self.top_right_y - self.bottom_left_y))
        return perimetr

    def calculate_area(self):
        area = abs(self.top_right_x - self.bottom_left_x) * abs(self.top_right_y - self.bottom_left_y)
        return area


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__()
        self.name = "Circle"
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def calculate_perimeter(self):
        perimetr = math.pi * self.radius * 2
        return round(perimetr, 2)

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return round(area, 2)
