import time
import RPi.GPIO as GPIO


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def bitSignal(dictionary, timeUnit, startIndex):

    i = startIndex

    for item in (decimalToBinary(int(timeUnit))[::-1]):
        print("Startitem: " + str(i))
        print(item)
        if item == 1:
            GPIO.output(dictionary["l"+str(startIndex)], 1)
            i += 1
        elif item == 0:
            GPIO.output(dictionary["l"+str(startIndex)], 0)
            i += 1


GPIO.setmode(GPIO.BCM)


gpio_dict = {"l0": 4, "l1": 17, "l2": 27, "l3": 22, "l4": 5, "l5": 6, "l6": 13, "l7": 19,
             "l8": 26, "l9": 21, "l10": 20, "l11": 16, "l12": 12, "l13": 25, "l14": 24, "l15": 23, "l16": 18}


while True:
    Hr, Min, Sec = time.strftime("%H %M %S").split(sep=" ")
    print(Hr, Min, Sec)
    bitSignal(gpio_dict, Hr, 0)
    bitSignal(gpio_dict, Min, 5)
    bitSignal(gpio_dict, Sec, 11)
    time.sleep(1.0)
