import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10

    def attack(self, monster):
        damage = random.randint(5, self.attack_power)
        monster.health -= damage
        print(f"{self.name} attacks {monster.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, character):
        damage = random.randint(5, self.attack_power)
        character.health -= damage
        print(f"{self.name} attacks {character.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.character = None
        self.monsters = [
            Monster("Goblin", 30, 5),
            Monster("Orc", 50, 10),
            Monster("Dragon", 100, 15)
        ]

    def start(self):
        print("Welcome to the Text-Based RPG!")
        name = input("Enter your character's name: ")
        self.character = Character(name)
        print(f"Character {self.character.name} created with {self.character.health} health.")

        while self.character.is_alive():
            self.play_turn()

        print("Game Over! You have been defeated.")

    def play_turn(self):
        print("\nYou encounter a monster!")
        monster = random.choice(self.monsters)
        print(f"A wild {monster.name} appears with {monster.health} health!")

        while monster.is_alive() and self.character.is_alive():
            action = input("Do you want to (A)ttack or (R)un? ").strip().lower()
            if action == 'a':
                self.character.attack(monster)
                if monster.is_alive():
                    monster.attack(self.character)
                    print(f"{self.character.name} has {self.character.health} health left.")
            elif action == 'r':
                print(f"{self.character.name} runs away!")
                break
            else:
                print("Invalid action. Please choose 'A' to attack or 'R' to run.")

        if not monster.is_alive():
            print(f"You defeated the {monster.name}!")

if __name__ == "__main__":
    game = Game()
    game.start()