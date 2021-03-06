#!/usr/bin/env python

import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BOARD)
pwm_pin_r=37
sig1_pin_r=40
sig2_pin_r=38

pwm_pin_l=11
sig1_pin_l=13
sig2_pin_l=15

GPIO.setup(pwm_pin_l, GPIO.OUT)
pwm_l = GPIO.PWM(pwm_pin_l, 10000)
pwm_l.start(0)
GPIO.setup(sig1_pin_l, GPIO.OUT)
GPIO.setup(sig2_pin_l, GPIO.OUT)

GPIO.setup(pwm_pin_r, GPIO.OUT)
pwm_r = GPIO.PWM(pwm_pin_r, 10000)
pwm_r.start(0)
GPIO.setup(sig1_pin_r, GPIO.OUT)
GPIO.setup(sig2_pin_r, GPIO.OUT)

while 1:


    pwm_l.ChangeDutyCycle(99)
    pwm_r.ChangeDutyCycle(100)

    i=0
    while(i<5):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        i+=1
        time.sleep(.1)
        print('go straight')
    GPIO.output(sig1_pin_l, GPIO.LOW)
    GPIO.output(sig2_pin_l, GPIO.LOW)
    GPIO.output(sig1_pin_r, GPIO.LOW)
    GPIO.output(sig2_pin_r, GPIO.LOW)


    i=0
    pwm_l.ChangeDutyCycle(90)
    pwm_r.ChangeDutyCycle(80)

    while(i<150):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        i+=1
        time.sleep(.1)
        print('go straight')
    GPIO.output(sig1_pin_l, GPIO.LOW)
    GPIO.output(sig2_pin_l, GPIO.LOW)
    GPIO.output(sig1_pin_r, GPIO.LOW)
    GPIO.output(sig2_pin_r, GPIO.LOW)
    #time.sleep(3)

    i=0
    pwm_l.ChangeDutyCycle(97)
    pwm_r.ChangeDutyCycle(100)

    while(i<40):
            GPIO.output(sig1_pin_l, GPIO.HIGH)
            GPIO.output(sig2_pin_l, GPIO.LOW)
            GPIO.output(sig1_pin_r, GPIO.HIGH)
            GPIO.output(sig2_pin_r, GPIO.LOW)

            i+=1
            time.sleep(.1)
            print('go straight')
    GPIO.output(sig1_pin_l, GPIO.LOW)
    GPIO.output(sig2_pin_l, GPIO.LOW)
    GPIO.output(sig1_pin_r, GPIO.LOW)
    GPIO.output(sig2_pin_r, GPIO.LOW)
        #time.sleep(3)

    i=0
    pwm_l.ChangeDutyCycle(90)
    pwm_r.ChangeDutyCycle(89)

    while(i<100):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        i+=1
        time.sleep(.1)
        print('go straight')
    GPIO.output(sig1_pin_l, GPIO.LOW)
    GPIO.output(sig2_pin_l, GPIO.LOW)
    GPIO.output(sig1_pin_r, GPIO.LOW)
    GPIO.output(sig2_pin_r, GPIO.LOW)
    #time.sleep(3)


    i=0
    pwm_l.ChangeDutyCycle(95)
    pwm_r.ChangeDutyCycle(100)

    while(i<15):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        i+=1
        time.sleep(.1)
        print('go straight')
    GPIO.output(sig1_pin_l, GPIO.LOW)
    GPIO.output(sig2_pin_l, GPIO.LOW)
    GPIO.output(sig1_pin_r, GPIO.LOW)
    GPIO.output(sig2_pin_r, GPIO.LOW)
    #time.sleep(3)

    pwm_l.ChangeDutyCycle(100)
    pwm_r.ChangeDutyCycle(100)

    while(i<50):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        i+=1
        time.sleep(.1)
        print('go straight')
    GPIO.output(sig1_pin_l, GPIO.LOW)
    GPIO.output(sig2_pin_l, GPIO.LOW)
    GPIO.output(sig1_pin_r, GPIO.LOW)
    GPIO.output(sig2_pin_r, GPIO.LOW)
    time.sleep(10)

    j=0
    while(j<15):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.LOW)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        j+=1
        time.sleep(0.1)
        print('turn')

    i=0
    while(i<30):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        i+=1
        time.sleep(.1)
        print('go straight')

    GPIO.output(sig1_pin_l, GPIO.LOW)
    GPIO.output(sig2_pin_l, GPIO.LOW)
    GPIO.output(sig1_pin_r, GPIO.LOW)
    GPIO.output(sig2_pin_r, GPIO.LOW)
    time.sleep(5)

    j=0
    while(j<10):
        GPIO.output(sig1_pin_l, GPIO.LOW)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        j+=1
        time.sleep(0.1)
        print('turn')

    i=0
    while(i<30):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)

        i+=1
        time.sleep(.1)
        print('go straight')

    GPIO.output(sig1_pin_l, GPIO.LOW)
    GPIO.output(sig2_pin_l, GPIO.LOW)
    GPIO.output(sig1_pin_r, GPIO.LOW)
    GPIO.output(sig2_pin_r, GPIO.LOW)
    time.sleep(15)
