class Apple:
    flavor = ""
    color = ""

    def set_flavor(self, flavor):
        self.flavor = flavor

    def set_color(self, color):
        self.color = color

    def __init__(self, flavor, color):
        self.set_flavor(flavor)
        self.set_color(color)


food = Apple("red", "sweet")
print("The flavor is {} and color is {}".format(food.flavor, food.color))
