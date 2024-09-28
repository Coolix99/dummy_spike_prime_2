# primehub.py

class PrimeHub:
    """
    A class to represent the SPIKE Prime Hub.

    The PrimeHub class provides access to the hub's features such as the left and right buttons,
    speaker, light matrix, status light, and motion sensor.

    Example:
        from spike import PrimeHub

        # Initialize the Hub
        hub = PrimeHub()
    """

    # Constants for Ports
    PORT_A = 'A'
    PORT_B = 'B'
    PORT_C = 'C'
    PORT_D = 'D'
    PORT_E = 'E'
    PORT_F = 'F'

    def __init__(self):
        """
        Initialize the PrimeHub and its components.
        """
        self.left_button = Button('left')
        self.right_button = Button('right')
        self.speaker = Speaker()
        self.light_matrix = LightMatrix()
        self.status_light = StatusLight()
        self.motion_sensor = MotionSensor()

class Button:
    """
    Represents one of the programmable buttons on the SPIKE Prime Hub.

    Example:
        from spike import PrimeHub

        hub = PrimeHub()

        # Wait until the left button is pressed
        hub.left_button.wait_until_pressed()
    """

    def __init__(self, side):
        """
        Initialize the Button.

        Args:
            side (str): The side of the button ('left' or 'right').
        """
        self.side = side

    # Events

    def wait_until_pressed(self):
        """
        Waits until the button is pressed.
        """
        pass

    def wait_until_released(self):
        """
        Waits until the button is released.
        """
        pass

    def was_pressed(self):
        """
        Tests to see whether the button has been pressed since the last time this method was called.

        Once this method returns True, the button must be released and pressed again before this method will return True again.

        Returns:
            bool: True if the button was pressed, otherwise False.
        """
        return False

    # Measurements

    def is_pressed(self):
        """
        Tests whether the button is currently pressed.

        Returns:
            bool: True if the button is pressed, otherwise False.
        """
        return False

class Speaker:
    """
    Represents the speaker inside the Hub.

    Example:
        from spike import PrimeHub

        hub = PrimeHub()

        hub.speaker.beep()
    """

    # Actions

    def beep(self, note=60, seconds=0.2):
        """
        Plays a beep on the Hub.

        Your program will not continue until the beep has finished playing.

        Args:
            note (int, optional): The MIDI note number (60 is middle C). Defaults to 60.
            seconds (float, optional): The duration of the beep in seconds. Defaults to 0.2.

        Raises:
            TypeError: If `note` is not an integer or `seconds` is not a number.
            ValueError: If `note` is not within the allowed range of 44-123.
        """
        pass

    def start_beep(self, note=60):
        """
        Starts playing a beep.

        The beep will play indefinitely until `stop()` or another beep method is called.

        Args:
            note (int, optional): The MIDI note number (60 is middle C). Defaults to 60.

        Raises:
            TypeError: If `note` is not an integer.
            ValueError: If `note` is not within the allowed range of 44-123.
        """
        pass

    def stop(self):
        """
        Stops any sound that is playing.
        """
        pass

    # Measurements

    def get_volume(self):
        """
        Retrieves the current volume of the speaker.

        Returns:
            int: The current volume (0 to 100%).
        """
        return 100

    # Settings

    def set_volume(self, volume):
        """
        Sets the speaker volume.

        Args:
            volume (int): The new volume percentage (0 to 100%).

        Raises:
            TypeError: If `volume` is not an integer.
        """
        pass

