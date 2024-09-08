const int X_PIN = A0;      // Joystick X-axis
const int Y_PIN = A1;      // Joystick Y-axis
const int BUTTON_PIN = 2;  // Joystick button

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);  // Use the internal pull-up resistor for the button
  Serial.begin(9600);
}

void loop() {
  int xValue = analogRead(X_PIN);
  int yValue = analogRead(Y_PIN);
  int buttonState = digitalRead(BUTTON_PIN);  // Read the button state

  // Sending the X, Y, and button state to serial as comma-separated values
  Serial.print(xValue);
  Serial.print(",");
  Serial.print(yValue);
  Serial.print(",");
  Serial.println(buttonState);

  delay(100);  // Delay to reduce the speed of sending data
}
