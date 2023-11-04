# write a Python class named Rectangle to represent a rectangle shape.
# The class should have the following functionalities
# 1. A method named set_dimensions that takes two parameters width and height and sets the attributes of the rectangle object accordingly

# 2. A method named area that calculates and returns the area of the rectangle.

# 3. A method named perimeter that calculates and returns the perimeter of the rectangle.

# Use this to create objects of the class and print the width, height, area and perimeter.


class Rectangle:

    # def __init__(self, height, width):
    #     print
    #     (f"A rectangle is created with height: {height} and width: {width}")
    #     self.height = height
    #     self.width = width

    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


# creating objects
# rectangle1 = Rectangle(4, 3)
# rectangle2 = Rectangle(5, 2)
rectangle1 = Rectangle()
rectangle1.set_dimensions(4, 3)
print("The height and width are:", rectangle1.height, rectangle1.width)
print("The area is:", rectangle1.area())
print("The perimeter is:", rectangle1.perimeter())
