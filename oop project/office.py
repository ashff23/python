class Office:
    employee_counter = 0 

    def __init__(self, name):
        self.name = name
        self.employee_lst = []

    @classmethod
    def change_emp_num(cls, num):
        cls.employee_counter = num

    def get_all_employee(self):
        return self.employee_lst

    def get_employee(self, emp_id):
        for emp in self.employee_lst:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employee_lst.append(employee)
        Office.employee_counter += 1

    def fire(self, emp_id):
        fire_employees_lst = []
        for emp in self.employee_lst:
            if emp.id != emp_id:
                fire_employees_lst.append(emp)
        if len(fire_employees_lst) < len(self.employee_lst):
            Office.employee_counter -= 1
        self.employee_lst = fire_employees_lst

    @staticmethod
    def late(targethour, movehour, distance, velocity):
        if velocity==0:
            return True
        arrival_time = movehour + (distance / velocity)
        return arrival_time > targethour

    def check_late(self, id, movehour):
        emp = self.get_employee(id)
        if emp:
            late = Office.late(9, movehour, emp.distanceToWork, emp.car.velocity)
            if late:
                self.deduct(id, 10)
                print(f"Employee {id} was late.")
            else:
                self.reward(id, 10)
                print(f"Employee {id} was on time.")

    def deduct(self, id, amount):
        emp = self.get_employee(id)
        if emp:
            emp.salary -= amount

    def reward(self, id, amount):
        emp = self.get_employee(id)
        if emp:
            emp.salary += amount








