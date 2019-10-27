#include <ArduinoJson.h>
#include <Adafruit_NeoPixel.h>


void setup() 
{
  Serial.begin(9600);
  while (!Serial) continue;
 //DynamicJsonDocument doc(200);
  StaticJsonDocument<200> doc;
 

 char json[] = "{\"result\" : \"yeehaw\"}";

 DeserializationError error = deserializeJson(doc, json);

 if(error)
 {
  Serial.print(F("deserialization() failed"));
  Serial.println(error.c_str());
  return;
 }
 
 Serial.println((char*)doc["result"]);


 

}

void loop() {
 
    

}
