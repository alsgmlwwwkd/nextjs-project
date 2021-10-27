import hello2

# OOP: Object Oriented Programming
class Car:
    def __init__(self, velocity):
        self.position = 0
        self.velocity = velocity
    
    def drive(self, hours):
        self.position += self.velocity * hours

class Porsche(Car):
    def __init__(self):
        # super: parent class
        super().__init__(velocity=200)

    def drive_sports_mode(self, hours):
        self.drive(hours=hours * 2)

    @classmethod
    def print_name(cls):
        print('My name is Porsche')

if __name__ == '__main__':
    # instance
    my_porsche = Porsche()
    your_porsche = Porsche()

    # my_porsche.print_name()

    Porsche.print_name()
    Porsche().print_name()
