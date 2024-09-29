# colorsensor.py

class ColorSensor:
    """
    Represents a Color Sensor connected to the SPIKE Prime Hub.

    The Color Sensor can detect colors, measure light intensity, and control its built-in lights.

    Example:
        from spike import ColorSensor

        # Initialize the Color Sensor on port 'A'
        color_sensor = ColorSensor('A')

        # Get the detected color
        color = color_sensor.get_color()
        print(f"Detected color: {color}")
    """

    def __init__(self, port):
        """
        Initializes the Color Sensor.

        Args:
            port (str): The port to which the sensor is connected ('A'-'F').

        Raises:
            ValueError: If the port is not a valid port ('A'-'F').
        """
        self.port = port

    # Measurements

    def get_color(self):
        """
        Detects the color of a surface.

        Returns:
            str or None: The name of the detected color, or None if no color is detected.

        Possible Values:
            'black', 'violet', 'blue', 'cyan', 'green', 'yellow', 'red', 'white', None

        Example:
            color = color_sensor.get_color()
            if color == 'red':
                print("Red color detected!")
        """
        return None

    def get_ambient_light(self):
        """
        Measures the ambient light intensity.

        Returns:
            int: The ambient light intensity as a percentage (0 to 100%).

        Example:
            ambient_light = color_sensor.get_ambient_light()
            print(f"Ambient light: {ambient_light}%")
        """
        return 0

    def get_reflected_light(self):
        """
        Measures the intensity of light reflected from a surface.

        Returns:
            int: The reflected light intensity as a percentage (0 to 100%).

        Example:
            reflected_light = color_sensor.get_reflected_light()
            print(f"Reflected light: {reflected_light}%")
        """
        return 0

    def get_rgb_intensity(self):
        """
        Measures the intensity of red, green, and blue colors.

        Returns:
            tuple of int: A tuple containing the red, green, blue, and overall intensity values (0 to 1024).

        Example:
            red, green, blue, overall = color_sensor.get_rgb_intensity()
            print(f"Red: {red}, Green: {green}, Blue: {blue}, Overall: {overall}")
        """
        return (0, 0, 0, 0)

    def get_red(self):
        """
        Measures the intensity of red light.

        Returns:
            int: The red light intensity (0 to 1024).

        Example:
            red_intensity = color_sensor.get_red()
            print(f"Red intensity: {red_intensity}")
        """
        return 0

    def get_green(self):
        """
        Measures the intensity of green light.

        Returns:
            int: The green light intensity (0 to 1024).

        Example:
            green_intensity = color_sensor.get_green()
            print(f"Green intensity: {green_intensity}")
        """
        return 0

    def get_blue(self):
        """
        Measures the intensity of blue light.

        Returns:
            int: The blue light intensity (0 to 1024).

        Example:
            blue_intensity = color_sensor.get_blue()
            print(f"Blue intensity: {blue_intensity}")
        """
        return 0

    # Events

    def wait_until_color(self, color):
        """
        Waits until the specified color is detected.

        Args:
            color (str or None): The name of the color to wait for.

        Possible Values:
            'black', 'violet', 'blue', 'cyan', 'green', 'yellow', 'red', 'white', None

        Raises:
            ValueError: If the color is not one of the allowed values.

        Example:
            color_sensor.wait_until_color('blue')
            print("Blue color detected!")
        """
        pass

    def wait_for_new_color(self):
        """
        Waits until a new color is detected.

        The method returns immediately the first time it is called.
        After that, it waits until a different color is detected compared to the last time.

        Returns:
            str or None: The name of the new color detected.

        Possible Values:
            'black', 'violet', 'blue', 'cyan', 'green', 'yellow', 'red', 'white', None

        Example:
            while True:
                new_color = color_sensor.wait_for_new_color()
                print(f"New color detected: {new_color}")
        """
        return None

    # Actions

    def light_up_all(self, brightness=100):
        """
        Lights up all the lights on the Color Sensor with the specified brightness.

        Args:
            brightness (int, optional): The brightness level (0 to 100%). Defaults to 100.

        Raises:
            ValueError: If the brightness is not between 0 and 100.

        Example:
            # Turn on the lights at full brightness
            color_sensor.light_up_all()

            # Turn off the lights
            color_sensor.light_up_all(0)
        """
        pass

    def light_up(self, light_1=100, light_2=100, light_3=100):
        """
        Sets the brightness of the individual lights on the Color Sensor.

        Args:
            light_1 (int, optional): Brightness of light 1 (0 to 100%). Defaults to 100.
            light_2 (int, optional): Brightness of light 2 (0 to 100%). Defaults to 100.
            light_3 (int, optional): Brightness of light 3 (0 to 100%). Defaults to 100.

        Raises:
            ValueError: If any brightness value is not between 0 and 100.

        Example:
            # Turn on only the first light at full brightness
            color_sensor.light_up(100, 0, 0)
        """
        pass
