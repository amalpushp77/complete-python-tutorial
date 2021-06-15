class Enemy:
    def __init__(self):
        self.life = 100

    def shoot(self, attack):
        self.life = self.life - attack

    def status(self):
        print(self.life)
        if self.life == 0:
            print("Enemy is dead")


e1 = Enemy()
e2 = Enemy()
e3 = Enemy()

e2.status()
e2.shoot(80)
e2.status()
e2.shoot(20)
e2.status()

# e1.status()
# e2.status()
# e3.status()


#print(type(e1))