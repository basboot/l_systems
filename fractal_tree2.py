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
        alphabet="0F[]-+rgk<>",
        init="F0",
        rules={
            'F': [("FF", 1)],
            '0': [("[------------rF0k][rF0k]++++++++++++rF0k", 1),
                  ("[------------gF0k][gF0k]++++++++++++gF0k", 3)],
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




