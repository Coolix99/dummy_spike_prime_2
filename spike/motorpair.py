class MotorPair:
    """
    Represents a pair of motors connected to the SPIKE Prime Hub, allowing you to control two motors simultaneously.

    The `MotorPair` class is typically used to control a driving base with two motors, such as a robot with left and right wheels.

    Example:
        from spike import MotorPair

        # Initialize the MotorPair with motors connected to ports 'B' and 'C'
        motor_pair = MotorPair('B', 'C')

        # Move forward for 10 cm
        motor_pair.move(10, 'cm')
    """

    def __init__(self, port_left, port_right):
        """
        Initializes the MotorPair with the specified ports for the left and right motors.

        Args:
            port_left (str): The port for the left motor ('A'-'F').
            port_right (str): The port for the right motor ('A'-'F').

        Raises:
            ValueError: If the ports are not valid or the motors cannot be paired.
            RuntimeError: If one or both of the motors are disconnected.
        """
        self.port_left = port_left
        self.port_right = port_right

    # Actions

    def move(self, amount, unit='cm', steering=0, speed=None):
        """
        Starts the two motors simultaneously to move a driving base.

        The program will not continue until the specified amount is reached.

        Args:
            amount (float): The quantity to move in relation to the specified unit of measurement.
            unit (str, optional): The units of measurement of the amount parameter.
                Possible values: 'cm', 'in', 'rotations', 'degrees', 'seconds'. Defaults to 'cm'.
            steering (int, optional): The direction and amount to steer the driving base (-100 to 100).
                0 makes the driving base go straight. Negative numbers make it turn left. Positive numbers make it turn right.
                Defaults to 0.
            speed (int, optional): The motor speed (-100 to 100%). Defaults to the default speed set by `set_default_speed()`.

        Raises:
            TypeError: If `amount` is not a number, or `steering` or `speed` is not an integer, or `unit` is not a string.
            ValueError: If `unit` is not one of the allowed values.
            RuntimeError: If one or both of the motors have been disconnected or the motors could not be paired.

        Example:
            motor_pair.move(20, 'cm', steering=50, speed=60)
        """
        pass

    def start(self, steering=0, speed=None):
        """
        Starts the two motors simultaneously to move a driving base without waiting.

        The program flow is not interrupted. This is useful for non-blocking movement.

        Args:
            steering (int, optional): The direction and amount to steer the driving base (-100 to 100).
                0 makes the driving base go straight. Negative numbers make it turn left. Positive numbers make it turn right.
                Defaults to 0.
            speed (int, optional): The motor speed (-100 to 100%). Defaults to the default speed set by `set_default_speed()`.

        Raises:
            TypeError: If `steering` or `speed` is not an integer.
            RuntimeError: If one or both of the motors have been disconnected or the motors could not be paired.

        Example:
            motor_pair.start(steering=-50, speed=75)
        """
        pass

    def stop(self):
        """
        Stops the two motors simultaneously, which will stop the driving base.

        The motors will either actively hold their current position or coast freely depending on the option selected by `set_stop_action()`.

        Raises:
            RuntimeError: If one or both of the motors have been disconnected or the motors could not be paired.

        Example:
            motor_pair.stop()
        """
        pass

    def move_tank(self, amount, unit='cm', left_speed=None, right_speed=None):
        """
        Moves the driving base using differential (tank) steering.

        The speed of each motor can be controlled independently for differential (tank) drive driving bases.

        Args:
            amount (float): The quantity to move in relation to the specified unit of measurement.
            unit (str, optional): The units of measurement of the amount parameter.
                Possible values: 'cm', 'in', 'rotations', 'degrees', 'seconds'. Defaults to 'cm'.
            left_speed (int, optional): The speed of the left motor (-100 to 100%). Defaults to the default speed.
            right_speed (int, optional): The speed of the right motor (-100 to 100%). Defaults to the default speed.

        Raises:
            TypeError: If `amount`, `left_speed`, or `right_speed` is not a number or `unit` is not a string.
            ValueError: If `unit` is not one of the allowed values.
            RuntimeError: If one or both of the motors have been disconnected or the motors could not be paired.

        Example:
            motor_pair.move_tank(10, 'cm', left_speed=25, right_speed=75)
        """
        pass

    def start_tank(self, left_speed, right_speed):
        """
        Starts moving the driving base using differential (tank) steering without waiting.

        Args:
            left_speed (int): The speed of the left motor (-100 to 100%).
            right_speed (int): The speed of the right motor (-100 to 100%).

        Raises:
            TypeError: If `left_speed` or `right_speed` is not an integer.
            RuntimeError: If one or both of the motors have been disconnected or the motors could not be paired.

        Example:
            motor_pair.start_tank(50, -50)
        """
        pass

    def start_at_power(self, power, steering=0):
        """
        Starts moving the driving base without speed control.

        The motors can be driven without speed control, useful when using your own control algorithm (e.g., a proportional line follower).

        Args:
            power (int): The amount of power to send to the motors (-100 to 100%).
            steering (int, optional): The steering direction (-100 to 100). Defaults to 0.

        Raises:
            TypeError: If `power` or `steering` is not an integer.
            RuntimeError: If one or both of the motors have been disconnected or the motors could not be paired.

        Example:
            motor_pair.start_at_power(50, steering=25)
        """
        pass

    def start_tank_at_power(self, left_power, right_power):
        """
        Starts moving the driving base using differential (tank) steering without speed control.

        Args:
            left_power (int): The power of the left motor (-100 to 100%).
            right_power (int): The power of the right motor (-100 to 100%).

        Raises:
            TypeError: If `left_power` or `right_power` is not an integer.
            RuntimeError: If one or both of the motors have been disconnected or the motors could not be paired.

        Example:
            motor_pair.start_tank_at_power(50, -50)
        """
        pass

    # Measurements

    def get_default_speed(self):
        """
        Retrieves the default motor speed.

        Returns:
            int: The default motor speed (-100 to 100%).

        Example:
            default_speed = motor_pair.get_default_speed()
            print(f"Default speed: {default_speed}%")
        """
        return 100

    # Settings

    def set_motor_rotation(self, amount, unit='cm'):
        """
        Sets the ratio of one motor rotation to the distance traveled.

        If there are no gears used between the motors and the wheels of the driving base, then `amount` is the circumference of one wheel.

        Args:
            amount (float): The distance the driving base moves when both motors move one rotation each.
            unit (str, optional): The units of measurement of the `amount` parameter.
                Possible values: 'cm', 'in'. Defaults to 'cm'.

        Raises:
            TypeError: If `amount` is not a number or `unit` is not a string.
            ValueError: If `unit` is not one of the allowed values.

        Example:
            motor_pair.set_motor_rotation(17.6 * math.pi, 'cm')
        """
        pass

    def set_default_speed(self, speed):
        """
        Sets the default motor speed.

        This speed will be used when you omit the speed argument in one of the other methods.

        Args:
            speed (int): The default motor speed (-100 to 100%).

        Raises:
            TypeError: If `speed` is not an integer.

        Example:
            motor_pair.set_default_speed(50)
        """
        pass

    def set_stop_action(self, action):
        """
        Sets the motor action that will be used when the driving base stops.

        Args:
            action (str): The desired action when the motors stop.
                Possible values: 'coast', 'brake', 'hold'.

        Raises:
            TypeError: If `action` is not a string.
            ValueError: If `action` is not one of the allowed values.

        Example:
            motor_pair.set_stop_action('hold')
        """
        pass
