#!/usr/bin/python
import RPi.GPIO as GPIO #import GPIO functionalilty
from time import sleep #import the sleep function, for wating between turning LEDs on/off
from sys import exc_info #for requesting error information
 
#pins = [4, 25, 24, 23, 22, 27, 18, 17] #list of the pin number on the pi
pins = [4, 25, 24]
#ONTIME = 0.14 #set the amount of time in seconds that the LEDS will be on for


def setup(): #setup
    GPIO.setmode(GPIO.BCM) #setting the mode of the pins
    for pin in pins: #creating a for loop to do the below line for all of the pins
        GPIO.setup(pin, GPIO.OUT) #setting the pin as an output
    print("pins have been SETUP ")

def pinsOff(): #pinsOff
    for pin in pins: #creating a for loop to do the below line for all of the pins
        GPIO.output(pin, GPIO.LOW) #turning the pin off
    print("pins have been set LOW")


def toggle(status):
    setup()
    pinsOff()
    if status == 0:
        #turn LEDs on
        print("turn on")
        for i in pins: #
            GPIO.output(i, GPIO.HIGH) #turn the LED on
    else:
        print("turn off")
        #turn LEDs off
        for i in pins: #
            GPIO.output(i, GPIO.LOW) #turn the LED on
            

def main1(): #main1
    print("main1called")
    setup() #running the setup function
    pinsOff() #making sure the pins are off
    ONTIME = 0.14
    while ONTIME > 0: #specifying how long the loop is to run for
        for i in pins: #
            GPIO.output(i, GPIO.HIGH) #turn the LED on
            sleep(ONTIME) #wait ONTIME seconds
            GPIO.output(i, GPIO.LOW) #turn the LED off
        ONTIME -= 0.02 #Take amount of time from ONTIME
    pinsOff() #ensuring all LEDs are off
    GPIO.cleanup() #returning pins to a neutral state

"""
try: #running the function above in a try/ecept loop because if an error occurs, the LEDs can still be turned off to save the pi
    #main1() #run the code above
    print("doing this")
except KeyboardInterrupt: #if CTRL+c is pressed during running
    print("user cancelled running ")
    pinsOff() #turn the pins off 
    GPIO.cleanup() #returning pins to a neutral state
except: #if an error occurs
    print("unexpected error ", exc_info()) #outputs the error message to the screen
    raise #brings the error message to the top of the output to make sure it is seen
    pinsOff() #turn the pins off
    GPIO.cleanup() #returning pins to a neutral state
    
"""