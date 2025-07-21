from machine import Pin
import time

# Define input pins
P = Pin(14, Pin.IN, Pin.PULL_DOWN)
Q = Pin(15, Pin.IN, Pin.PULL_DOWN)
R = Pin(16, Pin.IN, Pin.PULL_DOWN)

# Define output pin
f = Pin(17, Pin.OUT)

while True:
    # Read input values
    p_val = P.value()
    q_val = Q.value()
    r_val = R.value()

    # Logic: f = NOT(Q) AND NOT(R)
    #f_output = (not q_val) and (not r_val)
    f_out=not(not(not (p_val or q_val) or not(q_val or r_val)) or not(not (p_val or r_val) or not(q_val or r_val)));

    # Write to output
    f.value(f_out)

    # Optional: print state for debugging
    #print(f"P={p_val}, Q={q_val}, R={r_val}, f={f_out}")

    time.sleep(0.2)  # Small delay for stability



