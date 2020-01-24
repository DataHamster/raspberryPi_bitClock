import time
import RPi.GPIO as GPIO


def decimalToBinary(n):
    bitCode = bin(n).replace("0b", "")
    while True:
        if len(bitCode) < 6:
            bitCode = "0" + bitCode
        else:
            break

    return bitCode


def bitSignal(dictionary, timeUnit, startIndex):

    i = startIndex

    for item in (decimalToBinary(int(timeUnit))[::-1]):

        if item == "1":
            GPIO.output(dictionary["l"+str(i)], 1)
            print("input i: " + str(i))
            i += 1
        elif item == "0":
            GPIO.output(dictionary["l"+str(i)], 0)
            print("output i: " + str(i))
            i += 1


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


gpio_dict = {"l0": 4, "l1": 17, "l2": 27, "l3": 22, "l4": 5, "l5": 6, "l6": 13, "l7": 19,
             "l8": 26, "l9": 21, "l10": 20, "l11": 16, "l12": 12, "l13": 25, "l14": 24, "l15": 23, "l16": 18}

for element in gpio_dict.values():
    GPIO.setup(element, GPIO.OUT)
    GPIO.output(element, 0)


while True:
    Hr, Min, Sec = time.strftime("%H %M %S").split(sep=" ")
    bitSignal(gpio_dict, Hr, 0)
    bitSignal(gpio_dict, Min, 5)
    bitSignal(gpio_dict, Sec, 11)
