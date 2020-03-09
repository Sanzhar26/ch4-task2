class Airplane:

     def __init__(self,mark,model,year,max_speed):
         self.mark = mark
         self.model = model
         self.year = year
         self.max_speed = max_speed
         self.odometer = 0
         self.is_flying = False

     def take_off(self):
        self.is_flying = True
        message_take = f"{self.mark} {self.model} was take off."
        return message_take

     def fly(self, km):
        self.odometer += km
        message_fly = f"{self.mark} {self.model} is flying now {self.odometer}km during the flying {self.max_speed} km/h."
        return message_fly

     def land(self):
            self.is_flying = False
            message_land = f"{self.mark} {self.model} landed, the odometer shows {self.odometer}km."
            return message_land
start = Airplane("Boeing","TU-154","2020",2000)
print(start.take_off())
print(start.fly(400))
print(start.fly(500))
print(start.land())