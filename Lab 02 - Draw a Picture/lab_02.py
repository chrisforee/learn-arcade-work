"""First drawing made using arcade module - Lab 02"""
# Import the arcade library
import arcade
# Window parameters and name
arcade.open_window(650, 650, "Learn Arcade Lab 02 - Alien Watching")
# Set the background color
arcade.set_background_color(arcade.csscolor.BLACK)
# Ready to draw
arcade.start_render()

# Drawing alien
# Draw head
arcade.draw_circle_filled(325, 125, 150, (141, 245, 66), 0, -1)
arcade.draw_circle_outline(325, 125, 150, (252, 252, 252), 5, 0, -1)
# Draw the eyes and mouth
arcade.draw_ellipse_filled(275, 200, 98, 55, (0, 0, 0), 20, 10)
arcade.draw_ellipse_filled(375, 200, 98, 55, (0, 0, 0), 160, 10)
arcade.draw_line(305, 110, 345, 110, (0, 0, 0), 5)

# Drawing stars
arcade.draw_circle_filled(400, 400, 5, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(650, 500, 5, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(100, 550, 10, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(310, 290, 3, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(540, 310, 4, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(420, 610, 3, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(330, 420, 3, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(210, 510, 3, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(240, 380, 6, arcade.csscolor.WHITE, 0, -1)

# Finished drawing
arcade.finish_render()

# Keep the window open
arcade.run()
