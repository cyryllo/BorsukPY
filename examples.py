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
Borsuk.ServosTurnZero(0)
Borsuk.ServosTurnFull(1)
Borsuk.ServosTurnFull(2)
Borsuk.ServoTurn(0, 50)
Borsuk.ServoTurn(1, 150)
Borsuk.ServosStop(2)
