from gpiozero import LED,Button
import time
from signal import pause
    

def traffic():
    red = LED(18)
    yellow = LED(4)
    green = LED(21)

    
    red.on()
    waiting_time = time.sleep(5)

    while waiting_time != time.sleep(5):
        red.on()
    red.off()

    yellow.on()
    time.sleep(3)
    yellow.off()
    green.on()
    time.sleep(5)
    green.off()


def traffic_control():
    button = Button(2)
    button.when_pressed = traffic
    pause()
    
    
traffic_control()
#button.when_pressed = led.on
#time.sleep(5)
#button.when_released = led.off
#button.when_released = led.off()

#pause()

#while True:
#    led.on()
#    time.sleep(1)
#    led.off()
#    time.sleep(1)

#led.on()
#time.sleep(5)
#led.off()
#
#led2.on()
#time.sleep(5)
#led2.off()
#
#led3.on()
#time.sleep(5)
#led3.off()
