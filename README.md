At-Home Coding Challenge
========================

# Setup

Download PyCharm Community Edition for free on JetBrain's website. You may need to scroll down to find the community edition. 
PyCharm is your integrated development environment (IDE). Essentially, its Google Docs but for writing code.

https://www.jetbrains.com/pycharm/download

Also, install Git. The team uses Git to track and share code between computers. You'll need it to download some files for this tutorial.

https://git-scm.com/downloads

Most importantly, you need to download Python. Make sure to install **version 3.12**, as newer verisons of Python won't work on the robot. If you're on Windows, click **Windows installer (64-bit)** on the download page.

https://www.python.org/downloads/release/python-3128

# Downloading the Project

Great, you have everything set up! Now, let's download the project for this tutorial. You should be greeted by this screen when you open PyCharm.

![PyCharm startup window](https://frc3164.s3.us-east-1.amazonaws.com/pycharm_welcome.png)

Click **Get from VCS**, and enter the link below:

https://github.com/3164-Stealth-Tigers/Tank-Drive-Simulation.git

Create the project, then open the terminal. Either click the Terminal icon on the bottom left-hand side of your screen or press Alt+F12 on your keyboard. Run the command below to install RobotPy.

```
pip install robotpy
```

# Running the Simulator

A simulator lets you test robot code without a physical robot.

To run the simulator, plug an Xbox or PlayStation controller into your computer. Then, type the following command in the terminal (Alt+F12 to open):

```
robotpy sim
```

Click here for more information on using the simulator: https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/simulation-gui.html

---
**Controls** 🎮

| Button         | Binding            |
| -------------: | :----------------- |
| Left Joystick  | Left Wheels Power  |
| Right Joystick | Right Wheels Power |

---

# Challenges

Once you get a hang of using the simulator, you can try to modify and test the code. Right now, the autonomous drives the robot forward at full speed for two seconds, then stops. The challenges below suggest different ways to modify the autonomous routine. 

---
**Reference** 📋

Here are some useful resources to consult while working on the challenges:

[RobotPy API Reference](https://robotpy.readthedocs.io/projects/robotpy/en/stable/api.html)  
[RobotPy Examples](https://github.com/robotpy/examples)  
[Drivetrain Program Tutorial](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-4/creating-test-drivetrain-program-cpp-java-python.html)  

---

---
**Suggestion** ✅

Try to use the references or ask each other for help on the Discord if you're stuck.

---

## Challenge 1: Time

Modify the routine so that the robot drives forward for three seconds instead of two seconds.

<details>
    <summary><b>Tip 💡</b></summary> 

    Look at the if-statements.

</details>

## Challenge 2: Power

Modify the routine so that the robot drives forward for two seconds at __half__ power instead of at full power.

<details>
    <summary><b>Tip 💡</b></summary> 

    Look at the arguments to the arcadeDrive function.

</details>

## Challenge 3: Turning

Modify the routine so that the robot pivots to the left for two seconds instead of driving straight.

<details>
    <summary><b>Tip 💡</b></summary> 

    Look at the arguments to the arcadeDrive function.

</details>

## Challenge 4: Driving a Distance

Up until now, we've been driving for a certain amount of __time__. Modify the autonomous routine so that the robot drives forward at full power for five meters, then stops.

<details>
    <summary><b>Tip 💡</b></summary> 

    Encoders measure the rotation of a wheel. There is a left- and right-hand side wheel encoder in the program. They are set up to measure the distance, in meters, that the drive wheels move.  
    Check out the API reference for the Encoder class in you're stuck.

</details>

---
**Suggestion** ✅

You can hover over the robot in the simulator to check its position. The simulated SmartDashboard also shows sensor readings. 

---

## Challenge 5: Turning to an Angle

Let's do something similar with turning. Modify the routine so that the robot turns to the left 90 degrees, then stops.

<details>
    <summary><b>Tip 💡</b></summary> 

    An gyro sensor measures the angle that the robot is facing. Use a method from the gyro to read the robot's heading angle.

</details>

## Challenge 6: Putting it All Together

Now, you're going to sequence two different actions one after another. First, make the robot drive forward for three meters. Then, turn left 180 degrees. 

<details>
    <summary><b>Tip 💡</b></summary> 

    You may need to use an if-elif loop.

</details>

## Extra Challenge

At the end of Challenge 6, make the robot drive an additional two meters in the same direction while facing backwards. This is an extra challenge because it is much less straightforward than the other challenges.

<details>
    <summary><b>Tip 💡</b></summary> 

    Sensor readings are cumulative. Encoder readings can be reset to zero with a method on the Encoder class.

</details>

# Conclusion

By completing the first six challenges, you have gained a solid understanding of the basics of robot programming. I look forward to working with you all soon! Please, reach out on Discord with any questions.
