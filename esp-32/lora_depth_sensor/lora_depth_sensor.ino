#define TRIG_PIN 47
#define ECHO_PIN 48
#define RAINDROP_PIN 36

// lowest and highest sensor readings:
const int sensorMin = 0;     // sensor minimum
const int sensorMax = 1024;  // sensor maximum

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // --- HC-SR04 Distance Measurement ---
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  long distance = duration / 58;  // Convert to cm

  // --- Raindrop Sensor Measurement ---
  int sensorReading = analogRead(RAINDROP_PIN);
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);
  
  // Output results
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  print("Raindrop Sensor")
  print(sensorReading)
  print(range)
  
  delay(1000);
}
