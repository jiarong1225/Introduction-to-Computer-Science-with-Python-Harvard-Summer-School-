import math

class Pizza:
    def __init__(self, topping, diameter, price, slices):
        self.topping = topping
        self.diameter = diameter
        self.price = price
        self.slices = slices
    # Make sure to add your constructore here.

    def __str__(self):
        return(f"Your {self.topping} pizza, has a diameter of {self.diameter} inches, a price of ${self.price}, and {self.slices} slices per pie")

    def area_per_slice(self):
        radius = self.diameter / 2
        area = 3.14 * (radius ** 2)
        area_per_slice = area / self.slices
        return area_per_slice

    def cost_per_slice(self):
        cost_per_slice = self.price / self.slices
        return cost_per_slice

    def cost_per_square_inch(self):
        radius = self.diameter / 2
        area = 3.14 * (radius ** 2)
        cost_per_square_inch = self.price / area
        return cost_per_square_inch




