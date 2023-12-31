import math


class Shape:
    def __init__(self):
        self.name = ""

    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass


class Square(Shape):
    # def __init__(self, top_right_x, top_right_y, side):
    #     super().__init__()
    #     self.name = "Square"
    #     self.top_right_x = top_right_x
    #     self.top_right_y = top_right_y
    #     if side > 0:
    #         self.side = side
    #     else:
    #         raise ValueError("The side of square should be > 0")

    def __init__(self, input_l):
        super().__init__()
        self.name = "Square"
        self.top_right_x = int(input_l[2])
        self.top_right_y = int(input_l[3])
        if int(input_l[5]) > 0:
            self.side = int(input_l[5])
        else:
            raise ValueError("The side of square should be > 0")

    def calculate_perimeter(self):
        perimetr = self.side * 4
        return perimetr

    def calculate_area(self):
        area = self.side * self.side
        return area


class Rectangle(Shape):
    def __init__(self, input_l):
        super().__init__()
        self.name = "Rectangle"
        if int(input_l[2]) - int(input_l[5]) != 0 and int(input_l[3]) - int(input_l[6]) != 0:
            self.top_right_x = int(input_l[2])
            self.top_right_y = int(input_l[3])
            self.bottom_left_x = int(input_l[5])
            self.bottom_left_y = int(input_l[6])
        else:
            raise ValueError("The coordinates should not be on the same point!")

    def calculate_perimeter(self):
        perimetr = 2 * (abs(self.top_right_x - self.bottom_left_x) + abs(self.top_right_y - self.bottom_left_y))
        return perimetr

    def calculate_area(self):
        area = abs(self.top_right_x - self.bottom_left_x) * abs(self.top_right_y - self.bottom_left_y)
        return area


class Circle(Shape):
    def __init__(self, input_l):
        super().__init__()
        self.name = "Circle"
        self.center_x = int(input_l[2])
        self.center_y = int(input_l[3])
        if int(input_l[-1]) > 0:
            self.radius = int(input_l[-1])
        else:
            raise ValueError("The radius of circle should be > 0")

    def calculate_perimeter(self):
        perimetr = math.pi * self.radius * 2
        return round(perimetr, 2)

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return round(area, 2)
