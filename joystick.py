from microbit import *
import music

display.off() # disable screen led

class JoyStick():
    Up = pin10
    Left = pin11
    Right = pin9
    Down = pin8
    Select = pin7
    Mode = pin6
    JX = pin4
    JY = pin3
    JB = pin5
    BUZZ = pin0 # can control by music library import music | etc. music.play(music.NYAN)

