import abc

class Robot(abc.ABC):

    manufacturer = "StalRotonics"
    botMany = 0

    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery
        Robot.botMany += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        value = max(0, min(100, value))
        self._battery = value

    def __str__(self):
        return f"{self.name} ({self.battery}% Battery)"

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', battery={self.battery}%)"

    @abc.abstractmethod
    def perform_task(self):
        pass
        


class CleaningRobot(Robot):
    def __str__(self):
        return f"{self.name}: With Modifications. From {self.manufacturer}. Description: Used for cleaning tasks"
    
    def __init__(self, name, battery=100, dustbin=50):
        super().__init__(name, battery)
        self.dustbin = dustbin

    def perform_task(self):
        print(f"{self.name} is cleaning the floor and has a {self.dustbin}% full dustbin.")
        self.battery -= 5



class DroneRobot(Robot):
    def __str__(self):
        return f"{self.name}: With Modifications. From {self.manufacturer}. Description: Used for aerial pictures"

    def __init__(self, name, battery=100, camera_quality="4K 1080p"):
        super().__init__(name, battery)
        self.camera_quality = camera_quality

    def perform_task(self):
        print(f"{self.name} is flying and taking aerial photos with {self.camera_quality} camera.")
        self.battery -= 12


def fleet_report(robots):
    for r in robots:
        print(str(r))

fleet = [CleaningRobot("Roomba"), DroneRobot("HeliDrone")]
fleet_report(fleet)