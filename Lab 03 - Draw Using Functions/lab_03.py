""" Using drawings from Lab02 to create drawing functions in Lab 03"""
# Import the arcade and random module
import arcade
import random

# Create window size variables
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650


def draw_alien_head(x, y):
    """Draw the Alien's head at x, y point"""

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)
    # Draw head outline
    arcade.draw_circle_filled(x, y, 150, (141, 245, 66), 0, -1)
    arcade.draw_circle_outline(x, y, 150, (252, 252, 252), 5, 0, -1)
    # Draw the eyes and mouth
    arcade.draw_ellipse_filled(x - 55, y + 55, 98, 55, (0, 0, 0), 20, 10)
    arcade.draw_ellipse_filled(x + 55, y + 55, 98, 55, (0, 0, 0), 160, 10)
    arcade.draw_line(x - 35, y - 75, x + 20, y - 75, (0, 0, 0), 5)


def draw_satellite():
    """Draw the satellite"""
    arcade.draw_rectangle_filled(520, 440, 35, 35, arcade.csscolor.DARK_SLATE_GRAY, 35)
    arcade.draw_rectangle_filled(520, 440, 145, 5, arcade.csscolor.DARK_SLATE_GRAY, 35)
    arcade.draw_rectangle_filled(460, 480, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
    arcade.draw_rectangle_filled(475, 470, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
    arcade.draw_rectangle_filled(490, 460, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
    arcade.draw_rectangle_filled(550, 420, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
    arcade.draw_rectangle_filled(565, 410, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
    arcade.draw_rectangle_filled(580, 400, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)


def draw_moon():
    """Draw the moon"""
    arcade.draw_circle_filled(100, 415, 55, arcade.csscolor.SILVER, 0, -1)
    arcade.draw_circle_filled(112, 429, 4.8, arcade.csscolor.DARK_SLATE_GRAY, 0, -1)
    arcade.draw_circle_filled(69, 378, 1, arcade.csscolor.SLATE_GREY, 7, -1)
    arcade.draw_circle_filled(95, 390, 3, arcade.csscolor.SLATE_GREY, 2, -1)
    arcade.draw_circle_filled(73, 422, 2, arcade.csscolor.SLATE_GREY, 2, -1)
    arcade.draw_circle_filled(107, 459, 2, arcade.csscolor.SLATE_GREY, 2, -1)


def draw_stars(x, y, z):
    """Draw the stars at random plots based on x, y points. z determines the density of stars on screen"""
    i = 0
    while i < z :
        arcade.draw_circle_filled(x + (random.randint(1, 625)),
                                  y + (random.randint(1, 625)), (random.randint(1, 3)), arcade.csscolor.WHITE, 0, -1)
        arcade.draw_circle_filled(x - (random.randint(1, 625)),
                                  y - (random.randint(1, 625)), (random.randint(1, 3)), arcade.csscolor.WHITE, 0, -1)
        arcade.draw_circle_filled(x + (random.randint(1, 625)),
                                  y - (random.randint(1, 625)), (random.randint(1, 3)), arcade.csscolor.WHITE, 0, -1)
        arcade.draw_circle_filled(x - (random.randint(1, 625)),
                                  y + (random.randint(1, 625)), (random.randint(1, 3)), arcade.csscolor.WHITE, 0, -1)
        i += 1


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Learn Arcade Lab 02 - Alien Watching")
    # Set the background color
    arcade.set_background_color(arcade.csscolor.BLACK)
    # Ready to draw
    arcade.start_render()

    # Draw the stars
    draw_stars(325, 325, 150)

    # Draw the satellite
    draw_satellite()

    # Draw the moon
    draw_moon()

    # Draw the alien head
    draw_alien_head(275, 125)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started
main()
