#include <Adafruit_CircuitPlayground.h>

Adafruit_CircuitPlayground cp;

void setup() {
  // put your setup code here, to run once:
  cp.begin();
}

void loop() {
  Adafruit_CircuitPlayground cp;
  cp.begin();
  int orange[3] = {50, 25, 0}, purple[3] = {50, 0, 50};
  
  cp.setPixelColor(0, orange[0], orange[1], orange[2]);
  cp.setPixelColor(1, purple[0], purple[1], purple[2]);

  delay(1000); // milliseconds

  cp.setPixelColor(0, 0, 0, 0); 
  delay(1000); // milliseconds
}
