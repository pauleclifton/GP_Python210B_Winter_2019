class DrivingRules:
    def __init__(self, minimum_age, drivers_age):
        #self.minimum_age = minimum_age
        self._minimum_age = minimum_age
        #self.drivers_age = drivers_age
        self._drivers_age = drivers_age

    @property
    def minimum_age(self):
        return self._minimum_age

    @minimum_age.setter
    def minimum_age(self, age):
        self._minimum_age = age

    @property
    def drivers_age(self):
        return self._drivers_age

    def can_drive(self):
        if self.drivers_age >= self.minimum_age:
            return True
        return False
        