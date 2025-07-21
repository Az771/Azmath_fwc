// Define pin numbers
const int pinP = 2;
const int pinQ = 3;
const int pinR = 4;
const int pinF = 13;  // Output pin (e.g., built-in LED)

void setup() {
  // Set up input pins
  pinMode(pinP, INPUT);
  pinMode(pinQ, INPUT);
  pinMode(pinR, INPUT);

  // Set up output pin
  pinMode(pinF, OUTPUT);

  // Optional: start serial for debugging
  Serial.begin(9600);
}

void loop() {
  // Read input values
  int p = digitalRead(pinP);
  int q = digitalRead(pinQ);
  int r = digitalRead(pinR);

  // Compute F = p XOR q XOR r
  int F = p ^ q ^ r;

  // Write the result to the output pin
  digitalWrite(pinF, F);

  // Optional: print for debugging
  Serial.print("p=");
  Serial.print(p);
  Serial.print(" q=");
  Serial.print(q);
  Serial.print(" r=");
  Serial.print(r);
  Serial.print(" -> F=");
  Serial.println(F);

  delay(200);  // short delay to avoid flooding serial
}

