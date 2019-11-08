#include "FastLED.h"
#include "patterns.h"

#define CMDBUFSIZE 32
char cmdBuffer[CMDBUFSIZE];
int charsRead;

// For mirroring strips, all the "special" stuff happens just in setup.  We
// just addLeds multiple times, once for each strip
void setup() {
  Serial.begin(9600);
  delay(30);
  //Serial.println("Beginning Serial communication");
  //delay(30);
  //Serial Communication Setup
  //Fastled setup
  mainLEDSetup();
  char cmdBuffer[CMDBUFSIZE];
  ledReset();
}

void read_serial() {
  // get message from serial
  charsRead = Serial.readBytesUntil('\n', cmdBuffer, sizeof(cmdBuffer) - 1);  //read entire line
  delay(5);
  cmdBuffer[charsRead] = '\0';       // Make it a C string
  Serial.print(">"); Serial.println(cmdBuffer);
  Serial.flush();
}

void loop() {
  
  //Serial.println("Waiting for serial");
  //delay(30);
  if (Serial.available()) {
    read_serial();
    int profOneNUM = (cmdBuffer[0] - '0') * 12;
    int profTwoNUM =  (cmdBuffer[1] - '0') * 12;
    int profThreeNUM = (cmdBuffer[2] - '0') * 12;
    int profFourNUM = (cmdBuffer[3] - '0') * 12;
    int profFiveNUM = (cmdBuffer[4] - '0') * 12;
    
    int rarityDotzNUM = (cmdBuffer[5] - '0') * 21;
    
    int indicaLEDsNUM1 = (cmdBuffer[6] - '0') * 10;
    int indicaLEDsNUM = (cmdBuffer[7] - '0') + indicaLEDsNUM1;

    int pattern1 = (cmdBuffer[8] - '0') * 10;
    int pattern   = (cmdBuffer[9] - '0') + pattern1;

    unsigned long Time = millis();
    
    //while (millis() < Time + 10000) {
    while (true) {
      if (Serial.available()) {
        read_serial();
        break;
      }
      switch(pattern) 
      {
        case 1:
          bpm(profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 2:
          radialPaletteShift(profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 3:
          all_color(CRGB::White, profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 4:
          all_color(CRGB::Red, profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 5:
          all_color(CRGB::Orange, profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 6:
          all_color(CRGB::Yellow, profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 7:
          all_color(CRGB::Green, profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 8:
          all_color(CRGB::Blue, profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 9:
          all_color(CRGB::Indigo, profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;
        case 10:
          all_color(CRGB::Violet, profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;  
        case 11:
          rainbow(profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
          break;  
      }
      //FastLED.show();
      //FastLED.delay(1000/FRAMES_PER_SECOND); 
      //EVERY_N_MILLISECONDS( 20 ) { gHue++; } // slowly cycle the "base color" through the rainbow
    }

    ledReset();
  }
}


//  for(int i = NUM_LEDS_PER_STRIP-1; i >= 0; i--) {
//    // set our current dot to red, green, and blue
//    profOne[i] = CRGB::Red;
//    profTwo[i] = CRGB::Green;
//    profThree[i] = CRGB::Blue;
//    profFour[i] = CRGB::Yellow;
//    FastLED.show();
//    // clear our current dot before we move on
//    profOne[i] = CRGB::Black;
//    profTwo[i] = CRGB::Black;
//    profThree[i] = CRGB::Black;
//    profFour[i] = CRGB::Black;
//    delay(100);
//  }
//}
