import wpilib

lstick = wpilib.Joystick(1)

Motor = wpilib.Jaguar(1)
motorValue = 0

def CheckRestart():
    if lstick.GetRawButton(10):
        raise RuntimeError("Restart")
        print("CheckRestart")

class MyRobot(wpilib.IterativeRobot):
    def DisabledContinuous(self):
        wpilib.Wait(0.01)
    def AutonomousContinuous(self):
        wpilib.Wait(0.01)
    def TeleopContinuous(self):
        wpilib.Wait(0.01)

    def DisabledPeriodic(self):
        CheckRestart()

    def AutonomousInit(self):
        self.GetWatchdog().SetEnabled(False)

    def AutonomousPeriodic(self):
        CheckRestart()

    def TeleopInit(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)
        
    def TeleopPeriodic(self):
        self.GetWatchdog().Feed()
        CheckRestart()
        
        if lstick.GetRawButton(0):              #Trigger sets shooter to 100%
                motorValue = 1
        if lstick.GetRawButton(1):              #Button 2 sets to 75%
                motorValue = 0.75
        else:                                   #Joystick y axis controls otherwise
                if lstick.GetY() > 0.05 or lstick.GetY() < -0.05:
                        motorValue = lstick.GetY()
                else:
                        motorValue = 0

        Motor.set(motorValue)

        
  

def run():
    robot = MyRobot()
    robot.StartCompetition()
