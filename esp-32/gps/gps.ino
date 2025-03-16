#ifndef LED_BUILTIN
#define LED_BUILTIN 17  // Change this to the correct pin if your board uses a different built-in LED pin
#endif

void setup() {
  // Initialize the built-in LED pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Turn the LED on.
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500); // wait for half a second
  
  // Turn the LED off.
  digitalWrite(LED_BUILTIN, LOW);
  delay(500); // wait for half a second
}
