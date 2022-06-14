from l_system import LSystem
import turtle
import time

from l_system_animation import LSystemAnimation

if __name__ == '__main__':

    # Example 2: Fractal (binary) tree[edit]
    # variables : 0, 1
    # constants: “[”, “]”
    # axiom  : 0
    # rules  : (1 → 11), (0 → 1[0]0)



    snow = LSystem(
        alphabet="0123[]-+rgk<>",
        init="[01]+++++++++[2]+++++++++[01]+++++++++[2]+++++++++[01]+++++++++[2]+++++++++[01]+++++++++[2]+++++++++",
        rules={
            '1': [("11", 1)],
            '2': [("131", 1)],
            '3': [("21[---------11][+++++++++11]", 1)],
            '0': [("01[---------1][+++++++++1]", 1)],
            'r': [("", 1)],
            'k': [("", 1)],
            'g': [("", 1)]
        }
    )

    snowAnimation = LSystemAnimation(snow)

    for i in range(10):

        snowAnimation.draw()

        time.sleep(5)
        snow.update()




