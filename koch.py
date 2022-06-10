from l_system import LSystem
import turtle
import time

if __name__ == '__main__':

    # Example 4: Koch curve[edit]
    # A variant of the Koch curve which uses only right angles.
    #
    # variables : F
    # constants : + −
    # start  : F
    # rules  : (F → F+F−F−F+F)

    koch = LSystem(
        alphabet={'F', '+', '-'},
        init=['F'],
        rules={'F': ['F', '+', 'F', '-', 'F', '-', 'F', '+', 'F']}
    )

    turtle.speed(0)


    for i in range(10):
        turtle.reset()
        turtle.penup()
        turtle.setx(turtle.window_width() // 2 - 20)
        turtle.pendown()
        turtle.clear()
        turtle.right(180) # to mirror like wikipedia example

        # draw first
        print(f"n={koch.generation} : {koch}")

        for character in koch.state:
            match character:
                case 'F':
                    turtle.forward(10)
                case '-':
                    turtle.left(90)
                case '+':
                    turtle.right(90)

        time.sleep(5)
        koch.update()




