import hello2

class Car:
    def __init__(self, velocity):
        self.position = 0
        self.velocity = velocity
    
    def drive(self, hours):
        self.position += self.velocity * hours

class Porsche(Car):
    def __init__(self):
        super().__init__(velocity=200)

    def drive_sports_mode(self, hours):
        self.drive(hours=hours * 2)

    def print_name(self):
        print('My name is Porsche')

if __name__ == '__main__':
    # my_porsche = Porsche()
    # your_porsche = Porsche()

    # my_porsche.print_name()
    genesis = Car(velocity=50)
    porsche = Car(velocity=200)

    porsche.drive(hours=2)

    print(porsche.position)