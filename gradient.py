import math

def hex_to_rgb(color_hex):
    """Returns list of [r, b, b] for given hex color.

    :param color_hex: color in hex format (without leading #)
    :type color_hex: string

    :return: [r, b, b]
    :rtype: list
    """
    return [ int(color_hex[x*2:x*2+2], 16) for x in range(3) ]

def rgb_to_hex(color_rgb):
    """Returns a color in hex format from a given color in rgb 

    :param color_rgb: color in rgb format ex [256, 256, 256] 
    :type color_rgb: list

    :return: color in hex format
    :rtype: string
    """
    return '%02x%02x%02x' % tuple(color_rgb)


class Gradient(object):
    lower_hex = None
    upper_hex = None

    N = 0

    def __init__(self, lower_hex, upper_hex, N):
        """Takes lower and upper colors formated in hex with N steps in between to generate a gradient.

        :param lower_hex: starting color in hex format for gradient (with or without #)
        :type lower_hex: string

        :param upper_hex: ending color in hex format for gradient (with or without #)
        :type upper_hex: string

        :param N: Number of steps to generate between the lower and upper color of the gradient
        :type N: integer
        """
        if lower_hex[0] == '#':
            self.lower_hex = lower_hex[1:]
        else:
            self.lower_hex = lower_hex

        if upper_hex[0] == '#':
            self.upper_hex = upper_hex[1:]
        else:
            self.upper_hex = upper_hex

        self.N = N

    def get_color(self, x):
        """Returns the color at fraction x/N between lower and upper colors of the gradient.
        Where x = 0 returns lower_hex and x = N returns upper_hex.

        :param x: x is the number of steps from lower_hex towards upper_hex
        :type x: integer

        :return: color in hex format
        :rtype: string
        """
        lower_rgb = hex_to_rgb(self.lower_hex)
        upper_rgb = hex_to_rgb(self.upper_hex)

        gradient_rgb = [ int(round((u - l)*x/self.N + l)) for l, u in zip(lower_rgb, upper_rgb) ]

        return "#%s" % rgb_to_hex(gradient_rgb).upper()