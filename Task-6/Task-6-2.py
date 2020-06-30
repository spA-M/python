class Road:

    massa_1kv_metra = 0.125

    def __init__(self, _length, _width,):
        self._length = _length
        self._width = _width

    def massa(self):
        return self._length * self._width * self.massa_1kv_metra


a = Road(20, 5000)
print(round(a.massa()))