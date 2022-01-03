"""
This is a sample program.

Multi-line comments are surrounded by three double quotes
"""
# Import the "arcade" library

import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw and ellipse with
# a center of (300, 300)
# width of 350
# height of 200
arcade.draw_rectangle_outline(300, 300, 350, 200, arcade.csscolor.BLACK, 3)
arcade.draw_ellipse_outline(300, 300, 350, 200, arcade.csscolor.RED, 3)

# Draw a rectangle
# Left of 0, right of 599,
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.color.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Finish drawing
arcade.finish_render()

# Keep the window open
arcade.run()