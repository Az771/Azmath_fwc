'''print("Q.6 : The minterm expression of f(P,Q,R) = PQ + QR' + PR' is :")
print("(A). m₂ + m₄ + m₆ + m₇           (B). m₀ + m₄ + m₅ + m₇")
print("(C). m₂ + m₄ + m₅ + m₇           (D). m₀ + m₅ + m₆ + m₇\n")

print("(A). Let us write the truth table for given equation")
#print("-----------------")
#print("| P | Q | R | F |")
#print("-----------------")
'''

segments = [
    machine.Pin(0, machine.Pin.OUT),
    machine.Pin(1, machine.Pin.OUT),
    machine.Pin(2, machine.Pin.OUT),
    machine.Pin(3, machine.Pin.OUT),
    machine.Pin(4, machine.Pin.OUT),
    machine.Pin(5, machine.Pin.OUT),
    machine.Pin(6, machine.Pin.OUT)
]

# Inverted digit to segment mapping for common anode (0 = ON, 1 = OFF)
number_map = [
    [0, 0, 0, 0, 0, 0, 1],  # 0
    [1, 0, 0, 1, 1, 1, 1],  # 1
    [0, 0, 1, 0, 0, 1, 0],  # 2
    [0, 0, 0, 0, 1, 1, 0],  # 3
    [1, 0, 0, 1, 1, 0, 0],  # 4
    [0, 1, 0, 0, 1, 0, 0],  # 5
    [0, 1, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 1, 1, 1, 1],  # 7
    [0, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 0, 1, 0, 0]   # 9
]

def display_number(number):
    for i in range(7):
        segments[i].value(number_map[number][i])

#while True:
 #   for num in range(10):
  #      display_number(num)
   #     utime.sleep(1)





minterms = []
A="m₂ + m₄ + m₆ + m₇";
B="m₀ + m₄ + m₅ + m₇"
C="m₂ + m₄ + m₅ + m₇"
D="m₀ + m₅ + m₆ + m₇"
a=[2,4,6,7];
b=[0,5,6,7];
c=[2,4,5,7];
d=[0,5,6,7];
for p in [0, 1]:
    for q in [0, 1]:
        for r in [0, 1]:
            # Compute complements
            q_bar = 1 - q
            r_bar = 1 - r
            pq=p and q;
            q_r_bar=q and r_bar;
            p_r_bar = p and r_bar
            # Evaluate expression: f = PQ' + QR + PR'
            f = pq or q_r_bar or p_r_bar;

            # Print truth table row
            #print(f"| {p} | {q} | {r} | {f} |")
            #print(f"{f}")
            # If output is 1, compute minterm index
            if f == 1:
                index = p * 4 + q * 2 + r
                minterms.append(index)


if minterms == a:
    for num in minterms:
        display_number(num)
        utime.sleep(3)

#    print(A)
elif minterms == b:
    print(B);
elif minterms == c:
    print(C);
else:
    print(D);



