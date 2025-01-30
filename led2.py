from gpiozero import Button, LED
import time
from signal import pause

button = Button(26, bounce_time=0.05)
red_led = LED(17)
blue_led = LED(27)
green_led = LED(22)

red_led.off()
blue_led.off()
green_led.off()

led_index = 0

def switch_led():
    global led_index
    if led_index == 0:
        red_led.on()
        blue_led.off()
        green_led.off()
        led_index += 1
    elif led_index == 1:
        red_led.off()
        blue_led.on()
        green_led.off()
        led_index += 1
    elif led_index == 2:
        red_led.off()
        blue_led.off()
        green_led.on()
        led_index = 0

button.when_pressed = switch_led
pause()

# Более сокращенный вариант, у методов включения и выключения нет скобок, так как это вызовы функций
# а when_pressed  это коллбеки, реакция которых направляется во включение и выключение ЛЕД
#button.when_pressed = led.on
#button.when_released = led.off
#pause()

# Запуск цикла для отлавливания нажатия кнопки
# тайм слип существенно улучшает производительность
#while True:
#    time.sleep(0.01)
#    isPressed = button.is_pressed
#    if isPressed:
#        led.on()
#    else:
#        led.off()
        
    