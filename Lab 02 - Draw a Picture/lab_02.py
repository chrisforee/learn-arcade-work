"""First drawing made using arcade module - Lab 02"""
# Import the arcade library
import arcade
# Window parameters and name
arcade.open_window(650, 650, "Learn Arcade Lab 02")
# Set the background color
arcade.set_background_color((141, 245, 66))
# Ready to draw
arcade.start_render()
# Drawing circle/coin
arcade.draw_circle_outline(325, 350, 150, (252, 252, 252), 5, 0, -1)
arcade.finish_render()

# Keep the window open
arcade.run()



