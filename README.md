# IMU Muscle Fatigue Detection

The goal of this project is to detect potential muscle fatigue using inertial (gyroscope and accelerometer) data. Weak muscles can cause subtle yet detectable changes in everyday movements, which could be detected by a wearable IMU sensor. We also help to fuse this IMU data with EMG (electromyography) data.

## Current Status

This project is still very early in it's experimental stage. The setup consists of an MPU9255 IMU connected via I2C to an ESP32. Only gyro and accelerometer data are used (so an MPU6050 can be used instead as well). The current area of work is inferring human activities like walking, sitting etc., and also detecting and characterising sit-to-stand and stand-to-sit transitions.

## Setup and File Description

ESP32 code was written in Arduino flavour, but using PlatformIO extension in VSCode. 

* src/main.cpp is the main driver code for ESP32
* lib/MPU9250 contains the MPU9250 class for interfacing the IMU
* python-util contains programs for collecting and analysing IMU data that the ESP32 sends via USB serial 
