print("for revert testing")

import abc
import logging
import functools

class InsufficientBatteryError(Exception):
    def __init__(self, name, required, available):
        self.name = name
        self.required = required
        self.available = available
        super().__init__(self._build_message())

    def _build_message(self):
        return f"{self.name} has insufficient battery. Required: {self.required}%, Available: {self.available}%"

logging.basicConfig(level=logging.INFO)

def run_task_safely(robot, **kwargs):
    try:
        result = robot.perform_task(**kwargs)
    except InsufficientBatteryError as er:
        logging.error(f"Execution failed for {er.name}: {er}")
    else:
        print(f"Execution successful for {robot.name}: {result}")
    finally:
        print(f"Battery level after task: {robot.battery}%")

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished: {func.__name__}")
        return result
    return wrapper

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
        
    def use_battery(self, batCharge):
        if batCharge > self.battery:
            raise InsufficientBatteryError(self.name, batCharge, self.battery)
        self.battery -= batCharge

    @classmethod
    def from_config(cls, config):
        return cls(config['name'], config.get('battery', 100))

class CleaningRobot(Robot):
    def __str__(self):
        return f"{self.name}: With Modifications. From {self.manufacturer}. Description: Used for cleaning tasks."
    
    def __init__(self, name, battery=100, dustbin=50, suction=50):
        super().__init__(name, battery)
        self.dustbin = dustbin
        self.suction = suction

    def bot_upgrade(self, new_suction_power=100):
            self.suction = new_suction_power
            print(f"{self.name} has been upgraded from {self.suction} suction power.")

    @log_action
    def perform_task(self):
        self.use_battery(5)
        print(f"{self.name} is cleaning the floor and has a {self.dustbin}% full dustbin with suction power of {self.suction}.")
        return f"{self.name} Task Complete."



class DroneRobot(Robot):
    def __str__(self):
        return f"{self.name}: With Modifications. From {self.manufacturer}. Description: Used for aerial pictures."

    def __init__(self, name, battery=100, camera_quality="4K"):
        super().__init__(name, battery)
        self.camera_quality = camera_quality

    def bot_upgrade(self, new_camera_quality="8K"):
        self.camera_quality = new_camera_quality
        print(f"{self.name} has been upgraded to {self.camera_quality} camera.")

    @log_action
    def perform_task(self):
        self.use_battery(12)
        print(f"{self.name} is flying and taking aerial photos with {self.camera_quality} camera.")
        return f"{self.name} Task Complete."


def fleet_report(robots):
    print()
    print(f"Fleet Created: {Robot.botMany} Robots")
    print()
    for r in robots:
        print(str(r))
    print()

fleet = [CleaningRobot.from_config({"name": "Roomba"}), DroneRobot.from_config({"name": "HeliDrone"})]
fleet_report(fleet)

for r in fleet:
    run_task_safely(r)
    print()

print("Drone Upgrade:")
fleet[0].bot_upgrade()
fleet[1].bot_upgrade()
print()
