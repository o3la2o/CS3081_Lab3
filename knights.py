# Lab 3 - Task 3: Knights & Knaves
from logic import *

AKnight, AKnave = Symbol("A is a Knight"), Symbol("A is a Knave")
BKnight, BKnave = Symbol("B is a Knight"), Symbol("B is a Knave")
CKnight, CKnave = Symbol("C is a Knight"), Symbol("C is a Knave")

def kind(knight, knave):
    # each character is exactly one of knight or knave
    return And(Or(knight, knave), Not(And(knight, knave)))

def says(knight, knave, statement):
    # a knight's statement is true, a knave's statement is false
    return And(Implication(knight, statement), Implication(knave, Not(statement)))

# Puzzle 0: A says "I am both a knight and a knave."
knowledge0 = And(
    kind(AKnight, AKnave),
    says(AKnight, AKnave, And(AKnight, AKnave))
)

# Puzzle 1: A says "We are both knaves." B says nothing.
knowledge1 = And(
    kind(AKnight, AKnave), kind(BKnight, BKnave),
    says(AKnight, AKnave, And(AKnave, BKnave))
)

# Puzzle 2: A says "We are the same kind." B says "We are of different kinds."
knowledge2 = And(
    kind(AKnight, AKnave), kind(BKnight, BKnave),
    says(AKnight, AKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    says(BKnight, BKnave, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Bonus Puzzle 3:
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."  B says "C is a knave."  C says "A is a knight."
knowledge3 = And(
    kind(AKnight, AKnave), kind(BKnight, BKnave), kind(CKnight, CKnave),
    # A said one of the two sentences (exclusive)
    Or(
        And(says(AKnight, AKnave, AKnight), Not(says(AKnight, AKnave, AKnave))),
        And(says(AKnight, AKnave, AKnave), Not(says(AKnight, AKnave, AKnight)))
    ),
    # B: "A said 'I am a knave'"
    says(BKnight, BKnave, says(AKnight, AKnave, AKnave)),
    says(BKnight, BKnave, CKnave),
    says(CKnight, CKnave, AKnight)
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [("Puzzle 0", knowledge0), ("Puzzle 1", knowledge1),
               ("Puzzle 2", knowledge2), ("Puzzle 3", knowledge3)]
    for name, knowledge in puzzles:
        print(name)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")

if __name__ == "__main__":
    main()
