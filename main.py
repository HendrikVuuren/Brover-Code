from machine import SoftI2C, Pin
from motor import Motor
import ultrasonic
from APDS9960LITE import APDS9960LITE
import time as t
from encoder import Encoder
from pyb import Pin, ADC




IR_sensorL = ADC(Pin("A0"))
IR_sensorML = ADC(Pin("A1"))
IR_sensorMR = ADC(Pin("A2"))
IR_sensorR = ADC(Pin("A3"))


motorL = Motor('left', 'D6', 'D7', 'D4')
motorR = Motor('right', 'D8', 'D9', 'D5')

TRIG = 'D13'
ECHO = 'D12'
ultrasonic_sensor = ultrasonic.HCSR04(TRIG, ECHO)

ENC_L = "D2"
ENC_R = "D3"
enc = Encoder(ENC_L, ENC_R)

#greyscale code lines 31-43

# while True:
#     w1 = IR_sensorL.read()
#     w2 = IR_sensorML.read()
#     w3 = IR_sensorMR.read()
#     w4 = IR_sensorR.read()
#
#     numerator =
#     denominator =
#
#     line_dist = numerator/denominator;
#
#     print("Distance from line = {:3.2f}".format(line_dist));
#     t.sleep(0.1);

i2c = SoftI2C(scl=Pin("PB13"), sda=Pin("PB14"))
apds9960=APDS9960LITE(i2c)

speed = 70

while True:

    IR_readingL = IR_sensorL.value()
    IR_readingML = IR_sensorML.value()
    IR_readingMR = IR_sensorMR.value()
    IR_readingR = IR_sensorR.value()
    dist = ultrasonic_sensor.distance_mm()

    motorL.set_forwards()
    motorR.set_forwards()
    motorR.duty(speed)
    motorL.duty(speed)

    #print(IR_readingL, IR_readingML, IR_readingMR, IR_readingR)

    if IR_readingML == 1 and IR_readingMR == 1 and IR_readingL == 0 and IR_readingR == 0:
        motorR.duty(speed)
        motorL.duty(speed)
    elif IR_readingML == 1 and IR_readingMR == 1 and IR_readingL == 1 and IR_readingR == 0:
        motorR.duty(speed*1.25)
        t.sleep(1)
    elif IR_readingML == 1 and IR_readingMR == 1 and IR_readingL == 0 and IR_readingR == 1:
        motorL.duty(speed*1.25)
        t.sleep(1)
#pwm/encoder
    # pwm = 65
    # for pwm in range(0, 100, 5):
    #     motorL.set_forwards()
    #     motorR.set_forwards()
    #     enc.clear_count()
    #     motorL.duty(pwm)
    #     motorR.duty(pwm)
    #     motorR.duty(pwm)
    #     t.sleep(1)
    #
    #     left_count = enc.get_left()
    #     right_count = enc.get_right()
    #
    #     print("{:3d}, {:4d}, {:4d}".format(pwm, left_count, right_count))
    #

    apds9960.prox.enableSensor()
    t.sleep(0.1)

    dist = ultrasonic_sensor.distance_mm()
    proximity_measurement = apds9960.prox.proximityLevel
    ultrasonic_measurement_mm = dist
    print("RGB: {:3d},US: {:4.2f},IRL: {},IRLM: {},IRRM: {},IRR: {}".format(proximity_measurement,dist, IR_readingL, IR_readingML, IR_readingMR, IR_readingR))
    t.sleep(0.1)


print("PWM, ENC_L, ENC_R")

#while True:
    # pwm = 65
    # for pwm in range(0, 100, 5):
    #     motor_left.set_forwards()
    #     motor_right.set_forwards()
    #     enc.clear_count()
    #     motor_left.duty(pwm)
    #     motor_right.duty(pwm)
    #     sleep(1)
    #
    #     left_count = enc.get_left()
    #     right_count = enc.get_right()
    #
    #     print("{:3d}, {:4d}, {:4d}".format(pwm, left_count, right_count))



