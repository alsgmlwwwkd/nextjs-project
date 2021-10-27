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

    def print_name(self):
        print('My name is Porsche')

if __name__ == '__main__':
    # instance
    my_porsche = Porsche()
    your_porsche = Porsche()

    my_porsche.drive_sports_mode(hours=2)
    
    print(my_porsche.position)
    # my_porsche.print_name()
