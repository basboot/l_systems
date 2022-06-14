from l_system import LSystem
import turtle
import time



if __name__ == '__main__':

    # Example 2: Fractal (binary) tree[edit]
    # variables : 0, 1
    # constants: “[”, “]”
    # axiom  : 0
    # rules  : (1 → 11), (0 → 1[0]0)

    fractal_binary_tree = LSystem(
        alphabet="01[]",
        init="0",
        rules={'1': [("11", 1)], '0': [("1[0]0", 1)]}
    )

    turtle.speed(0)

    for i in range(10):
        turtle.reset()
        turtle.penup()
        turtle.sety(-turtle.window_height() // 2 + 20)
        turtle.pendown()
        turtle.clear()
        turtle.left(90) # to mirror like wikipedia example

        # draw first
        print(f"n={fractal_binary_tree.generation} : {fractal_binary_tree}")

        # use list as a stack
        stack = []

        for character in fractal_binary_tree.state:
            match character:
                case '0':
                    turtle.forward(10) # leaf
                case '1':
                    turtle.forward(10)
                case '[':
                    stack.append((turtle.position(), turtle.heading()))
                    turtle.left(45)
                case ']':
                    turtle_setting = stack.pop()
                    turtle.penup()
                    turtle.goto(turtle_setting[0])
                    turtle.setheading(turtle_setting[1])
                    turtle.pendown()

                    turtle.right(45)

        time.sleep(5)
        fractal_binary_tree.update()




