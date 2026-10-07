# Lab 3 – Answers (CS 3081 – Alaa Alqurashi, Faisal Alburti, Hashim Alsayed)

## Task 1
### harry.py – truth table (KB = (¬rain→hagrid) ∧ (hagrid∨dumbledore) ∧ ¬(hagrid∧dumbledore) ∧ dumbledore)
| rain | hagrid | dumbledore | KB |
|---|---|---|---|
| F | F | F | F |
| F | F | T | F (¬rain→hagrid fails) |
| F | T | F | F (dumbledore is false) |
| F | T | T | F (both hagrid and dumbledore) |
| T | F | F | F |
| T | F | T | **T** |
| T | T | F | F |
| T | T | T | F |

The KB is true in only one row, and rain is true in that row. Since rain holds in every model where the KB is true, model_check returns **True**. In words: dumbledore is true, so hagrid must be false (not both). Then ¬rain→hagrid can only hold if rain is true.

### clue.py – output: MsScarlet: YES, library: YES, knife: YES
- **MsScarlet:** someone did it. Mustard is ruled out (initial cards) and Plum is ruled out (known card), so it must be Scarlet.
- **library:** Kitchen (initial) and ballroom (known) are ruled out, so it must be the library.
- **knife:** the unknown card says ¬scarlet ∨ ¬library ∨ ¬wrench. Scarlet and library are both true, so wrench must be false. Revolver is ruled out (initial), so it must be the knife.

## Task 2
### harry.py without the fact `dumbledore`
- **Prediction:** False.
- **Result:** False.
- **Why:** The KB is now true in three rows: (rain=T, hagrid=T, dumbledore=F), (rain=F, hagrid=T, dumbledore=F), and (rain=T, hagrid=F, dumbledore=T). In one of them rain is false, so the KB no longer entails rain. That only shows rain can't be concluded, not that it's false.

### puzzle.py without `MinervaGryffindor`
- **Prediction:** nothing can be placed.
- **Result:** nothing prints.
- **Why:** The only clues left are Gilderoy ∈ {Gryffindor, Ravenclaw} and Pomona ≠ Slytherin. That leaves 8 valid assignments, and no person/house pair is true in all of them, so nobody can be placed.
- **New clue:** `knowledge.add(Symbol("HoraceGryffindor"))`. It gives a unique answer: Horace is in Gryffindor, so Gilderoy is in Ravenclaw. Pomona can't be in Slytherin, so she's in Hufflepuff, and Minerva is in Slytherin. Output: GilderoyRavenclaw, PomonaHufflepuff, MinervaSlytherin, HoraceGryffindor.

## Task 3 – knights.py output and reasoning
- **Puzzle 0: A is a Knave.** A knight can't say a contradiction, because it would have to be true. So A is a knave, and the statement is false, which is consistent.
- **Puzzle 1: A is a Knave, B is a Knight.** If A were a knight, "we are both knaves" would be true, making A a knave, which is a contradiction. So A is a knave and the statement is false. Since A is a knave, B can't be one, so B is a knight.
- **Puzzle 2: A is a Knave, B is a Knight.** If A were a knight, B would be the same kind (a knight), so B's claim "different kinds" would be true, which contradicts "same". So A is a knave, A's claim is false, and they are different kinds. That makes B a knight, and B's statement is true, which is consistent.
- **Bonus Puzzle 3: A is a Knight, B is a Knave, C is a Knight.** Nobody can say "I am a knave": a knight would be lying, and a knave would be telling the truth. So B's claim that A said it is false, which makes B a knave. Then "C is a knave" is false, so C is a knight. C says A is a knight, so A is a knight.

In the code, each character is exactly one of knight or knave. Each statement S by X is encoded as Implication(XKnight, S) ∧ Implication(XKnave, Not(S)).
