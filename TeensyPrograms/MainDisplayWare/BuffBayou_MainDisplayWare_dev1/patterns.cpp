#include "FastLED.h"
#include "patterns.h"

#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB
#define BRIGHTNESS          222
#define NUM_LEDS_PER_STRIP 63

CRGB profOne[NUM_LEDS_PER_STRIP];
CRGB profTwo[NUM_LEDS_PER_STRIP];
CRGB profThree[NUM_LEDS_PER_STRIP];
CRGB profFour[NUM_LEDS_PER_STRIP];
CRGB profFive[NUM_LEDS_PER_STRIP];
CRGB rarityDotz[NUM_LEDS_PER_STRIP];
CRGB indicaLEDs[NUM_LEDS_PER_STRIP];

uint8_t gHue = 200;

uint8_t FRAMES_PER_SECOND = 120;

const void mainLEDSetup()
{
  Serial.println("Setting up LEDs");

  FastLED.addLeds<NEOPIXEL, 2>(profOne, NUM_LEDS_PER_STRIP);

  FastLED.addLeds<NEOPIXEL, 14>(profTwo, NUM_LEDS_PER_STRIP);

  FastLED.addLeds<NEOPIXEL, 7>(profThree, NUM_LEDS_PER_STRIP);

  FastLED.addLeds<NEOPIXEL, 8>(profFour, NUM_LEDS_PER_STRIP);

  FastLED.addLeds<NEOPIXEL, 6>(profFive, NUM_LEDS_PER_STRIP);

  FastLED.addLeds<NEOPIXEL, 20>(rarityDotz, NUM_LEDS_PER_STRIP);

  FastLED.addLeds<NEOPIXEL, 21>(indicaLEDs, NUM_LEDS_PER_STRIP);

  FastLED.setBrightness(BRIGHTNESS);
}

