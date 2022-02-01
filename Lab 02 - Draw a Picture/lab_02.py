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
arcade.draw_circle_filled(100, 550, 3.65, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(310, 290, 3, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(540, 310, 4, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(420, 610, 3, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(330, 420, 3, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(210, 510, 3, arcade.csscolor.WHITE, 0, -1)
arcade.draw_circle_filled(240, 380, 6, arcade.csscolor.WHITE, 0, -1)

# Draw Satellite
arcade.draw_rectangle_filled(520, 440, 35, 35, arcade.csscolor.DARK_SLATE_GRAY, 35)
arcade.draw_rectangle_filled(520, 440, 195, 5, arcade.csscolor.DARK_SLATE_GRAY, 35)
arcade.draw_rectangle_filled(520, 440, 35, 35, arcade.csscolor.DARK_SLATE_GRAY, 35)
arcade.draw_rectangle_filled(460, 480, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
arcade.draw_rectangle_filled(475, 470, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
arcade.draw_rectangle_filled(490, 460, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
arcade.draw_rectangle_filled(550, 420, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
arcade.draw_rectangle_filled(565, 410, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)
arcade.draw_rectangle_filled(580, 400, 115, 8, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 125)

# Draw Moon

# Finished drawing
arcade.finish_render()

# Keep the window open
arcade.run()
