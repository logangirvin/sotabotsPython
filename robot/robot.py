import wpilib
from GyroFilter import gyroFilter

lstick = wpilib.Joystick(1)

leftMotor = wpilib.Jaguar(1)
rightMotor = wpilib.Jaguar(2)

drive = wpilib.RobotDrive(leftMotor,rightMotor)

table = wpilib.NetworkTable.GetTable("SmartDashboard")

gyro = wpilib.Gyro(1)

gyroF = gyroFilter(100)

shootEncoder = wpilib.Encoder(1,2,false,k4X)

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
        table.PutNumber("T", 1)
        gyro.Reset()

    def TeleopPeriodic(self):
        self.GetWatchdog().Feed()
        CheckRestart()
        
        # Motor control
        drive.ArcadeDrive(lstick)

        #Print gyro values
        PrintGyro()
        
    def PrintGyro(self):
        gyroF.update(gyro.GetAngle())
        print("Gyroscope calculated average: ", gyroF.getAverage())
        print("Raw value: ", gyro.GetAngle())
        

def run():
    robot = MyRobot()
    robot.StartCompetition()
