import time
import RPi.GPIO as GPIO


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def bitSignal(dictionary, timeUnit, startIndex):

    i = startIndex

    # print("timeUnit: " + str(timeUnit))
    # print("bitNumber: " + str(decimalToBinary(int(timeUnit))[::-1]))

    for item in (decimalToBinary(int(timeUnit))[::-1]):
        if item == "1":
            # print("i: " + str(i))
            # print("Output on: " + str(dictionary["l"+str(startIndex)]))
            GPIO.output(dictionary["l"+str(i)], 1)
            i += 1
        elif item == "0":
            # print("i: " + str(i))
            GPIO.output(dictionary["l"+str(i)], 0)
            i += 1


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


gpio_dict = {"l0": 4, "l1": 17, "l2": 27, "l3": 22, "l4": 5, "l5": 6, "l6": 13, "l7": 19,
             "l8": 26, "l9": 21, "l10": 20, "l11": 16, "l12": 12, "l13": 25, "l14": 24, "l15": 23, "l16": 18}

for element in gpio_dict.values():
    GPIO.setup(element, GPIO.OUT)

while True:
    Hr, Min, Sec = time.strftime("%H %M %S").split(sep=" ")
    bitSignal(gpio_dict, Hr, 0)
    bitSignal(gpio_dict, Min, 5)
    bitSignal(gpio_dict, Sec, 11)
