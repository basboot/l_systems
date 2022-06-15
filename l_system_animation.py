import turtle

INITIAL_DRAWING_UNIT = 5    # pixels
ROTATION_UNIT = 5   # degrees


class LSystemAnimation:
    def __init__(self, l_system, width=1000, height=500):
        # warning about unknown characters
        self.l_system = l_system
        self.width = width
        self.height = height
        self.startpos = (0, 0)
        self.drawing_unit = INITIAL_DRAWING_UNIT

    def draw(self):
        # init screen (add 10pct as a border)
        turtle.setup(width=self.width * 1.1, height=self.height * 1.1)

        # reset startpos
        self.startpos = (0, 0)

        # draw in memory first to check boundaries
        min_x, max_x, min_y, max_y = self.drawLSystem()

        # find size used
        size_x = max_x - min_x + 1  # avoid division by zero when drawing a line
        size_y = max_y - min_y + 1

        # calculate ratio needed to fit
        ratio_x = self.width / size_x
        ratio_y = self.height / size_y

        # choose only smallest ratio for scaling (we preserve aspect ratio)
        scaling = ratio_x if ratio_x < ratio_y else ratio_y

        # change unit to scale drawing
        self.drawing_unit *= scaling

        # find new origin
        delta_x = (min_x + max_x) / 2
        delta_y = (min_y + max_y) / 2

        # shift drawing in opposite direction and scale
        self.startpos = (
            -delta_x * scaling,
            -delta_y * scaling
        )

        # redraw after scaling
        self.drawLSystem()

        # show drawing
        turtle.update()
        #turtle.Screen().mainloop()

    def drawLSystem(self):
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0

        # reset turtle
        turtle.clear()
        turtle.reset()

        turtle.penup()
        turtle.goto(self.startpos)
        print(f"goto: {self.startpos}")
        turtle.pendown()


        turtle.speed(0)
        turtle.hideturtle()
        turtle.tracer(0, 0)
        # turtle.penup()
        # turtle.sety(-turtle.window_height() // 2 + 20)
        # turtle.pendown()

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
                case 'F':
                    turtle.forward(self.drawing_unit)
                case '[':
                    stack.append((turtle.position(), turtle.heading()))
                case '-':
                    turtle.right(ROTATION_UNIT)
                case ']':
                    turtle_setting = stack.pop()
                    turtle.penup()
                    turtle.goto(turtle_setting[0])
                    turtle.setheading(turtle_setting[1])
                    turtle.pendown()
                case '+':
                    turtle.left(ROTATION_UNIT)
                case '<':
                    turtle.left(90)
                    turtle.forward(1)
                    turtle.right(90)
                case '>':
                    turtle.right(90)
                    turtle.forward(1)
                    turtle.left(90)

            # update minmax
            posxy = turtle.position()
            min_x = min(posxy[0], min_x)
            min_y = min(posxy[1], min_y)
            max_x = max(posxy[0], max_x)
            max_y = max(posxy[1], max_y)

            #print(min_x, min_y, max_x, max_y)

        return min_x, max_x, min_y, max_y
