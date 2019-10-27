#include <FastLED.h>
#include <WiFi.h>

const char* ssid     = "takapiro2";
const char* password = "2kumifriends";
const char* host = "153.171.194.70";

#define NUM_LEDS 298 
#define DATA_PIN 5
#define CLOCK_PIN 13
#define BRIGHTNESS  80

// Define the array of leds
CRGB leds[NUM_LEDS];

void setup() { 
 Serial.begin(115200);
  delay(10);

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  
  FastLED.addLeds<WS2811, DATA_PIN, RGB>(leds, NUM_LEDS);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
      
  FastLED.setBrightness(  BRIGHTNESS );
}

void loop() {
  String line[310];
  delay(3000);

  Serial.print("connecting to ");
  Serial.println(host);

  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }

  String url = "/esp/";

  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  int timeout = millis() + 5000;
  while (client.available() == 0) {
    if (timeout - millis() < 0) {
      Serial.println(">>> Client Timeout !");
      client.stop();
      return;
    }
  }
  //文字列を整数型に変換
  int a=0;
  int temp;
  long colorcode[310];
  while(client.available()){
    line[a] = client.readStringUntil('\r');
    temp = line[a].toInt();
    colorcode[a] = temp;
    a++;
  }
  //デバッグ用
  /*
  Serial.print(colorcode[5]);
  Serial.println(" ");
  Serial.print(colorcode[6]);
  Serial.println(" ");
  Serial.print(colorcode[7]);
  Serial.println(" ");
  */
  //面とLEDの番号の対応配列
  int men1[] = {0, 1, 6, 7, 8, 15, 16, 17, 18, 27, 28, 29, 30, 31, 32, 45, 46, 47, 48, 49, 50, 51, 66, 67, 68, 69, 70, 71, 72, 73, 90, 91, 92, 93, 94, 95, 96, 97, 98, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254};
  int men2[] = {2, 3, 9, 10, 11, 19, 20, 21, 22, 33, 34, 35, 36, 37, 38, 52, 53, 54, 55, 56, 57, 58, 74, 75, 76, 77, 78, 79, 80, 81, 99, 100, 101, 102, 103, 104, 105, 106, 107, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266};
  int men3[] = {4, 5, 12, 13, 14, 23, 24, 25, 26, 39, 40, 41, 42, 43, 44, 59, 60, 61, 62, 63, 64, 65, 82, 83, 84, 85, 86, 87, 88, 89, 108, 109, 110, 111, 112, 113, 114, 115, 116, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278};
  //入れ替え
  for(int s=0;s<93;s++){
    leds[men3[s]]=leds[men2[s]]; 
  }
  for(int t=0;t<93;t++){
    leds[men2[t]]=leds[men1[t]]; 
  }
  //入手した発光パターンを適用
  for(int i=0;i<93;i++){
    leds[men1[i]].setRGB(colorcode[3*i+7], colorcode[3*i+8], colorcode[3*i+9]);
  }
  
  FastLED.show();
}
