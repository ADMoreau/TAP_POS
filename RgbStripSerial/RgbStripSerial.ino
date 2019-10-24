///////////////////////////////////////////////////////////////////////////////////////////
//
// ALA library example: RgbStripSerial
//
// Original -- 
// Web page: http://yaab-arduino.blogspot.com/p/ala-example-rgbstripserial.html
//
///////////////////////////////////////////////////////////////////////////////////////////

#include <AlaLedRgb.h>
#include <stdlib.h>

#define WS2811_PIN1 5    // WS2811 control connected to pin 6
#define WS2811_PIN2 6
#define WS2811_PIN3 8    //broken wire in port 7
#define WS2811_PIN4 9
#define WS2811_PIN5 10
#define WS2811_PIN6 11
#define WS2811_PIN7 12

#define NUM_PIXELS 5   // number of leds in the LED strip
#define CMDBUFSIZE 32   // buffer size for receiving serial commands

AlaLedRgb rgbStrip1;
AlaLedRgb rgbStrip2;
AlaLedRgb rgbStrip3;
AlaLedRgb rgbStrip4;
AlaLedRgb rgbStrip5;
AlaLedRgb rgbStrip6;
AlaLedRgb rgbStrip7;

char cmdBuffer[CMDBUFSIZE];

// global settings and initial values
int animation = ALA_OFF;
AlaColor color = 0xdddddd;
AlaColor white = 0xffffff;
AlaPalette palette = alaPalNull;
int paletteId=0;
float brightness = 0.3;
long duration = 5000;

void setup()
{
  rgbStrip1.initWS2812(NUM_PIXELS, WS2811_PIN1);
  rgbStrip1.setBrightness(color.scale(brightness));
  rgbStrip1.setAnimation(animation, duration, color);

  rgbStrip2.initWS2812(NUM_PIXELS, WS2811_PIN2);
  rgbStrip2.setBrightness(color.scale(brightness));
  rgbStrip2.setAnimation(animation, duration, color);

  rgbStrip3.initWS2812(NUM_PIXELS, WS2811_PIN3);
  rgbStrip3.setBrightness(color.scale(brightness));
  rgbStrip3.setAnimation(animation, duration, color);

  rgbStrip4.initWS2812(NUM_PIXELS, WS2811_PIN4);
  rgbStrip4.setBrightness(color.scale(brightness));
  rgbStrip4.setAnimation(animation, duration, color);

  rgbStrip5.initWS2812(NUM_PIXELS, WS2811_PIN5);
  rgbStrip5.setBrightness(color.scale(brightness));
  rgbStrip5.setAnimation(animation, duration, color);

  rgbStrip6.initWS2812(NUM_PIXELS, WS2811_PIN6);
  rgbStrip6.setBrightness(color.scale(brightness));
  rgbStrip6.setAnimation(animation, duration, color);

  rgbStrip7.initWS2812(NUM_PIXELS, WS2811_PIN7);
  rgbStrip7.setBrightness(color.scale(brightness));
  rgbStrip7.setAnimation(animation, duration, color);
  
  Serial.begin(9600);

  Serial.println("Welcome to ALA RgbStripSerial example");
  Serial.println("A=[animation code] Set the animation. See https://github.com/bportaluri/ALA/blob/master/src/AlaLed.h");
  Serial.println("B=[brightness]     Set the brightness [0-100]");
  Serial.println("D=[duration]       Set the duration in milliseconds of the animation cycle");
  Serial.println("C=[color]          Set the color (hexadecimal RGB representation ex. 0xE8A240)");
  Serial.println("P=[palette]        Set the palette.");
}

