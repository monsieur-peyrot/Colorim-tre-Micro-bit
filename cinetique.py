"""
Colorimètre Micro:bit
Suivi de cinétique v1.0
Décembre 2023 par Bruno PEYROT
"""

from microbit import *
from math import *

zero = 512
display.clear()

while True:
    sleep(1000)
    display.show("?")
    print()
    print("A : Etalonnage")
    print("B : Mesures")
    print()
    while not(button_a.is_pressed()) and not(button_b.is_pressed()):
        pass
    if button_a.is_pressed():
        display.show("0")
        print()
        print("Veuillez inserer le blanc,")
        print("puis appuyez sur A")
        print()
        sleep(1000)
        while not(button_a.is_pressed()):
            lecture = pin1.read_analog()
        zero = lecture
        print()
        print("Etalonnage OK")
        print()
    if button_b.is_pressed():
        display.show("M")
        print()
        print("Debut des mesures :")
        print("Appuyez sur B pour arreter")
        print()
        sleep(1000)
        temps_zero = running_time()
        while not(button_b.is_pressed()):
            lecture = pin1.read_analog()
            temps = (running_time() - temps_zero) / 1000
            A = log(zero / lecture) / log(10)
            print(temps, A)
            sleep(1000)
        while button_b.is_pressed():
            pass


