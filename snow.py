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



    for i in range(10):
        turtle.reset()
        turtle.speed(0)
        turtle.hideturtle()
        turtle.tracer(0, 0)
        turtle.penup()
        # turtle.sety(-turtle.window_height() // 2 + 20)
        turtle.pendown()
        turtle.clear()
        turtle.left(90) # to mirror like wikipedia example

        # draw first
        print(f"n={fractal_binary_tree.generation} : {fractal_binary_tree}")

        # use list as a stack
        stack = []

        g_count = 0
        r_count = 0

        for character in fractal_binary_tree.state:
            match character:
                case 'r':
                    turtle.pencolor('red')  # leaf
                    r_count+=1
                case 'g':
                    turtle.pencolor('green')  # leaf
                    g_count+=1
                case 'k':
                    turtle.pencolor('black')
                case '0':
                    turtle.forward(25) # leaf
                case '1':
                    turtle.forward(25)
                case '[':
                    stack.append((turtle.position(), turtle.heading()))
                case '-':
                    turtle.left(5)
                case ']':
                    turtle_setting = stack.pop()
                    turtle.penup()
                    turtle.goto(turtle_setting[0])
                    turtle.setheading(turtle_setting[1])
                    turtle.pendown()
                case '+':
                    turtle.right(5)
                case '<':
                    turtle.left(90)
                    turtle.forward(1)
                    turtle.right(90)
                case '>':
                    turtle.right(90)
                    turtle.forward(1)
                    turtle.left(90)

        turtle.update()
        time.sleep(5)
        print(f"Green: {g_count} Red: {r_count}")
        fractal_binary_tree.update()




