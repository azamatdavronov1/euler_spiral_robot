from controller import Robot

# Create a Robot instance
robot = Robot()

# Get the simulation time step
timestep = int(robot.getBasicTimeStep())

# Get motors (assuming your robot has 2 motors: left and right)
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set the motors to velocity control mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set initial speed
left_motor.setVelocity(3.0)
right_motor.setVelocity(3.0)

# Main control loop
while robot.step(timestep) != -1:
    # Here you could add logic, for now it just drives forward
    pass