class LightMatrix:
    """
    Represents the Light Matrix on the Hub.

    Example:
        from spike import PrimeHub

        hub = PrimeHub()

        hub.light_matrix.show_image('HAPPY')
    """

    # Actions

    def show_image(self, image, brightness=100):
        """
        Shows an image on the Light Matrix.

        Args:
            image (str): Name of the image.
            brightness (int, optional): Brightness of the image (0 to 100%). Defaults to 100.

        Raises:
            TypeError: If `image` is not a string or `brightness` is not an integer.
            ValueError: If `image` is not one of the allowed values.
        """
        pass

    def set_pixel(self, x, y, brightness=100):
        """
        Sets the brightness of one pixel on the Light Matrix.

        Args:
            x (int): Pixel position from the left (0 to 4).
            y (int): Pixel position from the top (0 to 4).
            brightness (int, optional): Brightness of the pixel (0 to 100%). Defaults to 100.

        Raises:
            TypeError: If `x`, `y`, or `brightness` is not an integer.
            ValueError: If `x` or `y` is not within the allowed range of 0-4.
        """
        pass

    def write(self, text):
        """
        Writes text on the Light Matrix, scrolling from right to left.

        Args:
            text (str): Text to write.

        Raises:
            TypeError: If `text` is not a string.
        """
        pass

    def off(self):
        """
        Turns off all the pixels on the Light Matrix.
        """
        pass

class StatusLight:
    """
    Represents the Brick Status Light on the Hub's Center Button.

    Example:
        from spike import PrimeHub

        hub = PrimeHub()

        hub.status_light.on('blue')
    """

    # Actions

    def on(self, color='white'):
        """
        Sets the color of the Brick Status Light.

        Args:
            color (str, optional): The color to set. Defaults to 'white'.

        Allowed Colors:
            'azure', 'black', 'blue', 'cyan', 'green', 'orange', 'pink', 'red', 'violet', 'yellow', 'white'

        Raises:
            TypeError: If `color` is not a string.
            ValueError: If `color` is not one of the allowed values.
        """
        pass

    def off(self):
        """
        Turns off the Brick Status Light.
        """
        pass

class MotionSensor:
    """
    Represents the Motion Sensor inside the Hub.

    Example:
        from spike import PrimeHub

        hub = PrimeHub()

        yaw = hub.motion_sensor.get_yaw_angle()
    """

    # Events

    def was_gesture(self, gesture):
        """
        Tests whether a gesture has occurred since the last time this method was called.

        Args:
            gesture (str): The name of the gesture.

        Possible Values:
            'shaken', 'tapped', 'doubletapped', 'falling', None

        Returns:
            bool: True if the gesture has occurred, otherwise False.

        Raises:
            TypeError: If `gesture` is not a string.
            ValueError: If `gesture` is not one of the allowed values.
        """
        return False

    def wait_for_new_gesture(self):
        """
        Waits until a new gesture happens.

        Returns:
            str: The new gesture.

        Possible Values:
            'shaken', 'tapped', 'doubletapped', 'falling'
        """
        return 'tapped'

    def wait_for_new_orientation(self):
        """
        Waits until the orientation of the Hub changes.

        The first time this method is called, it will immediately return the current value. After that, calling this method will block the program until the Hub's orientation has changed since the previous time this method was called.

        Returns:
            str: The Hub's new orientation.

        Possible Values:
            'front', 'back', 'up', 'down', 'leftside', 'rightside'
        """
        return 'front'

    # Measurements

    def get_orientation(self):
        """
        Retrieves the current orientation of the Hub.

        Returns:
            str: The Hub's current orientation.

        Possible Values:
            'front', 'back', 'up', 'down', 'leftside', 'rightside'
        """
        return 'front'

    def get_gesture(self):
        """
        Retrieves the most recently-detected gesture.

        Returns:
            str: The gesture.

        Possible Values:
            'shaken', 'tapped', 'doubletapped', 'falling'
        """
        return 'tapped'

    def get_roll_angle(self):
        """
        Retrieves the roll angle of the Hub.

        'Roll' is the rotation around the front-back (longitudinal) axis.

        Returns:
            int: The roll angle in degrees (-180 to 180).
        """
        return 0

    def get_pitch_angle(self):
        """
        Retrieves the pitch angle of the Hub.

        'Pitch' is the rotation around the left-right (transverse) axis.

        Returns:
            int: The pitch angle in degrees (-180 to 180).
        """
        return 0

    def get_yaw_angle(self):
        """
        Retrieves the yaw angle of the Hub.

        'Yaw' is the rotation around the vertical axis.

        Returns:
            int: The yaw angle in degrees (-180 to 180).
        """
        return 0

    # Settings

    def reset_yaw_angle(self):
        """
        Sets the yaw angle to 0.
        """
        pass
