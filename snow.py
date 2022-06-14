from l_system import LSystem
import turtle
import time

from l_system_animation import LSystemAnimation

if __name__ == '__main__':
    snow = LSystem(
        alphabet="0F23[]-+rgk<>",
        init="[0F]+++++++++[2]+++++++++[0F]+++++++++[2]+++++++++[0F]+++++++++[2]+++++++++[0F]+++++++++[2]+++++++++",
        rules={
            'F': [("FF", 1)],
            '2': [("F3F", 1)],
            '3': [("2F[---------FF][+++++++++FF]", 1)],
            '0': [("0F[---------F][+++++++++F]", 1)],
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




