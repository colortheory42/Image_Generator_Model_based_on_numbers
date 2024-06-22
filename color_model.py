import pickle


def argb_to_int(a, r, g, b):
    return (a << 24) + (r << 16) + (g << 8) + b


def int_to_argb(value):
    a = (value >> 24) & 0xFF
    r = (value >> 16) & 0xFF
    g = (value >> 8) & 0xFF
    b = value & 0xFF
    return (a, r, g, b)


class ColorModel:
    def __init__(self):
        self.even_colors = set()
        self.odd_colors = set()

    def predict(self, color_value):
        if color_value in self.even_colors:
            return 'even'
        elif color_value in self.odd_colors:
            return 'odd'
        else:
            return 'even' if color_value % 2 == 0 else 'odd'

    def train(self, color_value, category):
        if category == 'even':
            self.even_colors.add(color_value)
            self.odd_colors.discard(color_value)
        else:
            self.odd_colors.add(color_value)
            self.even_colors.discard(color_value)

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.even_colors, self.odd_colors), f)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self.even_colors, self.odd_colors = pickle.load(f)
