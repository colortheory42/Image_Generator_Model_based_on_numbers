import pygame
import random
from color_model import ColorModel, argb_to_int, int_to_argb


def display_color(screen, color):
    screen.fill(color)
    pygame.display.flip()


def get_next_even_color():
    while True:
        a, r, g, b = [random.randint(0, 255) for _ in range(4)]
        if argb_to_int(a, r, g, b) % 2 == 0:
            return a, r, g, b


def interactive_training():
    pygame.init()
    screen = pygame.display.set_mode((420, 420))
    pygame.display.set_caption("Color Classification")

    model = ColorModel()
    try:
        model.load('color_model.pkl')
        print("Model loaded successfully.")
    except FileNotFoundError:
        print("No saved model found, starting fresh.")

    running = True
    while running:
        a, r, g, b = get_next_even_color()
        color_value = argb_to_int(a, r, g, b)
        color = (r, g, b)
        display_color(screen, color)

        predicted_category = model.predict(color_value)
        print(f"Color (ARGB): ({a}, {r}, {g}, {b}) - Value: {color_value} - Predicted: {predicted_category.upper()}")

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_input = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        waiting_for_input = False
                    elif event.key == pygame.K_f:
                        model.train(color_value, 'even')
                        waiting_for_input = False
                    elif event.key == pygame.K_b:
                        model.train(color_value, 'odd')
                        waiting_for_input = False
                    elif event.key == pygame.K_s:
                        model.save('color_model.pkl')
                        print("Model saved.")
                    else:
                        print("Invalid input. Please press 'f' for EVEN, 'b' for ODD, 's' to save, or 'q' to quit.")

    pygame.quit()
    print("Training session ended.")
    print(f"Even colors count: {len(model.even_colors)}")
    print(f"Odd colors count: {len(model.odd_colors)}")


if __name__ == "__main__":
    interactive_training()
