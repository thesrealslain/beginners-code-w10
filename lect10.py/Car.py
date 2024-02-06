from graphics import *
from Utils import *

class Car:
    def __init__(self, win, topLeftX, topLeftY, widthCarTop, heightCarTop, diff, carColour):
        self.carParts = []
        self.win = win
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.widthCarTop = widthCarTop
        self.heightCarTop = heightCarTop
        self.diff = diff
        self.carColour = carColour

    def buildCarTop(self):
        topLeftPoint = Point(self.topLeftX, self.topLeftY)
        bottomRightPoint = Point(self.topLeftX + self.widthCarTop, self.topLeftY + self.heightCarTop)
        carTop = Utils.drawRectangle(self.win, topLeftPoint, bottomRightPoint, self.carColour)
        self.carParts.append(carTop)

    def buildCarBody(self):
        topLeftPoint = Point(self.topLeftX - self.diff, self.topLeftY + self.heightCarTop)
        bottomRightPoint = Point(self.topLeftX + self.widthCarTop + self.diff,
                                 self.topLeftY + self.heightCarTop + self.heightCarTop)
        carBody = Utils.drawRectangle(self.win, topLeftPoint, bottomRightPoint, self.carColour)
        self.carParts.append(carBody)

    def buildLeftWheel(self):
        center = Point(self.topLeftX, self.topLeftY + self.heightCarTop + self.heightCarTop)
        radius = self.heightCarTop / 2
        blackCircle = Utils.drawCircle(self.win, center, radius, "black")
        whiteRadius = radius - 10
        whiteCircle = Utils.drawCircle(self.win, center, whiteRadius, "white")
        self.carParts.extend([blackCircle, whiteCircle])

    def buildRightWheel(self):
        center = Point(self.topLeftX + self.widthCarTop, self.topLeftY + self.heightCarTop + self.heightCarTop)
        radius = self.heightCarTop / 2
        blackCircle = Utils.drawCircle(self.win, center, radius, "black")
        whiteRadius = radius - 10
        whiteCircle = Utils.drawCircle(self.win, center, whiteRadius, "white")
        self.carParts.extend([blackCircle, whiteCircle])

    def buildCar(self):
        self.buildCarTop()
        self.buildCarBody()
        self.buildLeftWheel()
        self.buildRightWheel()

    def move(self, dx, dy):
        for carPart in self.carParts:
            carPart.move(dx, dy)