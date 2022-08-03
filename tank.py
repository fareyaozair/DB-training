class Tank:
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._health = 100
        self._shells = 20
        # No return keyword as implicitly called

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed += decrease
        return None

    def rotate_left (self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self, shells):
        self._shells