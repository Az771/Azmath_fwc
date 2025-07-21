// Pin definitions
const int pinP = 2;
const int pinQ = 3;
const int pinR = 4;
const int pinF = 13;  // Output pin

void setup() {
  // Set up input pins
  pinMode(pinP, INPUT);
  pinMode(pinQ, INPUT);
  pinMode(pinR, INPUT);

  // Set up output pin
  pinMode(pinF, OUTPUT);

  // Optional: serial for debugging
  Serial.begin(9600);
}

void loop() {
  // Read input values
  int P = digitalRead(pinP);
  int Q = digitalRead(pinQ);
  int R = digitalRead(pinR);

  // Compute F = NOT (P OR Q OR R)
  int F = !(P || Q || R);

  //

