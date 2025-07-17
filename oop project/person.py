class Person:
    def __init__(self,name,money,mood,healthrate): 
        self.name=name
        self.money=money
        self.mood=mood
        self.healthrate=healthrate

    def buy(self, items):
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
                        
    def sleep(self,hours):    
        if hours==7:
            self.mood= 'happy'
        elif hours > 7:
            self.mood='lazy'
        else:
             self.mood='tired'

    def eat(self,meals):    
        if meals==3:
            self.healthrate=100
        elif meals==2:
            self.healthrate=75
        elif meals==1:
            self.healthrate=50








