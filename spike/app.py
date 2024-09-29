class App:
    """
    A class to represent the SPIKE Prime App, allowing interaction with the device (tablet or computer).

    Example:
        from spike import App

        # Initialize the App
        app = App()
    """

    def __init__(self):
        """
        Initialize the App.
        """
        pass

    def play_sound(self, name, volume=100):
        """
        Plays a sound from the device (tablet or computer).

        The program will not continue until the sound has finished playing.

        If no sound is found with the given name, nothing will happen.

        Args:
            name (str): The name of the sound to play.
            volume (int, optional): The volume at which the sound will be played. Defaults to 100%.

        Raises:
            TypeError: If `name` is not a string or `volume` is not an integer.
            RuntimeError: If the SPIKE App has been disconnected from the Hub.

        Sound Names:
            'Alert', 'Applause1', 'Applause2', 'Applause3', 'Baa', 'Bang1', 'Bang2',
            'BasketballBounce', 'BigBoing', 'Bird', 'Bite', 'BoatHorn1', 'BoatHorn2',
            'Bonk', 'BoomCloud', 'BoopBingBop', 'BowlingStrike', 'Burp1', 'Burp2',
            'Burp3', 'CarAccelerate1', 'CarAccelerating2', 'CarHorn', 'CarIdle',
            'CarReverse', 'CarSkid1', 'CarSkid2', 'CarVroom', 'CatAngry', 'CatHappy',
            'CatHiss', 'CatMeow1', 'CatMeow2', 'CatMeow3', 'CatPurring', 'CatWhining',
            'Chatter', 'Chirp', 'Clang', 'ClockTicking', 'ClownHonk1', 'ClownHonk2',
            'ClownHonk3', 'Coin', 'Collect', 'Connect', 'Crank', 'CrazyLaugh', 'Croak',
            'CrowdGasp', 'Crunch', 'Cuckoo', 'CymbalCrash', 'Disconnect', 'DogBark1',
            'DogBark2', 'DogBark3', 'DogWhining1', 'DogWhining2', 'Doorbell1', 'Doorbell2',
            'Doorbell3', 'DoorClosing', 'DoorCreek1', 'DoorCreek2', 'DoorHandle',
            'DoorKnock', 'DoorSlam1', 'DoorSlam2', 'DrumRoll', 'DunDunDunnn', 'EmotionalPiano',
            'Fart1', 'Fart2', 'Fart3', 'Footsteps', 'Gallop', 'GlassBreaking', 'Glug',
            'GoalCheer', 'Gong', 'Growl', 'Grunt', 'HammerHit', 'HeadShake', 'HighWhoosh',
            'Jump', 'JungleFrogs', 'Laser1', 'Laser2', 'Laser3', 'LaughingBaby1',
            'LaughingBaby2', 'LaughingBoy', 'LaughingCrowd1', 'LaughingCrowd2',
            'LaughingGirl', 'LaughingMale', 'Lose', 'LowBoing', 'LowSqueak', 'LowWhoosh',
            'MagicSpell', 'MaleJump1', 'MaleJump2', 'Moo', 'OceanWave', 'Oops',
            'OrchestraTuning', 'PartyBlower', 'Pew', 'PingPongHit', 'PlaneFlyingBy',
            'PlaneMotorRunning', 'PlaneStarting', 'Pluck', 'PoliceSiren1', 'PoliceSiren2',
            'PoliceSiren3', 'Punch', 'Rain', 'Ricochet', 'Rimshot', 'RingTone', 'Rip',
            'Robot1', 'Robot2', 'Robot3', 'RocketExplosionRumble', 'Rooster', 'ScramblingFeet',
            'Screech', 'Seagulls', 'ServiceAnnouncement', 'SewingMachine', 'ShipBell',
            'SirenWhistle', 'Skid', 'SlideWhistle1', 'SlideWhistle2', 'SneakerSqueak',
            'Snoring', 'Snort', 'SpaceAmbience', 'SpaceFlyby', 'SpaceNoise', 'Splash',
            'SportWhistle1', 'SportWhistle2', 'SqueakyToy', 'SquishPop', 'SuctionCup',
            'Tada', 'TelephoneRing2', 'TelephoneRing', 'Teleport2', 'Teleport3', 'Teleport',
            'TennisHit', 'ThunderStorm', 'TolietFlush', 'ToyHonk', 'ToyZing', 'Traffic',
            'TrainBreaks', 'TrainHorn1', 'TrainHorn2', 'TrainHorn3', 'TrainOnTracks',
            'TrainSignal1', 'TrainSignal2', 'TrainStart', 'TrainWhistle', 'Triumph',
            'TropicalBirds', 'Wand', 'WaterDrop', 'WhistleThump', 'Whiz1', 'Whiz2',
            'WindowBreaks', 'Win', 'Wobble', 'WoodTap', 'Zip'

        Example:
            from spike import App

            app = App()
            app.play_sound('Cat Meow 1')
        """
        pass

    def start_sound(self, name, volume=100):
        """
        Starts playing a sound from your device (tablet or computer).

        The program will not wait for the sound to finish playing before proceeding to the next command.

        If no sound with the given name is found, nothing will happen.

        Args:
            name (str): The name of the sound to play.
            volume (int, optional): The volume at which the sound will be played. Defaults to 100%.

        Raises:
            TypeError: If `name` is not a string or `volume` is not an integer.
            RuntimeError: If the SPIKE App has been disconnected from the Hub.

        Sound Names:
            (Same as in `play_sound` method.)

        Example:
            from spike import App

            app = App()
            app.start_sound('Cat Meow 1')
        """
        pass
