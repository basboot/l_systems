import turtle

from l_system import LSystem

import time

from l_system_animation import LSystemAnimation

if __name__ == '__main__':

    crown = LSystem(
        alphabet="F012[]rgk-+s{}",
        init="sF0",
        rules={
            # 'F': [("FF", 1)],
            '0': [("F10", 16), ("[---------F2][+++++++++F2]FF10", 1)],
            '1': [("+", 20), ("", 1)],  # slowly expanding circle
            '2': [("F2", 2), ("[---------F2][+++++++++F2]", 1), ("[gs{F+++++F+++++F}]", 20), ("[rs{F+++++++F+++++++F+++++++F}]", 10)],
        }
    )

    crown_animation = LSystemAnimation(crown)

    time.sleep(0)

    # for i in range(40):
    #
    #     crown_animation.draw(rescale=True)
    #     time.sleep(0.5)
    #     crown.update()

    crown.update(n=1000)
    crown_animation.draw(rescale=True)
    turtle.mainloop()
    time.sleep(15)



