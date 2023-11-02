from figures import Square, Rectangle, Circle


def calculate():
    input_l = input('Please enter your data here:').split()
    shape_type = input_l[0]

    if shape_type == "Square":
        top_right_x = int(input_l[2])
        top_right_y = int(input_l[3])
        side = int(input_l[5])
        if side > 0:
            shape = Square(top_right_x, top_right_y, side)
        else:
            raise ValueError("The side of square should be > 0")

    elif shape_type == "Rectangle":
        top_right_x = int(input_l[2])
        top_right_y = int(input_l[3])
        bottom_left_x = int(input_l[5])
        bottom_left_y = int(input_l[6])
        if top_right_x - bottom_left_x != 0 or top_right_y - bottom_left_y != 0:
            shape = Rectangle(top_right_x, top_right_y, bottom_left_x, bottom_left_y)
        else:
            raise ValueError("The coordinates should not be on the same point!")

    elif shape_type == "Circle":
        center_x = int(input_l[2])
        center_y = int(input_l[3])
        radius = int(input_l[-1])
        if radius > 0:
            shape = Circle(center_x, center_y, radius)
        else:
            raise ValueError("The radius of circle should be > 0")

    else:
        raise ValueError(f"Unknown shape type {shape_type}")

    perimeter = shape.calculate_perimeter()
    area = shape.calculate_area()

    print(f"{shape_type} Perimeter {perimeter} Area {area}")


def main():
    while True:
        try:
            calculate()

        except EOFError:
            break
        except ValueError as e:
            print(e)
            continue


if __name__ == "__main__":
    main()








