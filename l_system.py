# https://en.wikipedia.org/wiki/L-system
import random


class LSystem:
    def __init__(self, alphabet, init, rules):
        # set with the alphabet
        self.alphabet = set(alphabet)
        # store init to make a resstart possible
        self.state_init = list(init)
        # list with the current state (string)
        self.state = list(init)
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


    def update(self, n=None):
        if n is not None:
            # n is set, so reset L-System and perform n updates on it
            self.generation = 0
            self.state = self.state_init
        else:
            # no n, so just perform the next update
            n = 1

        for i in range(n):
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
        alphabet="AB",
        init="A",
        rules={'A': [("AB", 1)], 'B': [("A", 1)]}
    )
    print(f"Algea, init n = 0: {l}")
    for i in range(7):
        l.update()
        print(f"n={l.generation} : {l}")

    l.update(n=6)
    print(f"n={l.generation} : {l}")
