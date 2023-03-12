from microbit import *
Dir = [
    'f',
    'b',
]


class MotorDriver():
    def __init__(self):
        self.PWMA = pin8
        self.AIN1 = pin13
        self.AIN2 = pin12
        self.PWMB = pin16
        self.BIN1 = pin14
        self.BIN2 = pin15
        self.S0 = pin0
        self.S1 = pin1
        self.S2 = pin2
        self.S0.set_analog_period(20)
        self.S1.set_analog_period(20)
        self.S2.set_analog_period(20)

    def MotorRun(self, motor, index, speed):
        if(speed > 16):
            return
        speed = speed * 64 - 1

        if(motor == 0):
            self.PWMA.write_analog(speed)
            if(index == Dir[0]):
                self.AIN1.write_digital(1)
                self.AIN2.write_digital(0)
            else:
                self.AIN1.write_digital(0)
                self.AIN2.write_digital(1)
        else:
            self.PWMB.write_analog(speed)
            if(index == Dir[0]):
                self.BIN1.write_digital(1)
                self.BIN2.write_digital(0)
            else:
                self.BIN1.write_digital(0)
                self.BIN2.write_digital(1)

    def MotorStop(self, motor):
        if (motor == 0):
            self.PWMA.write_analog(0)
        else:
            self.PWMB.write_analog(0)

    def ServosTurnZero(self, servo):
        if(servo == 0):
            self.S0.write_analog(25)
        elif(servo == 1):
            self.S1.write_analog(25)
        else:
            self.S2.write_analog(25)

    def ServosTurnFull(self, servo):
        if(servo == 0):
            self.S0.write_analog(128)
        elif(servo == 1):
            self.S1.write_analog(128)
        else:
            self.S2.write_analog(128)

    def ServosStop(self, servo):
        if(servo == 0):
            self.S0.write_analog(0)
        elif(servo == 1):
            self.S1.write_analog(0)
        else:
            self.S2.write_analog(0)

    def ServoTurn(self, servo, angle):
        if(angle > 180):
            return
        temp = angle / 2 + 25
        if(servo == 0):
            self.S0.write_analog(temp)
        elif(servo == 1):
            self.S1.write_analog(temp)
        else:
            self.S2.write_analog(temp)



