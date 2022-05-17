#include "DHT.h"

DHT dht(D0,DHT11);
void setup() {
  // put your setup code here, to run once:
  dht.begin();
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float h=dht.readHumidity();
  float t=dht.readTemperature();

  Serial.print("H: ");
  Serial.print(h);
  Serial.print(",T: ");
  Serial.println(t);
  delay(2000);
}
