from car import Car
from employee import Employee
from office import Office

samy_car = Car(name="Fiat 128", fuelrate=40, velocity=80)
samy = Employee(
    name="Samy",
    money=4000,
    healthrate=60,
    mood="happy",
    id=1,
    car=samy_car,
    salary=6000,
    distanceToWork=20,
    email="samy@iti.gov"
)


iti = Office("ITI Smart Village")

iti.hire(samy)

samy.drive(samy.distanceToWork)
samy.work(8)
iti.check_late(samy.id, 11)
samy.send_mail(
    to="manager@iti.org",
    subject="Work Update",
    body="I worked 8 hours and completed my tasks.",
)

print(f"Samy Final Status:")
print(f"Money: {samy.money}")
print(f"Mood: {samy.mood}")
print(f"Health: {samy.healthrate}")
print(f"Salary: {samy.salary}")
print(f"Car Name: {samy.car.name}")
print(f"Fuel Rate: {samy.car.fuelrate}")
print(f"Velocity: {samy.car.velocity}")

