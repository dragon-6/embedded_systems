from gpiozero import LED
from time import sleep

led = LED(17) # BCM GPIO17

try:
    led.on()  # HIGH (점등)
    sleep(2)
finally:
    led.off() # LOW (소등)
    led.close() # 리소스 반환