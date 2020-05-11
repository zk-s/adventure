def main():
    # Empty inventory to accumulate items in
    health = 5
    inventory = []
    items_grabbed = []
    cactus_fruit = 'Cactus Fruit'
    key = 'Key'
    choices = []
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
    player_commands = {
        'health': health,
        'inv': inventory,
        'inventory': inventory

    }

    def enter():
        global choice
        choice = input('<')
        if choice.lower() == 'help':
            help(inventory,health)
        print(choice)
        return choice
    # Prints out the current items in inventory
    def help(inventory, health):
        check = input("What do you wish to check? \nHealth/Inventory")
        print(player_commands[check.lower()])
        print('Anything else you want to check?')
        anything_else = input('>')
        if anything_else.lower() == 'yes':
            help(inventory, health)
        elif anything_else.lower() == 'no':
            return

    # Staring point. Not sure if I want to make it anything else then an inbewteen area
    def desert():
        i = 0
        while i == 0:
            print("You are in the desert. \nYou see a cactus and a vulture")
            print("Where do you want to go?")
            i += 1
        desert_first_choice = input('>')
        if desert_first_choice.upper() == 'HELP':
            help(inventory,health)
            desert()
        if desert_first_choice.upper() == 'CACTUS':
            cactus(inventory,health,items_grabbed)
        if desert_first_choice == 'yo':
            house(inventory,health,items_grabbed)
        elif desert_first_choice.upper() == 'VULTURE':
            vulture(inventory, health,items_grabbed)


    def vulture(inventory,health,items_grabbed):
        if key not in items_grabbed:
            print('you walk up to a large vulture standing over bones \n'
                  'the bird has a key around its neck. What do you wish to do?' )
            print('Fight')
            choice = input('>')
            if choice.lower() == 'fight':
                health += -1
                print('You punch the bird but hurt your hand in the process \n'
                      'you grab the key from the bird')
                inventory.append(key)
                items_grabbed.append(key)
            if choice.lower() == 'give fruit':
                if 'Cactus Fruit' in items_grabbed:
                    print('The bird eats the fruit and you take the key from the bird')
                    inventory.remove(cactus_fruit)
                    inventory.append(key)
                    items_grabbed.append(key)
                elif 'Cactus Fruit' not in items_grabbed:
                    print('You have no fruit to give')
        print('Where do you wish to go now?')
        print('House/Desert')
        choice = input('>')
        if choice.lower() == 'house':
            house(inventory, health, items_grabbed)
        elif choice.lower() == 'desert':
            desert()

    # Stage with a cactus. Player takes the fruit and uses it for a later objective.
    def cactus(inventory,health, items_grabbed):
        print('You walk up to the cactus')
        # Checks for fruit int inventory. If the player had already taken the fruit it will print
        # out a cactus with no fruit.
        if 'Cactus Fruit' not in items_grabbed:
            print(cactus_with_fruit)
            print("The cactus is tall with fruit blooming!")
            cactus_fruit_choice = input('Do you pick the fruit? \n>')
            if cactus_fruit_choice.upper() == 'YES':
                inventory.append(cactus_fruit)
                items_grabbed.append(cactus_fruit)

        # Prints cactus with no fruit
        elif cactus_fruit in items_grabbed:
            print(cactus_without_fruit)
            print("The cactus has no more fruit on it")


        print("Where do you want to go? \nType Desert or Vulture")
        cactus_exit = input(">")
        if cactus_exit.upper() == 'DESERT':
            desert()
        elif cactus_exit.upper() == 'VULTURE':
            vulture(inventory,health,items_grabbed)

    def house(inventory, health, items_grabbed):
        print("its a house")
        enter()
        print(choice)
        if choice == 'yo':
            print("hey")

    print("** WELCOME TO ADVENTURE ** ||")
    name = input("What's your name? \n > ")
    print("Welcome " + name + "!")
    desert()


main()