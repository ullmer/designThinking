#include <Adafruit_CircuitPlayground.h>

Adafruit_CircuitPlayground cp;

void setup() {
  // put your setup code here, to run once:
  cp.begin();
}

void loop() {
  Adafruit_CircuitPlayground cp;
  cp.begin();
  int orange[3] = {40, 20, 0}, purple[3] = {40, 0, 40};
  
  cp.setPixelColor(0, orange[0], orange[1], orange[2]);
  cp.setPixelColor(1, purple[0], purple[1], purple[2]);
  delay(1000); // milliseconds

  cp.setPixelColor(0, orange[0]/4, orange[1]/4, orange[2]/4);
  cp.setPixelColor(1, purple[0]/4, purple[1]/4, purple[2]/4);
  delay(1000); // milliseconds

  cp.setPixelColor(0, 0, 0, 0); 
  delay(1000); // milliseconds
}
