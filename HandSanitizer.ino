//the time we give the sensor to calibrate (10-60 secs according to the datasheet)
int calibrationTime = 30;        

int pirPin = 3;    //the digital pin connected to the PIR sensor's output
int motorPin = 9;  //the digital pin connected to the transistor to control motor

/////////////////////////////
//SETUP
void setup(){
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  pinMode(motorPin, OUTPUT);
  digitalWrite(pirPin, LOW);
  }

  void loop()
  {
      if(digitalRead(pirPin) == HIGH)
      {
        //Serial.println("Motion Detected");
        digitalWrite(motorPin, HIGH);
        delay(300);
        digitalWrite(motorPin,LOW);
        String pass = "1234";
        Serial.println(pass);
        delay(5000);
      }
      if(digitalRead(pirPin) == LOW)
      {
        digitalWrite(motorPin, LOW);
        //delay(10000);
      }
  }