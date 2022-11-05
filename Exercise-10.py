# 1

import random


# 2 

class building:
    def __init__(self, bottom_floor, top_floor, elevaitor_list):
        self.elevaitor_list : []
        for i in range(elevaitor_list):
            self.elevaitor_list.append(Elevaitor(bottom_floor, top_floor))

    def run_elevaitor(self, elevaitor_number, floor):
        print(f"the elevaitor number {elevaitor_number} is running")
        self.elevaitor_list[elevaitor_number - 1].go_to_floor(floor)        



# 3

class building:
    def __init__(self, bottom_floor, top_floor, elevaitor_list):
        self.elevaitor_list : []
        for i in range(elevaitor_list):
            self.elevaitor_list.append(Elevaitor(bottom_floor, top_floor))

    def run_elevaitor(self, elevaitor_number, floor):
        print(f"the elevaitor number {elevaitor_number} is running")
        self.elevaitor_list[elevaitor_number - 1].go_to_floor(floor)

    def fire_alarm(self):
        for i in  self.elevaitor_list :
            i.go_to_floor(i.bottom_floor)





# 4




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
            print(f"{car.reg:6s} : ")        