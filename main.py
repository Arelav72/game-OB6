import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        current_attacker = random.choice([self.player, self.computer])
        while self.player.is_alive() and self.computer.is_alive():
            if current_attacker == self.player:
                self.player.attack(self.computer)
                current_attacker = self.computer
            else:
                self.computer.attack(self.player)
                current_attacker = self.player

            print(f"{self.player.name}: {self.player.health} HP, {self.computer.name}: {self.computer.health} HP\n")

        winner = self.player if self.player.is_alive() else self.computer
        print(f"Игра окончена. Победил {winner.name}!")




if __name__ == "__main__":
    player_name = input("Введите имя героя: ")
    game = Game(player_name)
    game.start()