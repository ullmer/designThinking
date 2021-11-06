#include <Adafruit_CircuitPlayground.h>

Adafruit_CircuitPlayground cp;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  cp.begin();
}

////////////////////////////////////////////////////////////////////////////
void loop() {
  int orange[3] = {60, 24, 0}, purple[3] = {60, 0, 60};
  // Print cap touch reading on serial port.
  int cap0 = cp.readCap(1);
  Serial.println(cap0);

  if (cap0 > 100) {
    cp.setPixelColor(0, orange[0], orange[1], orange[2]);
    cp.setPixelColor(1, purple[0], purple[1], purple[2]);
  } else {
    cp.setPixelColor(0, 0,0,0);
    cp.setPixelColor(1, 0,0,0);
  }
  // Update rate.
  delay(100);
}

  