void loop()
{

  if (Serial.available())
  {
    int charsRead;
    charsRead = Serial.readBytesUntil('\n', cmdBuffer, sizeof(cmdBuffer) - 1);  //read entire line
    cmdBuffer[charsRead] = '\0';       // Make it a C string
    Serial.print(">"); Serial.println(cmdBuffer);
    
    if(cmdBuffer[2] != '=' || strlen(cmdBuffer)<3)
    {
      Serial.println("KO");
    }
    else
    {
      switch(cmdBuffer[0])
      {
        
        case '1': 
          Serial.print("Command = "); Serial.println(toupper(cmdBuffer[1]));
          Serial.print("Value = "); Serial.println(atoi(&cmdBuffer[3]));
          switch(toupper(cmdBuffer[1]))
          {
          case 'A':
            animation = atoi(&cmdBuffer[3]);
            Serial.println("OK");
            break;
          case 'B':
            brightness = atoi(&cmdBuffer[3]);
            rgbStrip1.setBrightness(white.scale((float)brightness / 100));
            Serial.println("OK");
            break;
          case 'C':
            color = strtol(&cmdBuffer[3], 0, 16);
            palette=alaPalNull;
            Serial.print(strtol(&cmdBuffer[3], 0, 16));Serial.println(" = Color");
            break;
          case 'D':
            duration = atol(&cmdBuffer[3]);
            Serial.println("OK");
            break;
          case 'P':
            paletteId = atoi(&cmdBuffer[3]);
            switch(paletteId)
            {
            case 0:
              palette=alaPalNull;
              break;
            case 1:
              palette=alaPalRgb;
              break;
            case 2:
              palette=alaPalRainbow;
              break;
            case 3:
              palette=alaPalParty;
              break;
            case 4:
              palette=alaPalHeat;
              break;
            case 5:
              palette=alaPalFire;
              break;
            case 6:
              palette=alaPalCool;
              break;
            }
            break;
          
          default:
            Serial.println("KO");
          }
          
          if(palette==alaPalNull) {
            rgbStrip1.setAnimation(animation, duration, color);
          }
          else {
            rgbStrip1.setAnimation(animation, duration, palette);
          }
          rgbStrip1.runAnimation();
          
        case '2':
           Serial.print("Command = "); Serial.println(toupper(cmdBuffer[0]));
           switch(toupper(cmdBuffer[1]))
              {
              case 'A':
                animation = atoi(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'B':
                brightness = atoi(&cmdBuffer[3]);
                rgbStrip2.setBrightness(white.scale((float)brightness / 100));
                Serial.println("OK");
                break;
              case 'C':
                color = strtol(&cmdBuffer[3], 0, 16);
                palette=alaPalNull;
                Serial.println("OK");
                break;
              case 'D':
                duration = atol(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'P':
                paletteId = atoi(&cmdBuffer[3]);
                switch(paletteId)
                {
                case 0:
                  palette=alaPalNull;
                  break;
                case 1:
                  palette=alaPalRgb;
                  break;
                case 2:
                  palette=alaPalRainbow;
                  break;
                case 3:
                  palette=alaPalParty;
                  break;
                case 4:
                  palette=alaPalHeat;
                  break;
                case 5:
                  palette=alaPalFire;
                  break;
                case 6:
                  palette=alaPalCool;
                  break;
                }
                break;
              
              default:
                Serial.println("KO");
              }
              
              if(palette==alaPalNull)
                rgbStrip2.setAnimation(animation, duration, color);
              else
                rgbStrip2.setAnimation(animation, duration, palette);
            rgbStrip2.runAnimation();
            
        case '3': 
           Serial.print("Command = "); Serial.println(toupper(cmdBuffer[0]));
           switch(toupper(cmdBuffer[1]))
              {
              case 'A':
                animation = atoi(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'B':
                brightness = atoi(&cmdBuffer[3]);
                rgbStrip3.setBrightness(white.scale((float)brightness / 100));
                Serial.println("OK");
                break;
              case 'C':
                color = strtol(&cmdBuffer[3], 0, 16);
                palette=alaPalNull;
                Serial.println("OK");
                break;
              case 'D':
                duration = atol(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'P':
                paletteId = atoi(&cmdBuffer[3]);
                switch(paletteId)
                {
                case 0:
                  palette=alaPalNull;
                  break;
                case 1:
                  palette=alaPalRgb;
                  break;
                case 2:
                  palette=alaPalRainbow;
                  break;
                case 3:
                  palette=alaPalParty;
                  break;
                case 4:
                  palette=alaPalHeat;
                  break;
                case 5:
                  palette=alaPalFire;
                  break;
                case 6:
                  palette=alaPalCool;
                  break;
                }
                break;
              
              default:
                Serial.println("KO");
              }
              
              if(palette==alaPalNull)
                rgbStrip3.setAnimation(animation, duration, color);
              else
                rgbStrip3.setAnimation(animation, duration, palette);
            rgbStrip3.runAnimation();
            
        case '4':
           Serial.print("Command = "); Serial.println(toupper(cmdBuffer[0]));
           switch(toupper(cmdBuffer[1]))
              {
              case 'A':
                animation = atoi(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'B':
                brightness = atoi(&cmdBuffer[3]);
                rgbStrip4.setBrightness(white.scale((float)brightness / 100));
                Serial.println("OK");
                break;
              case 'C':
                color = strtol(&cmdBuffer[3], 0, 16);
                palette=alaPalNull;
                Serial.println("OK");
                break;
              case 'D':
                duration = atol(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'P':
                paletteId = atoi(&cmdBuffer[3]);
                switch(paletteId)
                {
                case 0:
                  palette=alaPalNull;
                  break;
                case 1:
                  palette=alaPalRgb;
                  break;
                case 2:
                  palette=alaPalRainbow;
                  break;
                case 3:
                  palette=alaPalParty;
                  break;
                case 4:
                  palette=alaPalHeat;
                  break;
                case 5:
                  palette=alaPalFire;
                  break;
                case 6:
                  palette=alaPalCool;
                  break;
                }
                break;
              
              default:
                Serial.println("KO");
              }
              
              if(palette==alaPalNull)
                rgbStrip4.setAnimation(animation, duration, color);
              else
                rgbStrip4.setAnimation(animation, duration, palette);
            rgbStrip4.runAnimation();
            
        case '5': 
           Serial.print("Command = "); Serial.println(toupper(cmdBuffer[0]));
           switch(toupper(cmdBuffer[1]))
              {
              case 'A':
                animation = atoi(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'B':
                brightness = atoi(&cmdBuffer[3]);
                rgbStrip5.setBrightness(white.scale((float)brightness / 100));
                Serial.println("OK");
                break;
              case 'C':
                color = strtol(&cmdBuffer[3], 0, 16);
                palette=alaPalNull;
                Serial.println("OK");
                break;
              case 'D':
                duration = atol(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'P':
                paletteId = atoi(&cmdBuffer[3]);
                switch(paletteId)
                {
                case 0:
                  palette=alaPalNull;
                  break;
                case 1:
                  palette=alaPalRgb;
                  break;
                case 2:
                  palette=alaPalRainbow;
                  break;
                case 3:
                  palette=alaPalParty;
                  break;
                case 4:
                  palette=alaPalHeat;
                  break;
                case 5:
                  palette=alaPalFire;
                  break;
                case 6:
                  palette=alaPalCool;
                  break;
                }
                break;
              
              default:
                Serial.println("KO");
              }
              
              if(palette==alaPalNull)
                rgbStrip5.setAnimation(animation, duration, color);
              else
                rgbStrip5.setAnimation(animation, duration, palette);
            rgbStrip5.runAnimation();
            
        case '6': 
           Serial.print("Command = "); Serial.println(toupper(cmdBuffer[0]));
           switch(toupper(cmdBuffer[1]))
              {
              case 'A':
                animation = atoi(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'B':
                brightness = atoi(&cmdBuffer[3]);
                rgbStrip6.setBrightness(white.scale((float)brightness / 100));
                Serial.println("OK");
                break;
              case 'C':
                color = strtol(&cmdBuffer[3], 0, 16);
                palette=alaPalNull;
                Serial.println("OK");
                break;
              case 'D':
                duration = atol(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'P':
                paletteId = atoi(&cmdBuffer[3]);
                switch(paletteId)
                {
                case 0:
                  palette=alaPalNull;
                  break;
                case 1:
                  palette=alaPalRgb;
                  break;
                case 2:
                  palette=alaPalRainbow;
                  break;
                case 3:
                  palette=alaPalParty;
                  break;
                case 4:
                  palette=alaPalHeat;
                  break;
                case 5:
                  palette=alaPalFire;
                  break;
                case 6:
                  palette=alaPalCool;
                  break;
                }
                break;
              
              default:
                Serial.println("KO");
              }
              
              if(palette==alaPalNull)
                rgbStrip6.setAnimation(animation, duration, color);
              else
                rgbStrip6.setAnimation(animation, duration, palette);
            rgbStrip6.runAnimation();
            
        case '7':
           Serial.print("Command = "); Serial.println(toupper(cmdBuffer[0]));
           switch(toupper(cmdBuffer[1]))
              {
              case 'A':
                animation = atoi(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'B':
                brightness = atoi(&cmdBuffer[3]);
                rgbStrip7.setBrightness(white.scale((float)brightness / 100));
                Serial.println("OK");
                break;
              case 'C':
                color = strtol(&cmdBuffer[3], 0, 16);
                palette=alaPalNull;
                Serial.println("OK");
                break;
              case 'D':
                duration = atol(&cmdBuffer[3]);
                Serial.println("OK");
                break;
              case 'P':
                paletteId = atoi(&cmdBuffer[3]);
                switch(paletteId)
                {
                case 0:
                  palette=alaPalNull;
                  break;
                case 1:
                  palette=alaPalRgb;
                  break;
                case 2:
                  palette=alaPalRainbow;
                  break;
                case 3:
                  palette=alaPalParty;
                  break;
                case 4:
                  palette=alaPalHeat;
                  break;
                case 5:
                  palette=alaPalFire;
                  break;
                case 6:
                  palette=alaPalCool;
                  break;
                }
                break;
              
              default:
                Serial.println("KO");
              }
              
              if(palette==alaPalNull)
                rgbStrip7.setAnimation(animation, duration, color);
              else
                rgbStrip7.setAnimation(animation, duration, palette);
            rgbStrip7.runAnimation();
          
      }
    }
  }
  
}
