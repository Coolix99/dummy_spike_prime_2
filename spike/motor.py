class Motor:
    """
    Represents a single motor connected to the SPIKE Prime Hub.

    The `Motor` class allows you to control a motor connected to one of the hub's ports.
    You can run the motor for a specified duration, rotations, or degrees, control its speed,
    and read its position and speed.

    Example:
        from spike import Motor

        # Initialize the Motor
        motor = Motor('A')

        # Run the motor for 2 seconds at 50% speed
        motor.run_for_seconds(2, 50)
    """

    def __init__(self, port):
        """
        Initialize the Motor.

        Args:
            port (str): The port to which the motor is connected ('A'-'F').
        """
        self.port = port

    # Actions

    def run_to_position(self, degrees, direction='shortest path', speed=None):
        """
        Runs the motor to an absolute position.

        The sign of the speed will be ignored (absolute value) and the motor will always travel
        in the direction specified by the `direction` parameter. If speed is greater than 100,
        it will be limited to 100.

        Args:
            degrees (int): The target position (0 to 359 degrees).
            direction (str, optional): The direction to use to reach the target position.
                Options are 'shortest path', 'clockwise', 'counterclockwise'. Defaults to 'shortest path'.
            speed (int, optional): The motor's speed (0 to 100%). Defaults to the default speed.

        Raises:
            TypeError: If `degrees` or `speed` is not an integer or `direction` is not a string.
            ValueError: If `direction` is not one of the allowed values or `degrees` is not within 0-359.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.run_to_position(0)
        """
        pass

    def run_to_degrees_counted(self, degrees, speed=None):
        """
        Runs the motor until degrees counted is equal to the value specified by the `degrees` parameter.

        The sign of the speed will be ignored and the motor will always travel in the direction required
        to reach `degrees`. If speed is greater than 100, it will be limited to 100.

        Args:
            degrees (int): The target degrees counted.
            speed (int, optional): The desired speed (positive values only, 0 to 100%).
                Defaults to the default speed.

        Raises:
            TypeError: If `degrees` or `speed` is not an integer.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.run_to_degrees_counted(360)
        """
        pass

    def run_for_degrees(self, degrees, speed=None):
        """
        Runs the motor for a given number of degrees.

        Args:
            degrees (int): The number of degrees the motor should run.
            speed (int, optional): The motor's speed (-100 to 100%). Defaults to the default speed.

        Raises:
            TypeError: If `degrees` or `speed` is not an integer.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.run_for_degrees(90)
        """
        pass

    def run_for_rotations(self, rotations, speed=None):
        """
        Runs the motor for a specified number of rotations.

        Args:
            rotations (float): The number of rotations the motor should run.
            speed (int, optional): The motor's speed (-100 to 100%). Defaults to the default speed.

        Raises:
            TypeError: If `rotations` is not a number or `speed` is not an integer.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.run_for_rotations(1)
        """
        pass

    def run_for_seconds(self, seconds, speed=None):
        """
        Runs the motor for a specified number of seconds.

        Args:
            seconds (float): The number of seconds for which the motor should run.
            speed (int, optional): The motor's speed (-100 to 100%). Defaults to the default speed.

        Raises:
            TypeError: If `seconds` is not a number or `speed` is not an integer.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.run_for_seconds(2, 50)
        """
        pass

    def start(self, speed=None):
        """
        Starts running the motor at a specified speed.

        The motor will keep moving at this speed until you give it another motor command,
        or when your program ends.

        Args:
            speed (int, optional): The motor's speed (-100 to 100%). Defaults to the default speed.

        Raises:
            TypeError: If `speed` is not an integer.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.start(50)
        """
        pass

    def stop(self):
        """
        Stops the motor.

        What the motor does after it stops depends on the action set in `set_stop_action()`.
        The default value is 'coast'.

        Raises:
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.stop()
        """
        pass

    def start_at_power(self, power):
        """
        Starts rotating the motor at a specified power level.

        The motor will keep moving at this power level until you give it another motor command,
        or when your program ends.

        Args:
            power (int): Power of the motor (-100 to 100%).

        Raises:
            TypeError: If `power` is not an integer.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.start_at_power(75)
        """
        pass

    # Measurements

    def get_speed(self):
        """
        Retrieves the speed of the motor.

        Returns:
            int: The current speed of the motor (-100% to 100%).

        Raises:
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            current_speed = motor.get_speed()
            print(f"Current speed: {current_speed}")
        """
        return 0

    def get_position(self):
        """
        Retrieves the position of the motor.

        This is the clockwise angle between the moving marker and the zero-point marker on the motor.

        Returns:
            int: The position of the motor (0 to 359 degrees).

        Raises:
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            position = motor.get_position()
            print(f"Motor position: {position} degrees")
        """
        return 0

    def get_degrees_counted(self):
        """
        Retrieves the degrees counted by the motor.

        Returns:
            int: The number of degrees counted.

        Raises:
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            degrees_counted = motor.get_degrees_counted()
            print(f"Degrees counted: {degrees_counted}")
        """
        return 0

    def get_default_speed(self):
        """
        Retrieves the current default motor speed.

        Returns:
            int: The default motor speed (-100% to 100%).

        Example:
            default_speed = motor.get_default_speed()
            print(f"Default speed: {default_speed}")
        """
        return 100

    # Events

    def was_interrupted(self):
        """
        Tests whether the motor was interrupted.

        Returns:
            bool: True if the motor was interrupted since the last time `was_interrupted()` was called,
            otherwise False.

        Raises:
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            if motor.was_interrupted():
                print("Motor was interrupted!")
        """
        return False

    def was_stalled(self):
        """
        Tests whether the motor was stalled.

        Returns:
            bool: True if the motor was stalled since the last time `was_stalled()` was called,
            otherwise False.

        Raises:
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            if motor.was_stalled():
                print("Motor was stalled!")
        """
        return False

    # Settings

    def set_degrees_counted(self, degrees_counted):
        """
        Sets the number of degrees counted to a desired value.

        Args:
            degrees_counted (int): The value to which the number of degrees counted should be set.

        Raises:
            TypeError: If `degrees_counted` is not an integer.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.set_degrees_counted(0)
        """
        pass

    def set_default_speed(self, default_speed):
        """
        Sets the default motor speed.

        This speed will be used when you omit the speed argument in one of the other methods,
        such as `run_for_degrees()`.

        Setting the default speed does not affect any motors that are currently running.

        Args:
            default_speed (int): The default speed value (-100% to 100%).

        Raises:
            TypeError: If `default_speed` is not an integer.

        Example:
            motor.set_default_speed(50)
        """
        pass

    def set_stop_action(self, action):
        """
        Sets the default behavior when a motor stops.

        Args:
            action (str): The desired motor behavior when the motor stops.
                Options are 'coast', 'brake', 'hold'.

        Raises:
            TypeError: If `action` is not a string.
            ValueError: If `action` is not one of the allowed values.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.set_stop_action('hold')
        """
        pass

    def set_stall_detection(self, stop_when_stalled):
        """
        Turns stall detection on or off.

        Stall detection senses when a motor has been blocked and can't move.
        If stall detection has been enabled and a motor is blocked, the motor will be powered off
        after two seconds and the current motor command will be interrupted.
        If stall detection has been disabled, the motor will keep trying to run and programs will
        "get stuck" until the motor is no longer blocked.

        Stall detection is enabled by default.

        Args:
            stop_when_stalled (bool): Choose True to enable stall detection or False to disable it.

        Raises:
            TypeError: If `stop_when_stalled` is not a boolean.
            RuntimeError: If the motor has been disconnected from the port.

        Example:
            motor.set_stall_detection(False)
        """
        pass
