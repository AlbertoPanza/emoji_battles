import random
import json
import time

class Fighter:
    def __init__(self, name: str, emoji: str, hp: int, attack_power: int, defense_power: int):
        self.name = name
        self.emoji = emoji
        self.total_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, opponent):
        attacker = f"{self.emoji} {self.name.capitalize()}"
        defender = f"{opponent.emoji} {opponent.name.capitalize()}"
        defense = random.randint(opponent.defense_power - 1, opponent.defense_power + 2)

        if random.random() < 0.8:
            damage = random.randint(self.attack_power - 2, self.attack_power + 2)
            print(f"\n{attacker} attacks with a {damage}!")
            time.sleep(delay_1)
        else:
            damage = random.randint(self.attack_power - 2, self.attack_power + 2) * 2
            print(f"\nCRITICAL HIT! {attacker} attacks with a {damage}!")
            time.sleep(delay_2)

        result = max(0, damage - defense)
        print(f"\n{defender} defends with a {defense}!")
        time.sleep(delay_1)

        if result > 0:
            opponent.hp -= result
            if opponent.hp < 0:
                opponent.hp = 0
            print(f"\n{defender} takes {result} of damage! Current Hp: {opponent.hp}")
            time.sleep(delay_1)
        else:
            print(f"\nNo damage taken by {defender}. Current Hp: {opponent.hp}")
            time.sleep(delay_2)

def load_fighters_from_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def choose_fighter():
    data = load_fighters_from_json("fighters.json")
    fighter_objects = [Fighter(**i) for i in data]

    while True:
        for idx, fighter in enumerate(fighter_objects):
            print(f"{idx + 1}. {fighter.emoji} {fighter.name.capitalize()}")
        player_choice = input("Please enter the number of your hero: ")
        time.sleep(delay_1)

        if player_choice.isdigit():
            choice = int(player_choice)
            if 1 <= choice <= len(fighter_objects):
                return fighter_objects[choice - 1], fighter_objects
            else:
                print("The number is out of range.")
                time.sleep(delay_1)
        else:
            print("Please enter a number.")
            time.sleep(delay_2)

def choose_opponent(fighter_list):
    return random.choice(fighter_list)

# Delay settings
delay_1 = 1.5
delay_2 = 2.0
delay_3 = 3.0
delay_4 = 4.0
delay_5 = 5.0

# Game setup
fighter1, all_fighters = choose_fighter()
fighter2 = choose_opponent(all_fighters)

if fighter2 == fighter1:
    fighter2 = Fighter(
        name=f"Evil {fighter1.name}",
        emoji=fighter1.emoji,
        hp=fighter1.total_hp,
        attack_power=fighter1.attack_power,
        defense_power=fighter1.defense_power
    )

fighters = [fighter1, fighter2]
print(f"\nYou are: {fighter1.emoji} {fighter1.name.capitalize()}")
print(f"Your opponent is: {fighter2.emoji} {fighter2.name.capitalize()}")
print("\n⚔️  Let the battle begin! ⚔️\n")
time.sleep(delay_5)

# Battle loop
while fighter1.hp > 0 and fighter2.hp > 0:
    random.shuffle(fighters)
    first_attacker = fighters[0]
    second_attacker = fighters[1]

    first_attacker.attack(second_attacker)
    time.sleep(delay_4)

    if second_attacker.hp <= 0:
        print(f"\n{second_attacker.emoji} {second_attacker.name.capitalize()} has died!")
        break
    else:
        second_attacker.attack(first_attacker)
        time.sleep(delay_4)

        if first_attacker.hp <= 0:
            print(f"\n{first_attacker.emoji} {first_attacker.name.capitalize()} has died!")
            break
