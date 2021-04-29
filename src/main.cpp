#include <MPU9250.h>
#include <Arduino.h>

#define rad2deg 59.29577951 

#define calibrateIMU true   // set false to skip calibration step
#define ACCELBIAS_X 2.38     //TODO: write to EEPROM
#define ACCELBIAS_Y 0.74
#define ACCELBIAS_Z 4.29

// an MPU9250 object with the MPU-9250 sensor on I2C bus 0 with address 0x68
MPU9250 IMU(Wire,0x68);
int status;

void setup() {
  // serial to display data
  Serial.begin(115200);
  while(!Serial) {}

  // start communication with IMU 
  status = IMU.begin();
  if (status < 0) {
    Serial.println("IMU initialization unsuccessful");
    Serial.println("Check IMU wiring or try cycling power");
    Serial.print("Status: ");
    Serial.println(status);
    while(1) {}
  }
  status = IMU.calibrateGyro();
  Serial.println("Gyro cal status: " + String(status));
  if (calibrateIMU){
    status = IMU.calibrateAccel2();
    Serial.println("Accel cal status: " + String(status));
  }
  else {
    // manually set accelbias and scales
    IMU.setAccelCalX(ACCELBIAS_X, 1);
    IMU.setAccelCalY(ACCELBIAS_Y, 1);
    IMU.setAccelCalZ(ACCELBIAS_Z, 1);
  }
  Serial.println("Accel biases: ");
  Serial.print(String(IMU.getAccelBiasX_mss()) + "  " 
              + String(IMU.getAccelBiasY_mss()) + "  "
              + String(IMU.getAccelBiasZ_mss()) + "  ");

  // setting the accelerometer full scale range to +/-8G 
  IMU.setAccelRange(MPU9250::ACCEL_RANGE_8G);
  // setting the gyroscope full scale range to +/-500 deg/s
  IMU.setGyroRange(MPU9250::GYRO_RANGE_500DPS);
  // setting DLPF bandwidth to 20 Hz
  IMU.setDlpfBandwidth(MPU9250::DLPF_BANDWIDTH_20HZ);
  // setting SRD to 19 for a 50 Hz update rate
  IMU.setSrd(19);

  delay(1000);
}

void loop() {
  // read the sensor
  // long tt = millis();
  IMU.readSensor();
  // tt = millis() - tt;

  // display the data
  Serial.print(IMU.getAccelX_mss(),6);
  Serial.print(",");
  Serial.print(IMU.getAccelY_mss(),6);
  Serial.print(",");
  Serial.print(IMU.getAccelZ_mss(),6);
  Serial.print(",");
  Serial.print(rad2deg * IMU.getGyroX_rads(),4);
  Serial.print(",");
  Serial.print(rad2deg * IMU.getGyroY_rads(),4);
  Serial.print(",");
  Serial.print(rad2deg * IMU.getGyroZ_rads(),4);
  Serial.println();
  delay(20);
}

