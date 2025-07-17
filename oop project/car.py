class Car :  
    def __init__(self,name, fuelrate, velocity):
        self.name=name
        self.set_fuel_rate(fuelrate)
        self. set_velocity(velocity)

    def set_fuel_rate(self, value):
        if value >= 100:
            self.fuelrate = 100
        elif value <= 0:
            self.fuelrate = 0
        else:
            self.fuelrate = value
    def get_fuel_rate(self):
        return self.fuelrate

    def set_velocity(self, value):
        if value >= 200:
            self.velocity = 200
        elif value <= 0:
            self.velocity = 0
        else:
            self.velocity = value

    def get_velocity(self):
        return self.velocity

    def run(self,velocity,distance):
        self.velocity = velocity
        needs = distance / 10
        if self.fuelrate >= needs:
            self.fuelrate -= needs
            return self.stop(0)
        else:
            traveled_distance = self.fuelrate * 10
            rest_dis = distance - traveled_distance
            self.fuelrate = 0
            return self.stop(rest_dis)
            
    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance == 0:
            return True
        else:
                return False





