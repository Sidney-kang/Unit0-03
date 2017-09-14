#Created by : Sidney Kang
#Created on : 14 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit0-03
# This program is the hello, world program, but with a button

import ui

def hello_world_touch_up_inside(sender):
	  view['hello_world_label'].text = ("Hello, World!")

view = ui.load_view()
view.present('sheet')


