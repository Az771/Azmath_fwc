#include <WiFi.h>
#include <WebServer.h>
#include <BluetoothSerial.h>

// ==== Motor Control Pins ====
#define ENA 12
#define ENB 13
#define IN1 25
#define IN2 26
#define IN3 27
#define IN4 14

int speedCar = 800;
const char* ssid = "ESP32_Car";

WebServer server(80);
BluetoothSerial SerialBT;

// ==== Setup ====
void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_Car");
  Serial.println("ESP32 Car Ready (WiFi + Bluetooth)");

  // Motor pins
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  analogWrite(ENA, speedCar);
  analogWrite(ENB, speedCar);

  // WiFi Access Point
  WiFi.softAP(ssid);
  Serial.println("WiFi Car started. Connect to:");
  Serial.println(WiFi.softAPIP());

  // WiFi Routes
  server.on("/", HTTP_root);
  server.on("/F", goForward_HTTP);
  server.on("/B", goBackward_HTTP);
  server.on("/L", goLeft_HTTP);
  server.on("/R", goRight_HTTP);
  server.on("/S", stopCar_HTTP);
  server.begin();
}

// ==== Loop ====
void loop() {
  server.handleClient();  // Handle WiFi web requests

  // Handle Bluetooth Commands
  if (SerialBT.available()) {
    String command = SerialBT.readStringUntil('\n');
    command.trim();
    command.toLowerCase();
    Serial.println("BT Command: " + command);

    if (command == "forward")      goForward_BT();
    else if (command == "backward") goBackward_BT();
    else if (command == "left")     goLeft_BT();
    else if (command == "right")    goRight_BT();
    else if (command == "stop")     stopCar_BT();
    else SerialBT.println("Unknown command");
  }
}

// ==== Motor Control ====
void setMotor(bool a1, bool a2, bool b1, bool b2) {
  digitalWrite(IN1, a1);
  digitalWrite(IN2, a2);
  digitalWrite(IN3, b1);
  digitalWrite(IN4, b2);
}

// ==== WiFi Command Functions ====
void goForward_HTTP()  { setMotor(0, 1, 0, 1); server.send(200, "text/html", "Moving Forward"); }
void goBackward_HTTP() { setMotor(1, 0, 1, 0); server.send(200, "text/html", "Moving Backward"); }
void goLeft_HTTP()     { setMotor(0, 1, 1, 0); server.send(200, "text/html", "Turning Left"); }
void goRight_HTTP()    { setMotor(1, 0, 0, 1); server.send(200, "text/html", "Turning Right"); }
void stopCar_HTTP()    { setMotor(0, 0, 0, 0); server.send(200, "text/html", "Stopped"); }

// ==== Bluetooth Command Functions ====
void goForward_BT()  { setMotor(LOW, HIGH, LOW, HIGH); SerialBT.println("Moving Forward"); }
void goBackward_BT() { setMotor(HIGH, LOW, HIGH, LOW); SerialBT.println("Moving Backward"); }
void goLeft_BT()     { setMotor(HIGH, LOW, LOW, HIGH); SerialBT.println("Turning Left"); }
void goRight_BT()    { setMotor(LOW, HIGH, HIGH, LOW); SerialBT.println("Turning Right"); }
void stopCar_BT()    { setMotor(LOW, LOW, LOW, LOW); SerialBT.println("Stopped"); }

// ==== HTML Page ====
void HTTP_root() {
  server.send(200, "text/html",
    "<h1>ESP32 WiFi Car</h1>"
    "<button onclick=\"location.href='/F'\">Forward</button><br>"
    "<button onclick=\"location.href='/L'\">Left</button>"
    "<button onclick=\"location.href='/S'\">Stop</button>"
    "<button onclick=\"location.href='/R'\">Right</button><br>"
    "<button onclick=\"location.href='/B'\">Backward</button>");
}
