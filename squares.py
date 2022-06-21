import turtle

from l_system import LSystem

import time

from l_system_animation import LSystemAnimation

if __name__ == '__main__':

    squares = LSystem(
        alphabet="F01[]rgk-+s{}",
        init="0",
        rules={
            'F': [("FF", 1)],
            '0': [("rs0F++++++++++++++++++0F++++++++++++++++++0F++++++++++++++++++0F++++++++++++++++++", 1)],
        }
    )

    squares_animation = LSystemAnimation(squares)

    time.sleep(0)

    for i in range(40):

        squares_animation.draw(rescale=True)
        time.sleep(0.5)
        squares.update()

    # squares.update(n=42)
    # squares_animation.draw(rescale=True)
    # turtle.mainloop()
    # time.sleep(15)



