def main():
    # Players health
    health = 5

    # Empty inventory to accumulate items in
    inventory = []

    # list to put items into. this is used to check if a player has already done an action.
    # Such as picking fruit from a cactus and not reprinting the cactus with fruit.
    items_grabbed = []

    # just some short cuts so I don't have to keep plugging in strings for items
    cactus_fruit = 'Cactus Fruit'
    key = 'Key'

    # The choices list I plan to use later on to have some type of weight to actions.
    # like if you punch the bird you'll be shamed for it, or if you didn't go to
    # certain room the game will make tease you for being blind.
    choices = []
    options = []

    #Ascii art

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
        'health': health,
        'inv': inventory,
        'inventory': inventory
    }
    # Function used to take in the players choice and give them the option to check
    # health and inventory instead of repasting code. Not happy with the global command.
    def enter():
        global choice
        choice = input('>')
        if choice.lower() == 'help':
            help(inventory, health)

    # A function meant for the player to be able to check there inventory or health
    # at anytime.

    def help(inventory, health):
        check = input("What do you wish to check? \nHealth/Inventory")
        print(player_commands[check.lower()])
        print('Anything else you want to check?')
        anything_else = input('>')
        if anything_else in player_commands:
            print(player_commands[anything_else])
        if anything_else.lower() == 'yes':
            help(inventory, health)

    # Staring point. Can travel to Cactus and Vulture from here
    def desert():
        print("You are in the desert. \nYou see a cactus and a vulture")
        print("Where do you want to go?")
        enter()
        if choice.upper() == 'HELP':
            desert()
        if choice.upper() == 'CACTUS':
            cactus(inventory,health,items_grabbed)
        if choice == 'yo':
            house(inventory,health,items_grabbed)
        elif choice.upper() == 'VULTURE':
            vulture(inventory, health,items_grabbed)

    # Vulture location. Ideally you want to give the vulture the cactus fruit to
    # not take damage and not hurt the bird. This is where you can obtained the key from.
    def vulture(inventory,health,items_grabbed):

        # Checking to see if the player has not collected the key from the vulture
        # if the player hasn't already collected the key it will run the code
        # saying the player see a vulture with a key around it's neck.
        if key not in items_grabbed:
            print('you walk up to a large vulture standing over bones \n'
                  'the bird has a key around its neck. What do you wish to do?' )

            # Checking for cactus fruit in inventory
            if cactus_fruit in inventory:
                print('Fight / Give fruit')
                enter()
            elif cactus_fruit not in inventory:
                print('Fight')
                enter()
            if choice.upper() == 'FIGHT':
                health += -1
                print('You punch the bird but hurt your hand in the process \n'
                      'you grab the key from the bird')
                # adding key both the inventory list and items_grabbed list
                inventory.append(key)
                items_grabbed.append(key)


            if choice.upper() == 'GIVE FRUIT':
                # Checking for the cactus fruit in inventory
                if 'Cactus Fruit' in inventory:
                    print('The bird eats the fruit and you take the key from the bird')

                    # removing cactus fruit from inventory list, adding key to
                    # inventory list and items_grabbed list.
                    inventory.remove(cactus_fruit)
                    inventory.append(key)
                    items_grabbed.append(key)
                # if the fruit isn't in inventory this runs
                elif 'Cactus Fruit' not in inventory:
                    print('You have no fruit to give')
        print('Where do you wish to go now?')
        print('House/Desert')
        enter()
        if choice.upper() == 'HOUSE':
            house(inventory, health, items_grabbed)
        elif choice.upper() == 'DESERT':
            desert()

    # Stage with a cactus. Player takes the fruit and uses it for a later objective.
    def cactus(inventory,health, items_grabbed):
        print('You walk up to the cactus')
        # Checks for fruit int inventory. If the player had already taken the fruit it will print
        # out a cactus with no fruit.
        if 'Cactus Fruit' not in items_grabbed:
            print(cactus_with_fruit)
            print("The cactus is tall with fruit blooming!")
            print('Do you pick the fruit? \n')
            enter()
            if choice.upper() == 'YES':
                inventory.append(cactus_fruit)
                items_grabbed.append(cactus_fruit)

        # Prints cactus with no fruit
        elif cactus_fruit in items_grabbed:
            print(cactus_without_fruit)
            print("The cactus has no more fruit on it")
        print("Where do you want to go? \nType Desert or Vulture")
        enter()
        if choice.upper() == 'DESERT':
            desert()
        elif choice.upper() == 'VULTURE':
            vulture(inventory, health, items_grabbed)

    def house(inventory, health, items_grabbed):
        print("its a house")

    print("** WELCOME TO ADVENTURE ** ||")
    name = input("What's your name? \n > ")
    print("Welcome " + name + "!")
    desert()


main()
