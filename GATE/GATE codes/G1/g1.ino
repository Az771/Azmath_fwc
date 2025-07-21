// Pin Definitions
const int pinP = 2;
const int pinQ = 3;
const int pinR = 4;
const int pinF = 13;  // Built-in LED for output

void setup() {
  // Set pin modes
  pinMode(pinP, INPUT);
  pinMode(pinQ, INPUT);
  pinMode(pinR, INPUT);
  pinMode(pinF, OUTPUT);

  // Optional: Start serial monitor
  Serial.begin(9600);
}

void loop() {
  // Read inputs
  int P = digitalRead(pinP);
  int Q = digitalRead(pinQ);
  int R = digitalRead(pinR);

  // Compute F = (P AND Q) OR (Q AND NOT R) OR (P AND NOT R)
  int F = (P && Q) || (Q && !R) || (P && !R);

  // Output result
  digitalWrite(pinF, F);

  // Debug output (optional)
  Serial.print("P: "); Serial.print(P);
  Serial.print(" Q: "); Serial.print(Q);
  Serial.print(" R: "); Serial.print(R);
  Serial.print(" => F: "); Serial.println(F);

  delay(500);  // Update every 0.5 second
}

