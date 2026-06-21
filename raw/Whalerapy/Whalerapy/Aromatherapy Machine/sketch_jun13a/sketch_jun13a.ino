const int Chill = 9;
const int Flower = 10;
const int Wood = 11;
const int Fruit = 12;
const int Energetic = 13;

void setup() {
  // Start the USB communication at 9600 speed
  Serial.begin(9600);
  
  // Set all 5 pins as OUTPUT
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  // Check if Python sent a message over the USB cable
  if (Serial.available() > 0) {
    
    // Read the 5 numbers sent by Python (separated by commas)
    float woodDrops = Serial.parseFloat();
    float flowerDrops = Serial.parseFloat();
    float fruitDrops = Serial.parseFloat();
    float chillDrops = Serial.parseFloat();
    float energeticDrops = Serial.parseFloat();
    
    // Read the newline character at the end
    Serial.readStringUntil('\n');

    // Run the pumps! (5000 milliseconds = 5 seconds per drop)
    runPump(Wood, woodDrops);
    runPump(Flower, flowerDrops);
    runPump(Fruit, fruitDrops);
    runPump(Chill, chillDrops);
    runPump(Energetic, energeticDrops);
  }
}

// Custom function to handle turning a pump on and off
void runPump(int pin, float drops) {
  if (drops > 0) {
    int pumpTime = drops * 5000; // Multiply drops by 5 seconds
    digitalWrite(pin, HIGH);
    delay(pumpTime);
    digitalWrite(pin, LOW);
    delay(500); // Tiny pause between pumps so they don't overlap
  }

}