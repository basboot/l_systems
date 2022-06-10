from l_system import LSystem
import time

# Example 3: Cantor set[edit]
# Cantor set in seven iterations.svg
# variables : A B
# constants : none
# start  : A {starting character string}
# rules  : (A → ABA), (B → BBB)
# Let A mean "draw forward" and B mean "move forward".
#
# This produces the famous Cantor's fractal set on a real straight line R.

cantor = LSystem(
    alphabet={'A', 'B'},
    init=['A'],
    rules={'A': ['A', 'B', 'A'], 'B': ['B', 'B', 'B']}
)

for i in range(10):

    # draw first
    print(f"n={cantor.generation} ({len(cantor.state)}): {cantor}")

    for character in cantor.state:
        match character:
            case 'A':
                pass
            case 'B':
                pass


    time.sleep(1)
    cantor.update()