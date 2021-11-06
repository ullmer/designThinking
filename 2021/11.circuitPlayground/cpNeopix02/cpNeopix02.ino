#include <Adafruit_CircuitPlayground.h>

Adafruit_CircuitPlayground cp;

void setup() {
  // put your setup code here, to run once:
  cp.begin();
}

void loop() {
  Adafruit_CircuitPlayground cp;
  cp.begin();
  int orange[3] = {60, 24, 0}, purple[3] = {60, 0, 60};
  
  cp.setPixelColor(0, orange[0], orange[1], orange[2]);
  cp.setPixelColor(1, purple[0], purple[1], purple[2]);
  delay(1000); // milliseconds

  cp.setPixelColor(0, orange[0]/3, orange[1]/3, orange[2]/3);
  cp.setPixelColor(1, purple[0]/3, purple[1]/3, purple[2]/3);
  delay(1000); // milliseconds

  cp.setPixelColor(0, 0, 0, 0); 
  delay(1000); // milliseconds
}
