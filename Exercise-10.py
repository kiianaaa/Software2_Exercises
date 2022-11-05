import random

# 1


class Elevaitor:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            print(f"The elevaitor is moving up from {self.current_floor} to {self.current_floor + 1}")
            self.current_floor += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            print(f"This elevaitor is moving down from {self.current_floor} to {self.current_floor - 1}")
            self.current_floor -= 1                
            return True
        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            for num in range(floor - self.current_floor):
                if not self.floor_up():
                    break
        elif floor < self.current_floor:
            for num in range(self.current_floor - floor):
                if not self.floor_down():
                    break            
        else:
            print("You ara already at this floor.")            


elevaitor = Elevaitor(1, 9)
elevaitor.floor_up(1)

# 2

class Elevaitor:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            print(f"The elevaitor is moving up from {self.current_floor} to {self.current_floor + 1}")
            self.current_floor += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            print(f"This elevaitor is moving down from {self.current_floor} to {self.current_floor - 1}")
            self.current_floor -= 1                
            return True
        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            for num in range(floor - self.current_floor):
                if not self.floor_up():
                    break
        elif floor < self.current_floor:
            for num in range(self.current_floor - floor):
                if not self.floor_down():
                    break            
        else:
            print("You ara already at this floor.")  



class Building:
    def __init__(self, bottom_floor, top_floor, elevaitor_list):
        self.elevaitor_list: []
        for i in range(elevaitor_list):
            self.elevaitor_list.append(Elevaitor(bottom_floor, top_floor))

    def run_elevaitor(self, elevaitor_number, floor):
        print(f"the elevaitor number {elevaitor_number} is running")
        self.elevaitor_list[elevaitor_number - 1].go_to_floor(floor)


print("Elevaitor is in the biulding: ")
building = Building(1, 7, 3)
building.run_elevaitor(1, 4)
building.run_elevaitor(2, 4)
building.run_elevaitor(3, 1)


# 3

class building:
    def __init__(self, bottom_floor, top_floor, elevaitor_list):
        self.elevaitor_list: []
        for i in range(elevaitor_list):
            self.elevaitor_list.append(Elevaitor(bottom_floor, top_floor))

    def run_elevaitor(self, elevaitor_number, floor):
        print(f"the elevaitor number {elevaitor_number} is running")
        self.elevaitor_list[elevaitor_number - 1].go_to_floor(floor)

    def fire_alarm(self):
        for i in self.elevaitor_list:
            i.go_to_floor(i.bottom_floor)


# 4

class Car:

    def __init__(self, registration_number, maximum_speed, current_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = 0

    def accerelate(self, speed_change):
        new_speed = Car.current_speed + speed_change
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

class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list

    def hour_pass(self):
        for car in self.cars_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1.)

    def print_status(self):
        print(self.name + ":")
        for car in self.cars_list:
            print(f"{car.reg:6s} : {car.travelled_distance}km")

    def racw_finished(self):
        for car in self.cars_list:
            if car.travelled_distance >= self.distance:
                return True 
        return False


car_list = []
for i in range(1, 11):
    new_car = Car("ABC-" + str(i), random.randint(100,200))
    car_list.append(new_car)        

race = Race("Grand Demolition Derby", 8000, car_list)

n = 0
while not race.race_finished():
    race.hour_passes()