# import turtle
# import time


# noinspection PyUnresolvedReferences # this will get rid of that error
# to apply it to all, can choose that option from the drop down
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)

# it will sit there for 4 seconds
# time.sleep(4)

# this will wait till you close the window
# turtle.done()

# =====================
#
# from turtle import forward, right, done
# # to be more selective
#
# forward(150)
# right(250)
# # turtle.circle(75) # the . needs import turtle
# forward(150)
# done()

# ===========================
# from turtle import *
# # this method is frowned upon
# # because can hide a name
#
# forward(150)
# right(250)
# forward(150)
# circle(75)
# done()

# ==============================
done = "Well done, you have finished your drawing"
from turtle import *

forward(150)
right(250)
forward(150)
circle(75)

done()
print(done)
# ================================
from turtle import *
done = "Well done, you have finished your drawing"

forward(150)
right(250)
forward(150)
circle(75)

done()
print(done)

# Note: unless you are working in an interactive session
# ,do not use import star
# because it can do weird unexpected stuff
# =============