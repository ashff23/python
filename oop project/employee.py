from person import Person
class Employee(Person):
    def __init__(self, name, money, mood, healthrate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthrate)  
        self.car = car
        self.id=id
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
         if hours == 8:
            self.mood='happy'
         elif hours > 8:
            self.mood='tired'
         elif hours < 8 :             
            self.mood='lazy' 
            
    def drive(self, velocity):
        self.car.run(velocity, self.distanceToWork)

    def refuel(self, gasamount):
        self.car.fuelrate += gasamount
        if self.car.fuelrate >100:
           self.car.fuelrate = 100

    def send_mail(self, to, subject, body):
        print(f"From: {self.email}")
        print(f"To: {to}")
        print(f"Subject: {subject}")
        print(f"{body}")
       

 