from observable import Observable

class Sensor(Observable):
    def detect_movement(self):
        self.notify_observers()

class AlarmSystem(Observable):
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)
        sensor.add_observer(self)

    def notify(self, *args, **kwargs):
        self.notify_observers()

    def check_sensors(self):
        for sensor in self.sensors:
            sensor.detect_movement()

class PoliceDepartment:
    def update(self, *args, **kwargs):
        print("Police department notified!")

class InsuranceCompany:
    def update(self, *args, **kwargs):
        print("Insurance company notified!")

if __name__ == "__main__":
    sensor1 = Sensor()
    sensor2 = Sensor()
    alarm_system = AlarmSystem()
    alarm_system.add_sensor(sensor1)
    alarm_system.add_sensor(sensor2)
    police_department = PoliceDepartment()
    insurance_company = InsuranceCompany()
    alarm_system.add_observer(police_department)
    alarm_system.add_observer(insurance_company)
    sensor1.detect_movement()
    sensor2.detect_movement()