from figures import Square, Rectangle, Circle


def calculate():
    input_l = input('Please enter your data here:').split()
    shape_type = input_l[0]

    if shape_type == "Square":
        shape = Square(input_l)

    elif shape_type == "Rectangle":
        shape = Rectangle(input_l)

    elif shape_type == "Circle":
        shape = Circle(input_l)
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
