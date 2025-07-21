# --- Your original code to generate the lists ---
A = []
B = []
C = []
D = []

for a in [0, 1]:
    for b in [0, 1]:
        A.append(int((not (b)) and (a ^ b)))
        B.append(int(not(b) and a))
        C.append(int((a and not(b)) or ((a and not (b)) and b)))
        D.append(int(not (a) or b))

print("Outputs:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

# --- Finding the Odd One Out without collections.Counter ---
print("\n--- Finding the Odd One Out ---")

# 1. Create a list of all circuit patterns, associating each with its name
#    Convert lists to tuples because lists are mutable and cannot be dictionary keys
all_circuit_data = [
    ("A", tuple(A)),
    ("B", tuple(B)),
    ("C", tuple(C)),
    ("D", tuple(D))
]

# 2. Count occurrences of each unique pattern
pattern_counts = {}
for circuit_name, pattern_tuple in all_circuit_data:
    # If the pattern is already in pattern_counts, increment its count.
    # Otherwise, add it with a count of 1.
    pattern_counts[pattern_tuple] = pattern_counts.get(pattern_tuple, 0) + 1

# 3. Identify the odd one out (the pattern that appears only once)
odd_one_out_pattern = None
for pattern, count in pattern_counts.items():
    if count == 1:
        odd_one_out_pattern = pattern
        break # Found it, so exit the loop

# 4. Identify and print the circuit name corresponding to the odd pattern
if odd_one_out_pattern:
    for circuit_name, pattern_tuple in all_circuit_data:
        if pattern_tuple == odd_one_out_pattern:
            print(f"The odd one out is Circuit {circuit_name} with pattern: {list(odd_one_out_pattern)}")
            break
else:
    print("No single 'odd one out' found. All patterns are either unique or multiple patterns have the same count.")

