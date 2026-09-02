"""
sally_anne.py - Sally-Anne false belief test using demo_light.
Run with: python sally_anne.py

This models the classic Theory of Mind test:
- Sally puts a toy in her basket and leaves.
- Anne moves the toy to her box.
- Question: Does Sally know where the toy is? (She should not.)
"""

from demo_light import (
    a, b,
    P, Prp, Top, Neg, Conj, K,
    initM, test, upd, is_true, display_s5
)
from change_vocab import ACM

# Propositions
# P(1): toy in Sally's basket
# P(2): toy in Anne's box
in_sally = Prp(P(1))
in_anne  = Prp(P(2))

# Agents
sally = a
anne  = b

# Step 0: blissful ignorance model
m0 = initM([sally, anne], [P(1), P(2)])

# Step 1: silently set the actual situation: toy in Sally's basket
toy_in_sally = Conj([in_sally, Neg(in_anne)])
m1 = upd(m0, test(toy_in_sally))

def private_move():
    """
    Return an ACM for Anne moving the toy while Sally is absent.
    Events:
        0: Anne moves the toy (substitution: in_sally <- False, in_anne <- True)
        1: No move (Top)
    Anne distinguishes 0 from 1; Sally does not.
    Actual event: 0 (Anne actually moves it).
    """
    def facm(agents):

        # Relations: reflexivity for all, plus:
        # - Anne: no link between 0 and 1 (she knows which event occurred)
        # - Sally: full connection between 0 and 1 (she cannot distinguish)
        rels = ([(ag, s, s) for ag in agents for s in [0, 1]] +
                [(ag, 0, 1) for ag in [sally]] +
                [(ag, 1, 0) for ag in [sally]])

        return ACM(
            states = [0, 1],
            agents = agents,
            pre    = {0: in_sally,1: Top()},
            subst  = {0: [(P(1), Neg(Top())), (P(2), Top())], 1: []},
            rels   = rels,
            actual = [0])
    return facm

# Apply the private move
m2 = upd(m1, private_move())

if __name__ == "__main__":
    print("=== Sally-Anne Test ===\n")
    print(f"After setting actual situation: {len(m1.states)} states")
    print(f"Actual world(s): {m1.actual}\n")
    print(f"After private move: {len(m2.states)} states")
    print(f"Actual world(s): {m2.actual}\n")

    print("Verification:")
    print(f"  Does Sally know the toy is in Anne's box? {is_true(m2, K(sally, in_anne))}")
    print(f"  Does Anne know the toy is in Anne's box?   {is_true(m2, K(anne, in_anne))}")
    print(f"  Does Sally know the toy is NOT in her basket? {is_true(m2, K(sally, Neg(in_sally)))}")
    print(f"  Does Sally consider it possible that the toy is still in her basket? "
      f"{is_true(m2, Neg(K(sally, Neg(in_sally))))}")

    # Expected output:
    #   Sally does NOT know the true location -> False
    #   Anne knows the true location -> True
    #   Sally does NOT know it's not in her basket -> False
    #   She considers it possible that it's still in her basket -> True