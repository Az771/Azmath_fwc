def NOR(a, b):   return int(not (a or b))      # P
def NAND(a, b):  return int(not (a and b))     # Q
def XNOR(a, b):  return int(not (a ^ b))       # R
def XOR(a, b):   return int(a ^ b)             # S

# Column B gates
def B1(a, b):    return XOR(a, b)              # Symbol 1
def B2(a, b):    return NAND(a, b)             # Symbol 2
def B3(a, b):    return XNOR(a, b)             # Symbol 3
def B4(a, b):    return NOR(a, b)              # Symbol 4

# Truth table cases
cases = [(0,0), (0,1), (1,0), (1,1)]
def table(fn): return [fn(a,b) for a,b in cases]

# Column A gate tables
A_tables = {
    'P': table(NOR),    # NOR
    'Q': table(NAND),   # NAND
    'R': table(XNOR),   # XNOR
    'S': table(XOR),    # XOR
}

# Column B gate tables
B_tables = {
    '1': table(B1),     # XOR
    '2': table(B2),     # NAND
    '3': table(B3),     # XNOR
    '4': table(B4),     # NOR
}

# Match each A to correct B
matches = {}
for a_name, a_tbl in A_tables.items():
    for b_name, b_tbl in B_tables.items():
        if a_tbl == b_tbl:
            matches[a_name] = b_name
            break

print("\nDerived mapping (A ➜ B):", matches)

# Given options
choices = {
    1: {'P':'2', 'Q':'4', 'R':'1', 'S':'3'},
    2: {'P':'4', 'Q':'2', 'R':'1', 'S':'3'},
    3: {'P':'2', 'Q':'4', 'R':'3', 'S':'1'},
    4: {'P':'4', 'Q':'2', 'R':'3', 'S':'1'},
}

# Check which matches
for num, choice in choices.items():
    if choice == matches:
        print("\n✅ Correct option is:", num)
        break
