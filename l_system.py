# https://en.wikipedia.org/wiki/L-system
import random


class LSystem:
    def __init__(self, alphabet, init, rules):
        # set with the alphabet
        self.alphabet = set(alphabet)
        # list with the current state (string)
        self.state = list(init)
        # list with all states
        self.history = [list(init)]
        # dictionary with the reproduction rules (character => list of characters)
        self.rules = {}

        # rules = { character: list of tuples (rule, weight) }
        # self.rules = { character: list of rules (larger weight = multiple times same rule) }
        for character, rule in rules.items():
            new_rule = []
            for rule_part in rule:
                for i in range(rule_part[1]):
                    new_rule.append(list(rule_part[0]))
            self.rules[character] = new_rule

        self.generation = 0


    def update(self):
        self.generation += 1

        new_state = []
        for character in self.state:
            assert character in self.alphabet, f"Illegal charachter: {character}"

            # apply rule to variable
            if character in self.rules:
                rule = self.rules[character]
                new_state += random.choice(rule)
            # or keep constant as is
            else:
                new_state.append(character)

        self.state = new_state
        self.history.append(self.state)

    def __str__(self):
        return ''.join(self.state)

if __name__ == '__main__':
    # Example 1: Algae
    # Lindenmayer's original L-system for modelling the growth of algae.
    #
    # variables : A B
    # constants : none
    # axiom  : A
    # rules  : (A → AB), (B → A)

    l = LSystem(
        alphabet={'A', 'B'},
        init=['A'],
        rules={'A': ['A', 'B'], 'B': ['A']}
    )
    print(f"Algea, init n = 0: {l}")
    for i in range(7):
        l.update()
        print(f"n={l.generation} : {l}")

