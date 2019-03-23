#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
pwm_pin_l=37
sig1_pin_l=40
sig2_pin_l=38

GPIO.setup(pwm_pin_l, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin_l, 10000)
pwm.start(0)
GPIO.setup(sig1_pin_l, GPIO.OUT)
GPIO.setup(sig2_pin_l, GPIO.OUT)

while 1:

    #i=0
    #while i<15:
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        pwm.ChangeDutyCycle(min(abs(15),100))
