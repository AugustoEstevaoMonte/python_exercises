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


class Tree(Apple):
    def __init__(self, color, flavor):
        super().__init__(flavor, color)


plant = Tree("Brown", "Horrible Taste")
print("The flavor is {} and color is {}".format(plant.flavor, plant.color))