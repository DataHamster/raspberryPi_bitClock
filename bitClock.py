import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BMC)

gpio_dict = {"l0": 4, "l1": 17, "l2": 27, "l3": 22, "l4": 5, "l5": 6, "l6": 13, "l7": 19,
             "l8": 26, "l9": 21, "l10": 20, "l11": 16, "l12": 12, "l13": 25, "l14": 24, "l15": 23, "l16": 18}

H = time.strftime("%H %M %S").split(sep=" ")


for element in gpio_dict.values():
    GPIO.setup(element, GPIO.OUT)

for i in range(20):
    for element in gpio_dict.values():
        GPIO.output(element, 1)
        time.sleep(0.1)
        GPIO.output(element, 0)
