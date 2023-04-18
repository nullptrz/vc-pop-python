class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def normalAttack(self):
        print("Normal Attack")
    

class SuperCharacter(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.canFly = True
        self.canHeal = True
    
    def performAerialAttack(self):
        print("Attacking from Air")

    def normalAttack(self):
        print("Performing Normal Super Attack")

c = Character(100, 20)
s = SuperCharacter(200, 50)

c.normalAttack()
s.normalAttack()