const void ledReset() 
{
  // funtion to turn all of the leds off
  for(int i = NUM_LEDS_PER_STRIP; i >= 0; i--) { //9948
    profOne[i] = CRGB::Black;
    profTwo[i] = CRGB::Black;
    profThree[i] = CRGB::Black;
    profFour[i] = CRGB::Black;
    profFive[i] = CRGB::Black;
    rarityDotz[i] = CRGB::Black;
  }
  FastLED.show();
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
CRGB Wheel(byte WheelPos) {
  if(WheelPos < 85) {
    return CRGB(WheelPos * 3, 255 - WheelPos * 3, 0);
  } 
  else if(WheelPos < 170) {
    WheelPos -= 85;
    return CRGB(255 - WheelPos * 3, 0, WheelPos * 3);
  } 
  else {
    WheelPos -= 170;
    return CRGB(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

const void bpm(int profOneNUM, int profTwoNUM, int profThreeNUM, int profFourNUM, int profFiveNUM, int rarityDotzNUM, int indicaLEDsNUM)
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 40;
  CRGBPalette16 palette = PartyColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for(int i = profOneNUM-1; i >= 0; i--) { //9948
    profOne[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
  for( int i = profTwoNUM-1; i >= 0; i--) { //9948
    profTwo[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
  for( int i = profThreeNUM-1; i >= 0; i--){ //9948
    profThree[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
  for( int i = profFourNUM-1; i >= 0; i--) { //9948
    profFour[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
  for( int i = profFiveNUM-1; i >= 0; i--) { //9948
    profFive[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
  for( int i = rarityDotzNUM-1; i >= 0; i--) { //9948
    rarityDotz[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
  indicaLEDs[indicaLEDsNUM] = ColorFromPalette(palette, gHue+(indicaLEDsNUM*2), beat-gHue+(indicaLEDsNUM*10));

  FastLED.show();
  FastLED.delay(1000/FRAMES_PER_SECOND); 
}

const void radialPaletteShift(int profOneNUM, int profTwoNUM, int profThreeNUM, int profFourNUM, int profFiveNUM, int rarityDotzNUM, int indicaLEDsNUM)
{
  CRGBPalette16 palette = PartyColors_p;
  for (uint16_t i = 0; i < profOneNUM; i++) {
    // leds[i] = ColorFromPalette( gCurrentPalette, gHue + sin8(i*16), brightness);
    profOne[i] = ColorFromPalette(palette, i + gHue, 255, LINEARBLEND);
  }
  for (uint16_t i = 0; i < profTwoNUM; i++) {
    // leds[i] = ColorFromPalette( gCurrentPalette, gHue + sin8(i*16), brightness);
    profTwo[i] = ColorFromPalette(palette, i + gHue, 255, LINEARBLEND);
  }
  for (uint16_t i = 0; i < profThreeNUM; i++) {
    // leds[i] = ColorFromPalette( gCurrentPalette, gHue + sin8(i*16), brightness);
    profThree[i] = ColorFromPalette(palette, i + gHue, 255, LINEARBLEND);
  }
  for (uint16_t i = 0; i < profFourNUM; i++) {
    // leds[i] = ColorFromPalette( gCurrentPalette, gHue + sin8(i*16), brightness);
    profFour[i] = ColorFromPalette(palette, i + gHue, 255, LINEARBLEND);
  }
  for (uint16_t i = 0; i < profFiveNUM; i++) {
    // leds[i] = ColorFromPalette( gCurrentPalette, gHue + sin8(i*16), brightness);
    profFive[i] = ColorFromPalette(palette, i + gHue, 255, LINEARBLEND);
  }
  for (uint16_t i = 0; i < rarityDotzNUM; i++) {
    // leds[i] = ColorFromPalette( gCurrentPalette, gHue + sin8(i*16), brightness);
    rarityDotz[i] = ColorFromPalette(palette, i + gHue, 255, LINEARBLEND);
  }
  indicaLEDs[indicaLEDsNUM] = ColorFromPalette(palette, indicaLEDsNUM + gHue, 255, LINEARBLEND);
  
  FastLED.show();
  FastLED.delay(1000/FRAMES_PER_SECOND); 
}

const void solid_color(CRGB c, int profOneNUM, int profTwoNUM, int profThreeNUM, int profFourNUM, int profFiveNUM, int rarityDotzNUM, int indicaLEDsNUM)
{
  for (uint16_t i = 0; i < profOneNUM; i++) {
    profOne[i] = c;
  }
  for (uint16_t i = 0; i < profTwoNUM; i++) {
    profTwo[i] = c;
  }
  for (uint16_t i = 0; i < profThreeNUM; i++) {
    profThree[i] = c;
  }
  for (uint16_t i = 0; i < profFourNUM; i++) {
    profFour[i] = c;
  }
  for (uint16_t i = 0; i < profFiveNUM; i++) {
    profFive[i] = c;
  }
  for (uint16_t i = 0; i < rarityDotzNUM; i++) {
    rarityDotz[i] = c;
  }
  indicaLEDs[indicaLEDsNUM] = c;
  
  FastLED.show();
  FastLED.delay(1000/FRAMES_PER_SECOND); 
}

const void rainbow(int profOneNUM, int profTwoNUM, int profThreeNUM, int profFourNUM, int profFiveNUM, int rarityDotzNUM, int indicaLEDsNUM)
{
  int cycles = 1;
  for(int j=0; j<256*cycles; j++) {
      for (uint16_t i = 0; i < profOneNUM; i++) {
        profOne[i] = Wheel(((i * 256 / profOneNUM) + j) & 255);
      }
      for (uint16_t i = 0; i < profTwoNUM; i++) {
        profTwo[i] = Wheel(((i * 256 / profTwoNUM) + j) & 255);
      }
      for (uint16_t i = 0; i < profThreeNUM; i++) {
        profThree[i] = Wheel(((i * 256 / profThreeNUM) + j) & 255);
      }
      for (uint16_t i = 0; i < profFourNUM; i++) {
        profFour[i] = Wheel(((i * 256 / profFourNUM) + j) & 255);
      }
      for (uint16_t i = 0; i < profFiveNUM; i++) {
        profFive[i] = Wheel(((i * 256 / profFiveNUM) + j) & 255);
      }
      for (uint16_t i = 0; i < rarityDotzNUM; i++) {
        rarityDotz[i] = Wheel(((i * 256 / rarityDotzNUM) + j) & 255);
      }
      indicaLEDs[indicaLEDsNUM] = Wheel(((256 / indicaLEDsNUM) + j) & 255);
      
      FastLED.show();
      FastLED.delay(1000/FRAMES_PER_SECOND); 
  }
}
