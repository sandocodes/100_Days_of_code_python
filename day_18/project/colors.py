import colorgram
import random


class RandomColors:
    def __init__(self):
        # Extract colors from image.jpg
        self.colors = colorgram.extract('image.jpg', 50)
        self.rgb_colors = []

    # Generate Random Colors
    def get_color(self):
        """ Generate random RGB Colors. E.g. (345, 321, 232) """
        for color in self.colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b

            new_color = (r, g, b)
            self.rgb_colors.append(new_color)

        random_color = random.choice(self.rgb_colors)
        return random_color
