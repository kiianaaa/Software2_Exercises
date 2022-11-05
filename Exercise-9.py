# 1 The basic info about the car.
import random
from random import random




class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


car = Car("ABC-123", 142)
print(f"The car's registration number is: {car.registration_number}, the maximum speed is: {car.maximum_speed}")
print(f"The current speed is: {car.current_speed} and the travelled distance is: {car.travelled_distance}")


# 2 extending the program by adding new values.


class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accerelate(self, speed_change):
        new_speed = car.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif self.maximum_speed > new_speed and new_speed > 0:
            self.current_speed += speed_change

    def brake(self):
        if self.current_speed > 200:
            self.current_speed -= 200   
        print("Emergency Brake!")    


car = Car("ABC-123", 142)
car.accerelate(+30)
print(f"The current speed is: {car.current_speed} km/h")
car.accerelate(+70)
print(f"The current speed is: {car.current_speed} km/h")
car.accerelate(+50)
print(f"The current speed is: {car.current_speed} km/h")
car.accerelate(200)
print(f"The current speed is: {car.current_speed} km/h")



# 3 adding the drive method.

class Car:

    def __init__(self, registration_number, maximum_speed, current_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = 0

    def accerelate(self, speed_change):
        new_speed = car.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif self.maximum_speed > new_speed and new_speed > 0:
            self.current_speed += speed_change

    def brake(self):
        if self.current_speed > 200:
            self.current_speed -= 200   
        print("Emergency Brake!") 

    def drive(self, hour):
        self.travelled_distance += self.current_speed * hour     


car = Car("ABC-123", 142, 60)    
car.drive(1.5)    
print(f"the new distance is: {car.travelled_distance} km.")




# 4 The car race


class Car:

    def __init__(self, registration_number, maximum_speed, current_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = 0

    def accerelate(self, speed_change):
        new_speed = car.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif self.maximum_speed > new_speed and new_speed > 0:
            self.current_speed += speed_change

    def brake(self):
        if self.current_speed > 200:
            self.current_speed -= 200   
        print("Emergency Brake!") 

    def drive(self, hour):
        self.travelled_distance += self.current_speed * hour  


ten_cars = []
for num in range(10):
    ten_cars.append(Car("ABC-" + str(num + 1), random.randint(100, 200)))    


travdis = 0
while travdis < 10000:
    for car in ten_cars:
        car.acceerelate(random.randint(-10, 15))
        car.drive(1)

for car in ten_cars:
    print(f"The registeratin number is: {Car.registration_number} the max speed: {Car.maximum_speed} and the travelled distance is: {Car.travelled_distance}")