from l_system import LSystem

import time

from l_system_animation import LSystemAnimation

if __name__ == '__main__':

    # Example 2: Fractal (binary) tree[edit]
    # variables : 0, 1
    # constants: “[”, “]”
    # axiom  : 0
    # rules  : (1 → 11), (0 → 1[0]0)



    fractal_binary_tree = LSystem(
        alphabet="01[]-+rgk<>",
        init="0",
        rules={
            '1': [("111", 1)],
            '0': [("1[------------r0k][r0k]++++++++++++r0k", 1),
                  ("1[------------g0k][g0k]++++++++++++g0k", 3)],
            'r': [("", 1)],
            'k': [("", 1)],
            'g': [("", 1)]
        }
    )

    fractal_binary_tree_animation = LSystemAnimation(fractal_binary_tree)

    for i in range(10):

        fractal_binary_tree_animation.draw()
        time.sleep(5)
        fractal_binary_tree.update()




