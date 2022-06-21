import turtle

from l_system import LSystem

import time

from l_system_animation import LSystemAnimation

if __name__ == '__main__':

    ivy = LSystem(
        alphabet="F012[]rgk-+s{}",
        init="[F10]------------------[F10]------------------[F10]------------------[F10]------------------",
        rules={
            # 'F': [("FF", 1)],
            '0': [("--FF10", 16),
                  ("[--------------FF10]+++++++++FF10", 16),
                  ("--gs{FF+2+FF+2+FFF}ks", 8),
                  ("--rs{F2+++++++++F2+++++++++F2+++++++++F2+++++++++F2+++++++++F2+++++++++F}ks", 1)],
            '1': [("", 1), ("+", 1), ("++", 1), ("+++", 1), ("++++", 1), ("+++++", 1)],
            '2': [("+++", 1), ("++", 1), ("+", 1), ("", 1), ("-", 1), ("--", 1), ("---", 1)]
        }
    )

    ivy_animation = LSystemAnimation(ivy)

    time.sleep(0)

    # for i in range(50):
    #
    #     ivy_animation.draw(rescale=True)
    #     time.sleep(0.5)
    #     ivy.update()

    ivy.update(n=42)
    ivy_animation.draw(rescale=True)
    turtle.mainloop()
    time.sleep(15)



