# Import the pygame library for creating games and multimedia applications
import pygame

# Import the random module for generating random numbers
import random

# Import the ColorModel class and functions argb_to_int and int_to_argb from the color_model module
from color_model import ColorModel, argb_to_int, int_to_argb


def display_color(screen, color):
    # Fill the entire screen with the specified color
    screen.fill(color)

    # Update the full display surface to the screen
    pygame.display.flip()


def get_next_even_color():
    # Loop indefinitely until an even color is found
    while True:
        # Generate random values for alpha, red, green, and blue components
        a, r, g, b = [random.randint(0, 255) for _ in range(4)]

        # Convert the ARGB components to a single integer and check if it's even
        if argb_to_int(a, r, g, b) % 2 == 0:
            # If the integer value is even, return the ARGB components
            return a, r, g, b


def interactive_training():
    # Initialize all Pygame modules
    pygame.init()

    # Set up the display with a width and height of 420 pixels each
    screen = pygame.display.set_mode((420, 420))

    # Set the window caption to "Color Classification"
    pygame.display.set_caption("Color Classification")

    # Create an instance of the ColorModel class
    model = ColorModel()

    # Attempt to load a previously saved model from a file
    try:
        # Load the model data from the file 'color_model.pkl'
        model.load('color_model.pkl')
        print("Model loaded successfully.")
    # Handle the case where the file does not exist
    except FileNotFoundError:
        print("No saved model found, starting fresh.")

    # Variable to control the main loop of the program
    running = True

    while running:
        # Get the next even color's ARGB components
        a, r, g, b = get_next_even_color()

        # Convert the ARGB components to a single integer value
        color_value = argb_to_int(a, r, g, b)

        # Create an RGB color tuple from the red, green, and blue components
        color = (r, g, b)

        # Display the color on the screen
        display_color(screen, color)

        # Predict the category (even or odd) of the color value using the model
        predicted_category = model.predict(color_value)

        # Print the color components (ARGB), the integer color value, and the predicted category in uppercase
        print(f"Color (ARGB): ({a}, {r}, {g}, {b}) - Value: {color_value} - Predicted: {predicted_category.upper()}")

        # Variable to control the input waiting loop
        waiting_for_input = True

        while waiting_for_input:
            # Loop through the event queue
            for event in pygame.event.get():
                # Check if the user closed the window
                if event.type == pygame.QUIT:
                    running = False  # Stop the main loop
                    waiting_for_input = False  # Stop the input waiting loop
                # Check if a key was pressed
                elif event.type == pygame.KEYDOWN:
                    # Check if the 'q' key was pressed to quit
                    if event.key == pygame.K_q:
                        running = False  # Stop the main loop
                        waiting_for_input = False  # Stop the input waiting loop
                    # Check if the 'f' key was pressed to train the model with the even category
                    elif event.key == pygame.K_f:
                        model.train(color_value, 'even')  # Train the model with the even category
                        waiting_for_input = False  # Stop the input waiting loop
                    # Check if the 'b' key was pressed to train the model with the odd category
                    elif event.key == pygame.K_b:
                        model.train(color_value, 'odd')  # Train the model with the odd category
                        waiting_for_input = False  # Stop the input waiting loop
                    # Check if the 's' key was pressed to save the model
                    elif event.key == pygame.K_s:
                        model.save('color_model.pkl')  # Save the model to a file
                        print("Model saved.")
                    # Handle any other key presses with an invalid input message
                    else:
                        print("Invalid input. Please press 'f' for EVEN, 'b' for ODD, 's' to save, or 'q' to quit.")

    # Quit all Pygame modules
    pygame.quit()

    # Print a message indicating the training session has ended
    print("Training session ended.")

    # Print the count of even colors in the model
    print(f"Even colors count: {len(model.even_colors)}")

    # Print the count of odd colors in the model
    print(f"Odd colors count: {len(model.odd_colors)}")


# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the interactive_training function to start the training session
    interactive_training()
