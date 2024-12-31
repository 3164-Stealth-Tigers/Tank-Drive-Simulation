#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
import math

import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):
    """Main robot class"""

    def robotInit(self):
        """Robot-wide initialization code should go here"""

        wheel_diameter = 0.1524
        encoder_resolution = 4096

        self.stick = wpilib.XboxController(0)

        self.lf_motor = wpilib.Spark(1)
        self.lr_motor = wpilib.Spark(2)
        self.rf_motor = wpilib.Spark(3)
        self.rr_motor = wpilib.Spark(4)

        l_motor = wpilib.MotorControllerGroup(self.lf_motor, self.lr_motor)
        r_motor = wpilib.MotorControllerGroup(self.rf_motor, self.rr_motor)

        r_motor.setInverted(True)

        self.drive = wpilib.drive.DifferentialDrive(l_motor, r_motor)

        # Position gets automatically updated as robot moves
        self.gyro = wpilib.AnalogGyro(1)

        # Encoders report the velocity and position (driven distance) of each wheel
        self.l_encoder = wpilib.Encoder(0, 1)
        self.r_encoder = wpilib.Encoder(2, 3)

        # Set the distance per pulse for the drive encoders to the distance traveled
        # for one rotation of the wheel divided by the encoder resolution
        self.l_encoder.setDistancePerPulse(math.pi * wheel_diameter / encoder_resolution)
        self.r_encoder.setDistancePerPulse(math.pi * wheel_diameter / encoder_resolution)

    def autonomousInit(self):
        """Called when autonomous mode is enabled"""

        self.timer = wpilib.Timer()
        self.timer.start()

    def autonomousPeriodic(self):
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(1.0, 0.0)
        else:
            self.drive.arcadeDrive(0, 0)

    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""
        self.drive.tankDrive(-self.stick.getLeftY(), -self.stick.getRightY())

    def robotPeriodic(self):
        """Called whenever the robot is enabled"""

        # Publish data about the robot to the dashboard
        wpilib.SmartDashboard.putNumber("Left Wheel Distance", self.l_encoder.getDistance())
        wpilib.SmartDashboard.putNumber("Right Wheel Distance", self.r_encoder.getDistance())
        wpilib.SmartDashboard.putNumber("Heading Angle", self.gyro.getAngle())
