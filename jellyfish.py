import turtle

from l_system import LSystem

import time

from l_system_animation import LSystemAnimation

if __name__ == '__main__':

    jellyfish = LSystem(
        alphabet="F012345[]rgbk-+s{}",
        init="gsFF[3]F[ks------------------0]F[3]F[ks------------------0]F[ks------------------0]FF[5]F[ks------------------0]F[ks------------------0]F[3][ks------------------0]FF[3]FF",
        rules={
            # 'F': [("FF", 1)],
            '0': [("1F0", 20), ("[rs---1F2][bs+++1F2]0", 1)],
            '1': [("--", 10), ("++", 1), ("-", 1), ("+", 1), ("", 1)],
            '2': [("1F2", 20), ("", 2), ("[rs---1F2][bs+++1F2]2", 1)],

            '3': [("+++[gs4]F3", 1)],
            '4': [("++++F4", 1)],
            '5': [("++[gs4]F5", 1)],
        }
    )

    jellyfish_animation = LSystemAnimation(jellyfish)

    time.sleep(0)

    # for i in range(40):
    #
    #     jellyfish_animation.draw(rescale=True)
    #     time.sleep(0.5)
    #     jellyfish.update()

    jellyfish.update(n=70)
    jellyfish_animation.draw(rescale=True)
    turtle.mainloop()
    time.sleep(15)



