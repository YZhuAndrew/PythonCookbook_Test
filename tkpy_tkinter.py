# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'PythonCookbook_Test'

from Gui import *

g = Gui()

g.title('Gui')
label = g.la(text='Press the button.')
# button = g.bu(text='Press me.')
#
#
# def make_label():
#     g.la(text='Thank you.')
#
# button2 = g.bu(text='No, press me!', command=make_label)

canvas = g.ca(width=500, height=500)
canvas.config(bg='white')

# item = canvas.circle([0, 0], 100, fill='blue')


def make_circle(size=100, color='white'):
    canvas.circle([0, 0], size, color)

button = g.bu(text='Create a circle!', command=make_circle)

g.mainloop()
