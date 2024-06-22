# Import the pickle module for serializing and deserializing Python objects
import pickle


def argb_to_int(a, r, g, b):
    # Shift the alpha value 'a' 24 bits to the left
    # Shift the red value 'r' 16 bits to the left
    # Shift the green value 'g' 8 bits to the left
    # Add the blue value 'b'
    # The result is a 32-bit integer representation of the ARGB color
    return (a << 24) + (r << 16) + (g << 8) + b


def int_to_argb(value):
    # Extract the alpha component by shifting right 24 bits and applying a mask of 0xFF
    a = (value >> 24) & 0xFF

    # Extract the red component by shifting right 16 bits and applying a mask of 0xFF
    r = (value >> 16) & 0xFF

    # Extract the green component by shifting right 8 bits and applying a mask of 0xFF
    g = (value >> 8) & 0xFF

    # Extract the blue component by applying a mask of 0xFF
    b = value & 0xFF

    # Return the components as a tuple (a, r, g, b)
    return (a, r, g, b)


class ColorModel:
    def __init__(self):
        # Initialize an empty set to store colors with even values
        self.even_colors = set()

        # Initialize an empty set to store colors with odd values
        self.odd_colors = set()

    def predict(self, color_value):
        # Check if the color_value is in the set of even colors
        if color_value in self.even_colors:
            return 'even'  # Return 'even' if found in even_colors
        # Check if the color_value is in the set of odd colors
        elif color_value in self.odd_colors:
            return 'odd'  # Return 'odd' if found in odd_colors
        else:
            # If color_value is not found in either set, determine if it is even or odd
            return 'even' if color_value % 2 == 0 else 'odd'

    def train(self, color_value, category):
        # Check if the category is 'even'
        if category == 'even':
            # Add the color_value to the set of even colors
            self.even_colors.add(color_value)
            # Ensure the color_value is not in the set of odd colors
            self.odd_colors.discard(color_value)
        else:
            # Add the color_value to the set of odd colors
            self.odd_colors.add(color_value)
            # Ensure the color_value is not in the set of even colors
            self.even_colors.discard(color_value)

    def save(self, filename):
        # Open the specified file in binary write mode
        with open(filename, 'wb') as f:
            # Serialize the even_colors and odd_colors sets and write them to the file
            pickle.dump((self.even_colors, self.odd_colors), f)

    def load(self, filename):
        # Open the specified file in binary read mode
        with open(filename, 'rb') as f:
            # Deserialize the even_colors and odd_colors sets from the file
            self.even_colors, self.odd_colors = pickle.load(f)
