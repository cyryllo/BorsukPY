from microbit import *
import music


class JoyStick():
    def __init__(self):
        self.Up = pin10
        self.Left = pin11
        self.Right = pin9
        self.Down = pin8
        self.Select = pin7
        self.Mode = pin6
        self.JX = pin4
        self.JY = pin3
        self.JB = pin5
        self.BUZZ = pin0 # can control by music library import music | etc. music.play(music.NYAN)

