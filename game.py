import random

description = []
linked = []
players_in_rooms = dict()
items_in_rooms = dict()
class Room:
    def __init__(self, room):
        self.room = room
    def set_description(self, words):
        description.append((self.room, words))
    def link_room(self, another_room, side):
        return linked.append((self.room, another_room.room, side))
    def set_character(self, character):
        players_in_rooms[self.room] = character.name
    def set_item(self, item):
        if item is None:
            del items_in_rooms[self.room]
            return True
        items_in_rooms[self.room] = item.item
    def get_details(self):
        for i in description:
            if i[0] == self.room:
                print(f'The Desription of {self.room} is {i[1]}')
                break
        print(('\n'))
        if self.room not in players_in_rooms.keys():
            print('There are no players in this room')
        else:
            print(players_in_rooms[self.room])
        print('\n')
        if self.room not in items_in_rooms.keys():
            print('There are no Items in this room')
        else:
            print(items_in_rooms[self.room])
        print('\n')
        for i in linked:
            if i[0] == self.room:
                print(f'If you go to {i[1]} you go to {i[2]}')
    def get_character(self):
        if self.room not in players_in_rooms.keys():
            return None
        else:
            name = players_in_rooms[self.room]
            descr = [i[1] for i in list_for_conversation_enemy if i[0] == name]
            return Enemy(name, descr)
    def get_item(self):
        if self.room not in items_in_rooms.keys():
            return None
        else:
            my_item = items_in_rooms[self.room]
            return Item(my_item)
    def move(self, side):
        for i in linked:
           if i[2] == side:
                if i[1] == self.room:
                   print('You are on your side')
                   new_room = i[1]
                else:
                    new_room = i[1]
                    break
        return Room(new_room)



class Character:
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics


list_for_conversation_enemy = []
list_for_weekness_enemy = []
list_of_wins = []
class Enemy(Character):
    def __init__(self, name, characteristics):
        super().__init__(name, characteristics)
    def set_conversation(self, dialogue):
        list_for_conversation_enemy.append((self.name, self.characteristics, dialogue))
    def set_weakness(self, weak_side):
        list_for_weekness_enemy.append((self.name, weak_side))
    def describe(self):
        for elem in list_for_conversation_enemy:
            if elem[0] == self.name:
                print(f'{elem[0]} is a {elem[1]}')
                break
    def talk(self):
        for row in list_for_conversation_enemy:
            if row[0] == self.name:
                print(row[2])
                break
    def fight(self, tool):
        can_he_fight = random.randint(1,2)
        tool = str(tool)
        if can_he_fight == 1:
            list_of_wins.append(True)
            return True
        else:
            return False
    def get_defeated(self):
        if len(list_of_wins) == 2:
            return 2
        else:
            return None


items = []
class Item:
    def __init__(self, item):
        self.item = item
    def set_description(self, descr):
        items.append((self.item, descr))
    def describe(self):
        for i in items:
            if i[0] == self.item:
                print(f'The description of the {i[0]} is {i[1]}')
                break
    def get_name(self):
        return self.item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")


kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)


cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

dead = False

current_room = dining_hall
backpack = ['book']
while dead == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")