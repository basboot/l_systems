import turtle

class LSystemAnimation:
    def __init__(self, l_system):
        # warning about unknown characters
        self.l_system = l_system

    def draw(self):
        # TODO: select starting position

        # reset turtle
        turtle.reset()
        turtle.speed(0)
        turtle.hideturtle()
        turtle.tracer(0, 0)
        # turtle.penup()
        # turtle.sety(-turtle.window_height() // 2 + 20)
        # turtle.pendown()
        turtle.clear()
        # turtle.left(90)  # to mirror like wikipedia example

        # log generation info
        print(f"n={self.l_system.generation} : {self.l_system}")

        # use list as a stack
        stack = []

        for character in self.l_system.state:
            match character:
                case 'r':
                    turtle.pencolor('red')  # leaf
                case 'g':
                    turtle.pencolor('green')  # leaf
                case 'k':
                    turtle.pencolor('black')
                case '0':
                    turtle.forward(5)  # leaf
                case '1':
                    turtle.forward(5)
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
