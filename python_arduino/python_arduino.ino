void setup() {
  Serial.begin(115200);
}

void loop() {
  float time = micros() / 1e6;
  int sensorValue1 = analogRead(A0);
  delay(250);

  Serial.print(time);
  Serial.print(", ");
  Serial.print(sensorValue1);
}
