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
        
    def batConsumption(self, batCharge):
        if batCharge > self.battery:
            raise InsufficientBatteryError(self.name, batCharge, self.battery)
        self.battery -= batCharge

class CleaningRobot(Robot):
    def __str__(self):
        return f"{self.name}: With Modifications. From {self.manufacturer}. Description: Used for cleaning tasks"
    
    def __init__(self, name, battery=100, dustbin=50):
        super().__init__(name, battery)
        self.dustbin = dustbin

    def perform_task(self):
        self.batConsumption(5)
        print(f"{self.name} is cleaning the floor and has a {self.dustbin}% full dustbin.")




class DroneRobot(Robot):
    def __str__(self):
        return f"{self.name}: With Modifications. From {self.manufacturer}. Description: Used for aerial pictures"

    def __init__(self, name, battery=100, camera_quality="4K 1080p"):
        super().__init__(name, battery)
        self.camera_quality = camera_quality

    def perform_task(self):
        self.batConsumption(10)
        print(f"{self.name} is flying and taking aerial photos with {self.camera_quality} camera.")
        


def fleet_report(robots):
    print()
    print(f"Fleet Created: {Robot.botMany} Robots")
    for r in robots:
        print(str(r))
    print()

fleet = [CleaningRobot("Roomba"), DroneRobot("HeliDrone")]
fleet_report(fleet)

class InsufficientBatteryError(Exception):
    def __init__(self, name, required, available):
        self.name = name
        self.required = required
        self.available = available
        super().__init__(self._build_message())

    def _build_message(self):
        return f"{self.name} has insufficient battery. Required: {self.required}%, Available: {self.available}%"
