#include <Adafruit_CircuitPlayground.h>

Adafruit_CircuitPlayground cp;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  cp.begin();
}

////////////////////////////////////////////////////////////////////////////
void loop() {
  // Print cap touch reading on serial port.
  Serial.println(CircuitPlayground.readCap(1));

  // Update rate.
  delay(100);
}

/*
void loop() {
  Adafruit_CircuitPlayground cp;
  cp.begin();
  int orange[3] = {60, 24, 0}, purple[3] = {60, 0, 60};


  
  cp.setPixelColor(0, orange[0], orange[1], orange[2]);
  cp.setPixelColor(1, purple[0], purple[1], purple[2]);
}
*/
