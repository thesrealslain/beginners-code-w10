from graphics import *


class Utils:
    @staticmethod
    def drawRectangle(win, tl, br, colour):
        rectangle = Rectangle(tl, br)
        rectangle.setFill(colour)
        rectangle.draw(win)
        return rectangle

    @staticmethod
    def drawCircle(win, center, radius, colour):
        circle = Circle(center, radius)
        circle.setFill(colour)
        circle.draw(win)
        return circle