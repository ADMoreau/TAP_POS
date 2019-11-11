#include "FastLED.h"
#include "patterns.h"

#define CMDBUFSIZE 32
char cmdBuffer[CMDBUFSIZE];
int charsRead;

CRGB colors[] = {CRGB::AliceBlue, CRGB::Amethyst, CRGB::AntiqueWhite, CRGB::Aqua, CRGB::Aquamarine, CRGB::Azure, CRGB::Beige, CRGB::Bisque,
                CRGB::BlanchedAlmond, CRGB::Blue, CRGB::BlueViolet, CRGB::Brown, CRGB::BurlyWood, CRGB::CadetBlue, CRGB::Chartreuse, CRGB::Chocolate,
                CRGB::Coral, CRGB::CornflowerBlue, CRGB::Cornsilk, CRGB::Crimson, CRGB::Cyan, CRGB::DarkBlue, CRGB::DarkCyan, CRGB::DarkGoldenrod, CRGB::DarkGray,
                CRGB::DarkGreen, CRGB::DarkKhaki, CRGB::DarkMagenta, CRGB::DarkOliveGreen, CRGB::DarkOrange, CRGB::DarkOrchid, CRGB::DarkRed, CRGB::DarkSalmon,
                CRGB::DarkSeaGreen, CRGB::DarkSlateBlue, CRGB::DarkSlateGray, CRGB::DarkTurquoise, CRGB::DarkViolet, CRGB::DeepPink, CRGB::DeepSkyBlue,
                CRGB::DimGray, CRGB::DodgerBlue, CRGB::FireBrick, CRGB::FloralWhite, CRGB::ForestGreen, CRGB::Fuchsia, CRGB::Gainsboro, CRGB::GhostWhite, CRGB::Gold,
                CRGB::Goldenrod, CRGB::Gray, CRGB::Green, CRGB::GreenYellow, CRGB::Honeydew, CRGB::HotPink, CRGB::IndianRed, CRGB::Indigo, CRGB::Ivory, CRGB::Khaki, CRGB::Lavender,
                CRGB::LavenderBlush, CRGB::LawnGreen, CRGB::LemonChiffon, CRGB::LightBlue, CRGB::LightCoral, CRGB::LightCyan, CRGB::LightGoldenrodYellow,
                CRGB::LightGreen, CRGB::LightGrey, CRGB::LightPink, CRGB::LightSalmon, CRGB::LightSeaGreen, CRGB::LightSkyBlue, CRGB::LightSlateGray, CRGB::LightSteelBlue,
                CRGB::LightYellow, CRGB::Lime, CRGB::LimeGreen, CRGB::Linen, CRGB::Magenta, CRGB::Maroon, CRGB::MediumAquamarine, CRGB::MediumBlue, CRGB::MediumOrchid,
                CRGB::MediumPurple, CRGB::MediumSeaGreen, CRGB::MediumSlateBlue, CRGB::MediumSpringGreen, CRGB::MediumTurquoise, CRGB::MediumVioletRed,
                CRGB::MidnightBlue, CRGB::MintCream, CRGB::MistyRose, CRGB::Moccasin, CRGB::NavajoWhite, CRGB::Navy, CRGB::OldLace, CRGB::Olive, CRGB::OliveDrab, CRGB::Orange,
                CRGB::OrangeRed, CRGB::Orchid, CRGB::PaleGoldenrod, CRGB::PaleGreen, CRGB::PaleTurquoise, CRGB::PaleVioletRed, CRGB::PapayaWhip, CRGB::PeachPuff,
                CRGB::Peru, CRGB::Pink, CRGB::Plaid, CRGB::Plum, CRGB::PowderBlue, CRGB::Purple, CRGB::Red, CRGB::RosyBrown, CRGB::RoyalBlue, CRGB::SaddleBrown, CRGB::Salmon,
                CRGB::SandyBrown, CRGB::SeaGreen, CRGB::Seashell, CRGB::Sienna, CRGB::Silver, CRGB::SkyBlue, CRGB::SlateBlue, CRGB::SlateGray, CRGB::Snow, CRGB::SpringGreen,
                CRGB::SteelBlue, CRGB::Tan, CRGB::Teal, CRGB::Thistle, CRGB::Tomato, CRGB::Turquoise, CRGB::Violet, CRGB::Wheat, CRGB::White, CRGB::WhiteSmoke, CRGB::Yellow, CRGB::YellowGreen}; 

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
      solid_color(colors[pattern], profOneNUM, profTwoNUM, profThreeNUM, profFourNUM, profFiveNUM, rarityDotzNUM, indicaLEDsNUM);
      
      /*
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
      }*/
    }

    ledReset();
  }
}
