#include <Wire.h>
#include "Adafruit_MCP23017.h"

// Basic pin reading and pullup test for the MCP23017 I/O expander
// public domain!

// Connect pin #12 of the expander to Analog 5 (i2c clock)
// Connect pin #13 of the expander to Analog 4 (i2c data)
// Connect pins #15, 16 and 17 of the expander to ground (address selection)
// Connect pin #9 of the expander to 5V (power)
// Connect pin #10 of the expander to ground (common ground)
// Connect pin #18 through a ~10kohm resistor to 5V (reset pin, active low)

// Input #0 is on pin 21 so connect a button or switch from there to ground

Adafruit_MCP23017 mcp;
Adafruit_MCP23017 mcp1;
Adafruit_MCP23017 mcp2;



void reset_mcp() {
  for (int i = 0; i<16 ; i++) {
    mcp.pinMode(i, INPUT);
    mcp.pullUp(i, HIGH);  // turn on a 100K pullup internally
    mcp1.pinMode(i, INPUT);
    mcp1.pullUp(i, HIGH);  // turn on a 100K pullup internally
    mcp2.pinMode(i, INPUT);
    mcp2.pullUp(i, HIGH);  // turn on a 100K pullup internally
  }
}
  
void setup() {  
  mcp.begin();      // use default address 0
  mcp1.begin(1);
  mcp2.begin(2);
  reset_mcp();
  Serial1.begin(9600);
}



void loop() {
  Serial.println("Waiting for input");
  // The LED will 'echo' the button
  for (int i = 0; i<16 ; i++) {
    Serial1.println(i);
    if (mcp.digitalRead(i) == 0) {
      Serial1.println(i);
      delay(2);
      Serial1.flush();
    }
  }
  for (int i = 0; i<16 ; i++) {
    if (mcp1.digitalRead(i) == 0) {
      Serial1.println(16 + i);
      delay(2);
      Serial1.flush();
    }
  }
  for (int i = 0; i<16 ; i++) {
    if (mcp2.digitalRead(i) == 0) {
      Serial1.println(32 + i);
      delay(2);
      Serial1.flush();
    }
  }
  delay(60);
}
