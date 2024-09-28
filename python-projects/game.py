import random

class Character:
    def __init__(self, name, health, level):
        self.__name = name
        self.__health = health
        self.__level = level

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_level(self):
        return self.__level

    def display_details(self):
        return f"Name: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}"

    def receive_attack(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def attack(self, target):
        damage = random.randint(self.get_level() * 1, self.get_level() * 5)
        target.receive_attack(damage)
        print(f"\n{self.get_name()} attacked {target.get_name()} and dealt {damage} damage!")

class Hero(Character):
    def __init__(self, name, health, level, ability):
        super().__init__(name, health, level)
        self.__ability = ability
    
    def special_attack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 10)
        target.receive_attack(damage)
        print(f"{self.get_name()} used the special ability {self.get_ability()} on {target.get_name()} and dealt {damage} damage!")
   
    def get_ability(self):
        return self.__ability

    def display_details(self):
        return f"{super().display_details()}\nAbility: {self.get_ability()}\n"

class Enemy(Character):
    def __init__(self, name, health, level, type_):
        super().__init__(name, health, level)
        self.__type = type_

    def get_type(self):
        return self.__type

    def display_details(self):
        return f"{super().display_details()}\nType: {self.get_type()}\n"


class Game:
    def __init__(self):
        self.hero = Hero(name="Hero", health=100, level=10, ability="Super Strength")
        self.enemy = Enemy(name="Zombie", health=100, level=10, type_="Undead")

    def start_battle(self):
        print("Starting the Battle!")
        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print("\nCharacter Details:")
            print(self.hero.display_details())
            print(self.enemy.display_details())
            input("Press Enter to attack! ")
            choice = None
            while choice not in [1, 2]:
                print("Entrou aqui")
                try:
                    choice = int(input("Choose (1 - Normal Attack, 2 - Special Attack): "))
                    if choice not in [1, 2]:
                        raise ValueError("Invalid choice!")
                except ValueError as e:
                    print(f"Error: {e}. Please enter 1 or 2.")
            if choice == 1:
                self.hero.attack(self.enemy)
            elif choice == 2:
                self.hero.special_attack(self.enemy)    
            
            if self.enemy.get_health() > 0:
                self.enemy.attack(self.hero)
            
            if self.hero.get_health() > 0:
                print("\nVICTORY")
            else:
                print("\nDEFEAT")

game = Game()
game.start_battle()
