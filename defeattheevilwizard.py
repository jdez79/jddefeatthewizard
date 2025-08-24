import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)  # random damage
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)  # prevent negative health
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount}. Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses RAGE SLASH on {opponent.name} for {damage} damage!")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        damage = self.attack_power + random.randint(10, 20)
        opponent.health -= damage
        print(f"{self.name} casts FIREBALL on {opponent.name} for {damage} damage!")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)
        self.evade_next = False

    def special_ability(self, opponent):
        choice = input("Use (1) Quick Shot (double attack) or (2) Evade (dodge next attack): ")
        if choice == '1':
            damage = self.attack_power + random.randint(5, 15)
            opponent.health -= damage
            print(f"{self.name} uses QUICK SHOT and deals {damage} damage!")
        elif choice == '2':
            self.evade_next = True
            print(f"{self.name} prepares to EVADE the next attack!")
        else:
            print("Invalid choice. You lose your turn!")


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.shield_active = False

    def special_ability(self, opponent):
        choice = input("Use (1) Holy Strike (bonus damage) or (2) Divine Shield (block next attack): ")
        if choice == '1':
            damage = self.attack_power + random.randint(15, 25)
            opponent.health -= damage
            print(f"{self.name} uses HOLY STRIKE on {opponent.name} for {damage} damage!")
        elif choice == '2':
            self.shield_active = True
            print(f"{self.name} activates DIVINE SHIELD and will block the next attack!")
        else:
            print("Invalid choice. You lose your turn!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen = random.randint(5, 15)
        self.health += regen
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates {regen} health! Current health: {self.health}/{self.max_health}")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            continue
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()

            # Check for evade/shield effects
            if isinstance(player, Archer) and player.evade_next:
                print(f"{player.name} evades the wizard's attack!")
                player.evade_next = False
            elif isinstance(player, Paladin) and player.shield_active:
                print(f"{player.name}'s Divine Shield blocks the wizard's attack!")
                player.shield_active = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"\n🎉 The wizard {wizard.name} has been defeated by {player.name}! 🎉")


def main():
    print("⚔️ Welcome to the Fantasy Battle Game! ⚔️")
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()