def main():

    class Player:
        def __init__(self, first_name, health, inventory):
            self.first_name = first_name
            self.health = health
            self.inventory = inventory

        def show_health(self):
            print(line)
            print(str(player.health) + ' health')
            print(line)

        def show_inv(self):
            print(line)
            print(player.inventory)
            print(line)
    player = Player('Zack', 5, '')
    player.inventory = []

    # list to put items into. this is used to check if a player has already done an action.
    # Such as picking fruit from a cactus and not reprinting the cactus with fruit.
    items_grabbed = []

    # just some short cuts so I don't have to keep plugging in strings for items
    cactus_fruit = 'Cactus Fruit'
    key = 'Key'
    line = '__________________________________'
    # The choices list I plan to use later on to have some type of weight to actions.
    # like if you punch the bird you'll be shamed for it, or if you didn't go to
    # certain room the game will make tease you for being blind.
    # choices = []
    # options = []
    idk = "\nI don't know that\n"

    # Ascii art

    cactus_with_fruit = '''           
          \  :  /
           ' _ '
       -= ( (_) ) =-
           .   .
          /  :  \,
     @.-.    '
      |.|
    /)|`|(\@
   (.(|'|)`)
~~~~`\`'./'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |.|           ~~
 ~~  @|`|                            ~~
     ,|'|.      (_)          ~~
  ~~  "'"        \/"\.
           ~~     ^~^ '''
    cactus_without_fruit = '''           
          \  :  /
           ' _ '
       -= ( (_) ) =-
           .   .
          /  :  \,
      .-.    '
      |.|
    /)|`|(\.
   (.(|'|)`)
~~~~`\`'./'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |.|           ~~
 ~~   |`|                            ~~
     ,|'|.      (_)          ~~
  ~~  "'"        \/"\.
           ~~     ^~^ '''

    # Dictionary used for the help function mainly. Just shortcuts to find health
    # or inventory.

    player_commands = {
        'health': player.health,
        'inv': player.inventory,
        'inventory': player.inventory
    }
    # Function used to take in the players choice and give them the option to check
    # health and inventory instead of repasting code. Not happy with the global command.

    def enter():
        global choice
        choice = input('>')
        if choice.upper() == 'HELP':
            help()

    # A function meant for the player to be able to check there inventory or health
    # at anytime.

    def help():
        check = input("What do you wish to check? \n[Health/Inventory]")
        if check.upper() == 'HEALTH':
            Player.show_health(player)
        elif check.upper() == 'INV' or 'INVENTORY':
            Player.show_inv(player)
        else:
            mistype()
            help()

    def mistype():
        print(line + idk + line)

    def lb():
        print(line)

    # Staring point. Can travel to Cactus and Vulture from here

    def desert():
        print("You are in a desert. \nWhere do you want to go?")
        print("[Cactus/Vulture]")
        enter()
        if choice.upper() == 'HELP':
            desert()
        elif choice.upper() == 'CACTUS':
            cactus()
        elif choice.upper() == 'VULTURE':
            vulture()
        else:
            mistype()
            desert()

    # Stage with a cactus. Player takes the fruit and uses it for a later objective.
    def cactus():
        print('You walk up to the cactus')
        # Checks for fruit int inventory. If the player had already taken the fruit it will print
        # out a cactus with no fruit.
        if 'Cactus Fruit' not in items_grabbed:
            print(cactus_with_fruit)
            print("The cactus is tall with fruit blooming! Do you pick up the fruit?")
            print('[Yes/No]')
            enter()
            if choice.upper() == 'YES':
                print("You pick up the fruit!")
                player.inventory.append(cactus_fruit)
                items_grabbed.append(cactus_fruit)
            elif choice.upper() == 'NO':
                print("You leave the fruit alone")

        # Prints cactus with no fruit
        elif cactus_fruit in items_grabbed:
            print(cactus_without_fruit)
            print("The cactus has no more fruit on it")
        print("Where do you want to go? \n[Desert/Vulture]")
        enter()
        if choice.upper() == 'DESERT':
            desert()
        elif choice.upper() == 'VULTURE':
            vulture()
        else:
            mistype()
            cactus()

    # Vulture location. Ideally you want to give the vulture the cactus fruit to
    # not take damage and not hurt the bird. This is where you can obtained the key from.
    def vulture():
        if key not in items_grabbed:
            get_key()
        Player.show_health(player)
        print('Where do you wish to go now?')
        print('[House/Desert]')
        enter()
        if choice.upper() == 'HOUSE':
            house()
        elif choice.upper() == 'DESERT':
            desert()
        else:
            mistype()
            vulture()

    def get_key():
        print('you walk up to a large vulture standing over bones \n'
              'the bird has a key around its neck. What do you wish to do?')
        # Checking for cactus fruit in inventory
        if cactus_fruit in player.inventory:
            print('[Fight/Give fruit]')
            enter()
        elif cactus_fruit not in player.inventory:
            print('[Fight]')
            enter()
        # Checking choice
        if choice.upper() == 'FIGHT':
            player.health += -1
            print('You punch the bird but hurt your hand in the process \n'
                  'you grab the key from the bird')
            # adding key both the inventory list and items_grabbed list
            player.inventory.append(key)
            items_grabbed.append(key)
        elif choice.upper() == 'GIVE FRUIT':
            # Checking for the cactus fruit in inventory
            if cactus_fruit in player.inventory:
                print('The bird eats the fruit and you take the key from the bird')

                # removing cactus fruit from inventory list, adding key to
                # inventory list and items_grabbed list.
                player.inventory.remove(cactus_fruit)
                player.inventory.append(key)
                items_grabbed.append(key)
            # if the fruit isn't in inventory this runs
            elif cactus_fruit not in player.inventory:
                print('You have no fruit to give')
        elif choice.upper() == 'HELP':
            get_key()
        else:
            mistype()
            get_key()

    def house():
        house_options = ['USE KEY', 'USEKEY', 'KEY', 'OPEN', 'UNLOCK']
        print("You walk up the house and find a locked door")
        if key in player.inventory:
            print('[Use Key]')
            enter()
            if choice.upper() in house_options:
                player.inventory.remove(key)
                inside_house()
        else:
            print("Where do you want to go?")
            print("[Cactus/Vulture]")

    def inside_house():
        print("You are inside the house")
        enter()
    lb()
    print("** WELCOME TO ADVENTURE **")
    lb()
    name = input("What's your name? \n > ")
    print("Welcome " + name + "!\n")
    desert()


main()