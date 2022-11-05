# 1

class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page):
        self.author = author
        self.page = page
        super().__init__(name)

    def print_info(self):
        print(
            f"Name is: {self.name}, Author is: {self.author}, Page count is: {self.page}")


class Magazine(Publication):
    def __init__(self, name, chief):
        self.chief = chief
        super().__init__(name)

    def print_info(self):
        print(f"Name is: {self.name}, chief is: {self.chief})")


book = Book("Campartment No. 6", "Rosa Liksom", 192)
magazine = Magazine("Donald Duck", "Aki Hyppa")

book.print_info()
magazine.print_info()


# 2

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


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_cap):
        self.battery_cap = battery_cap
        super().__init__(reg_number, max_speed)


class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank):
        self.tank = tank
        super().__init__(reg_number, max_speed)


eleccar = ElectricCar("ABC-15", 180, 52.5)
gascar = GasolineCar("ACD-123", 165, 32.3)
