# --- 1. helper --------------------------------------------------------------
def mux_output(P, Q, R):
    """4‑to‑1 MUX with inputs [R, R̅, R̅, R] and selects S1=P, S0=Q."""
    sel = (P << 1) | Q               # binary PQ → 0‑3
    inputs = [R, not R, not R, R]    # I0..I3
    return int(inputs[sel])          # cast bool → 0/1

# --- 2. generate the truth lists -------------------------------------------
combinations = [(P, Q, R)
                for P in (0, 1)
                for Q in (0, 1)
                for R in (0, 1)]

f_list = [mux_output(P, Q, R) for P, Q, R in combinations]

# Option formulas straight from the question:
optA = [(P ^ Q ^ (1 - R))            for P, Q, R in combinations]  # P ⊕ Q ⊕ R̅
optB = [(P ^ Q ^ R)                  for P, Q, R in combinations]  # P ⊕ Q ⊕ R
optC = [int((P or Q) or R)           for P, Q, R in combinations]  # P + Q + R
optD = [int((P or Q) or (1 - R))     for P, Q, R in combinations]  # P + Q + R̅

options = {"A": optA, "B": optB, "C": optC, "D": optD}

# --- 3. compare & announce --------------------------------------------------
print("Truth table order (P,Q,R):", combinations)
print("MUX outputs f_list        :", f_list)

for label, lst in options.items():
    match = (lst == f_list)
    print("Option", label, "matches MUX?" , match)
    if match:
        correct = label

print("\n➡️  Correct option is:", correct)
