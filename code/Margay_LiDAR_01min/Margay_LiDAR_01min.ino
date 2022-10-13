#include "Margay.h"
#include "SymbiontLiDAR.h"

// Instantiate classes
SymbiontLiDAR myLaser;
Margay Logger; // Margay v2.2; UPDATE CODE TO INDICATE THIS

// Empty header to start; will include sensor labels and information
String header = "";

// I2CVals for Symbiont
uint8_t I2CVals[] = {0x50}; // DEFAULT

//Number of seconds between readings
uint32_t updateRate = 300;

void setup(){
    header = header + myLaser.getHeader();
    Logger.begin(I2CVals, sizeof(I2CVals), header);
    initialize();
}

void loop(){
    Logger.run(update, updateRate);
}

String update() {
    initialize();
    return myLaser.getString();
}

void initialize(){
    myLaser.begin();
}
