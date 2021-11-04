#include <Adafruit_CircuitPlayground.h>

Adafruit_CircuitPlayground cp;

void setup() {
  // put your setup code here, to run once:
  cp.begin();
}

void loop() {
  Adafruit_CircuitPlayground cp;
  cp.begin();
  
  int pixel = 0; // pixel 0
  int r = 255; // red component
  int g = 0; // green component
  int b = 0; // blue component
  cp.setPixelColor(pixel, r, g, b); // we specify the pixel number and RGB component values

  delay(1000); // milliseconds

  r = 0; // red component
  g = 0; // green component
  b = 0; // blue component
  cp.setPixelColor(pixel, r, g, b); // alternatively you could use cp.clearPixels() to turn all the pixels off

  delay(1000); // milliseconds
}
