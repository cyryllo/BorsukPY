from microbit import *
from joystick import *
while True:
    if JoyStick.Down.read_digital() == 0: 
        print("A")
        sleep(50)
    elif JoyStick.Right.read_digital() == 0: 
        print("B")
        sleep(50)
    elif JoyStick.Left.read_digital() == 0: 
        print("C")
        sleep(50)
    elif JoyStick.Up.read_digital() == 0: 
        print("D")
        sleep(50)  
    elif JoyStick.JX.read_analog() <400: # wychylenie osi X w lewo
        print('Lewo')
        sleep(50)
    elif JoyStick.JX.read_analog() >700: # wychylenie osi X w prawo
        print('Prawo')
        sleep(50)
    elif JoyStick.JY.read_analog() >700: # wychylenie osi X w prawo
        print('Gora')
        sleep(50)
    elif JoyStick.JY.read_analog() <400: # wychylenie osi X w lewo
        print('Dol')
        sleep(50)
        
