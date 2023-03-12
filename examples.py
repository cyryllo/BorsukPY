from borsuk import *

Borsuk = MotorDriver()
# control 2 motor
Borsuk.MotorRun(0, 'f', 16)
# 
sleep(1000)
Borsuk.MotorStop(0)
Borsuk.MotorRun(1, 'b', 16)

sleep(1000)
Borsuk.MotorStop(1)

sleep(1000)
Borsuk.MotorRun(0, 'f', 16)
Borsuk.MotorRun(1, 'f', 16)

sleep(3000)

Borsuk.MotorStop(0)
Borsuk.MotorStop(1)

# control 3 servo
Motor.ServosTurnZero(0)
Motor.ServosTurnFull(1)
Motor.ServosTurnFull(2)
Motor.ServoTurn(0, 50)
Motor.ServoTurn(1, 150)
Motor.ServosStop(2)