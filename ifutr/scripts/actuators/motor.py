#!/usr/bin/env python

import RPi.GPIO as GPIO

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

    i=0
    while(i<15):
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)
        pwm.ChangeDutyCycle(100)
        i+=1

    while(i<15):
        GPIO.output(sig1_pin_l, GPIO.HIGH)
        GPIO.output(sig2_pin_l, GPIO.LOW)
        GPIO.output(sig1_pin_r, GPIO.HIGH)
        GPIO.output(sig2_pin_r, GPIO.LOW)
        pwm.ChangeDutyCycle(100)
        i+=1
