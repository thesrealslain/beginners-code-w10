from time import sleep
from Car import *
from Utils import *


def main():
    win = GraphWin('', 800, 500)
    # Initial values to set up car
    topLeftX = 100
    topLeftY = 130
    widthCarTop = 150
    heightCarTop = 70
    diff = 30

    car = Car(win, topLeftX, topLeftY, widthCarTop, heightCarTop, diff, 'blue')
    car.buildCar()

    win.getMouse()
    for _ in range(1000):
        sleep(.01)
        car.move(1, 0)

    win.getMouse()

main()