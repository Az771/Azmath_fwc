from machine import Pin
import time

# Input pins for x and y buttons
x_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)
y_pin = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    x = x_pin.value()
    y = y_pin.value()
    Z = Pin(17, Pin.OUT)

    # Custom logic expression
    z = bool(not ((not (not(x and x) and y)) and not (not (y and y) and x)))

    # XOR and XNOR logic
    xor = x ^ y
    xnor = not xor

    # Compare z with xor/xnor and print result
    if z == xor:
        #print(f"x={x}, y={y} → z={z} → Result: XOR")
        Z.value(z);
    elif z == xnor:
        print(f"x={x}, y={y} → z={z} → Result: XNOR")
    else:
        print(f"x={x}, y={y} → z={z} → Result: ERROR")

    time.sleep(1)




