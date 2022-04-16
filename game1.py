"""
Game of Clash
"""

import random
hero_description = dict()
main_deck = []
class Warrior:
    """
    Main warrior class
    """
    def __init__(self, name, damage, health):
        """
        Initializing the variables
        """
        self.name = name
        self.damage = damage
        self.health = health
    def set_description(self, words):
        """
        Setting the description for every hero
        """
        hero_description[self.name] = words
    def adding_to_deck(self):
        """
        Adding the player to a player
        """
        main_deck.append(self.name)
    def get_character(self, hero):
        """
        Getting character as an object
        """
        if hero in main_deck:
            return Warrior(hero, self.damage, self.health)
    def attack(self, vezha):
        """
        Attacking the enemy castke
        """
        health_of_castle = vezha.health
        amount_of_hits = random.randint(2, 4)
        hits = self.damage * amount_of_hits
        if health_of_castle - hits <= 0:
            return True


class Deck:
    """
    Deck class
    """
    def __init__(self):
        """
        Initializing amount of players in deck
        """
        self.amount_of_players = len(main_deck)
    def get_character(self, hero):
        """
        Getting character
        """
        if hero in main_deck:
            return Warrior(hero, random.randint(100, 200), random.randint(100, 1000))


class Poison(Warrior):
    """
    Poison
    """
    def __init__(self, name, damage, duration):
        """
        Initializiation
        """
        super().__init__(name, damage, health=0)
        self.duration = duration
    def set_description(self, words):
        """
        Setting the description for every hero
        """
        hero_description[self.name] = words
    def adding_to_deck(self):
        """
        Adding to the deck
        """
        main_deck.append(self.name)
    def get_character(self, hero):
        """
        Getting the character
        """
        if hero in main_deck:
            return Poison(hero, self.damage, self.health)
    def attack(self, vezha):
        """
        Attacking the enemy
        """
        health_of_castle = vezha.health
        amount_of_hits = random.randint(2-4)
        hits = self.damage * amount_of_hits
        if health_of_castle - hits <= 0:
            return True

class Slasher(Warrior):
    """
    Slasher class inherited from Warrior
    """
    def __init__(self, name, damage, amount_of_hits):
        """
        Initialization
        """
        super().__init__(name, damage, health=0)
        self.amount_of_hits = amount_of_hits
    def set_description(self, words):
        """
        Setting the description for every hero
        """
        hero_description[self.name] = words
    def adding_to_deck(self):
        """
        Adding to the deck
        """
        main_deck.append(self.name)
    def get_character(self, hero):
        """
        Getting the character
        """
        if hero in main_deck:
            return Slasher(hero, self.damage, self.health)
    def attack(self, vezha):
        """
        Attacking
        """
        health_of_castle = vezha.health
        amount_of_hits = random.randint(2-4)
        hits = self.damage * amount_of_hits
        if health_of_castle - hits <= 0:
            return True

class Castle:
    """
    Working with a castle
    """
    def __init__(self, general_enemy_hitter, health):
        """
        Initialization
        """
        self.general_enemy_hitter = general_enemy_hitter
        self.health = health
    def __str__(self):
        """
        String returning the explanation
        """
        return f"Enemy castle's general is {self.general_enemy_hitter} and " \
               f"he has {self.health} amount of health points"


class Elixir:
    """
    Elixir class
    """
    def __init__(self, amount):
        """
        Initialization
        """
        self.amount = amount
    def __str__(self):
        """
        String explanation
        """
        return f'Every player costs an elixir. We have {self.amount} drips of elixir for every attack.'
hog_rider = Slasher('Hog rider', 415, 3)
hog_rider.set_description('A massive warrior who rides the pig and hits good')
thunder = Poison('Thunder', 314, 0.5)
thunder.set_description('A massive storm gives an enemy castle a lot of pain')
valkyrie = Slasher('Valkyrie', 180, 5)
valkyrie.set_description('Walking queen who punches everything around her')
log = Poison('Legendary log', 95, 10)
log.set_description('Legendary log helps to beat all of the types of enemy castles')
hog_rider.adding_to_deck()
thunder.adding_to_deck()
valkyrie.adding_to_deck()
log.adding_to_deck()


win = False
print(str(Castle('king', 5000)))
castle = Castle('king', 5000)
while not win:
    print('\n')
    elixir = Elixir(10)
    elixir_for_attack = elixir.amount
    print(f'for the first attack we have {elixir_for_attack} elixir.Lets go')
    print('What type of fight would you like to perform?')
    type_of_fight = input()
    type_of_fights = ['silent', 'rush']
    if type_of_fight in type_of_fights:
        player = input('Pick a fighter')
        if player not in main_deck:
            print('You cant play with this player')
            win = True
        else:
            deck = Deck()
            attacking_warrior = deck.get_character(player)
            if attacking_warrior.attack(castle):
                print('Congrats you won')
                win = True
            else:
                print('Try a new player')






