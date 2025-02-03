from gpiozero import MotionSensor, Button, LED
import time
from signal import pause

pir = MotionSensor(4)

red_led = LED(17)
blue_led = LED(27)
green_led = LED(22)
led_list = [red_led, blue_led, green_led]

def all_leds_on():
    for l in led_list:
            l.on()
            
def all_leds_off():
    for l in led_list:
            l.off()
pir.when_motion = all_leds_on
pir.when_no_motion = all_leds_off

pause()
    