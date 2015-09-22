class Crop:
    #constructor
    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

        def needs(self):
            return {'light_need':self._light_need, 'water_need':self._water_need}
        def report(self):
            return {'type':self._type, 'status':self._status, 'growth':self._growth}

        def set_growt(self,value):
            self._growth = value
        def get_growth(self):
            return(self.growth)
def main():
    new_crop = Crop(1,4,3)
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)
    new_crop2 = Crop(2,5,7)
    print(new_crop2._status)
    print(new_crop2._light_need)
    print(new_crop2._water_need)
    help(Crop)
    help(math)
    print(math)
    new_crop.set_growt(5)

if __name__ == "__main__":
    main()