def main():
    # Player class where stats for the player along with functions for
    # the player will be kept. functions like show_health and show_inv are
    # kept inside of here to keep stats like inventory consistent when printed.
    # I plan to make more functions like show_map which will show the player a map
    # of the area and even show where they are. The show_map function should be
    # accessed though the help_command function .

    class Player:
        def __init__(self, first_name, health, inventory):
            self.first_name = first_name
            self.health = health
            self.inventory = inventory

        # Shows players current health.
        def show_health(self):
            print(line)
            print(str(player.health) + ' health')
            print(line)

        # Shows players current inventory.
        def show_inv(self):
            print(line)
            print(player.inventory)
            print(line)

    # Player stats. Ideally want to change the 'Zack' name to the name the player
    # chooses.
    player = Player('Zack', 5, [])

    # list to put items into. this is used to check if a player has already done an action.
    # Such as picking fruit from a cactus and not reprinting the cactus with fruit.
    items_grabbed = []

    # just some short cuts so I don't have to keep plugging in strings for items
    where_to = 'Where do you want to go?'
    help_caps = 'HELP'
    cactus_fruit = 'Cactus Fruit'
    key = 'Key'
    line = '__________________________________'

    # The choices list I plan to use later on to have some type of weight to actions.
    # like if you punch the bird you'll be shamed for it, or if you didn't go to
    # certain room the game will make tease you for being blind.
    # choices = []
    # options = []

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

    # Dictionary was going to be used for the help_command but didn't work out
    # the way I wanted it to. Keeping it here for now just in case I can think of
    # a way to use it.

    player_commands = {
        'HEALTH': player.health,
        'INV': player.inventory,
        'INVENTORY': player.inventory
    }

    # Function used to take in the players choice and give them the option to check
    # health and inventory by accessing the help_command function. Returns the variable
    # choice.
    def enter(options):
        choice1 = input('>')
        choice = choice1.upper()
        if choice == help_caps: # if choice == "HELP" the help command is called.
            help_command()

            # choice is still set to "HELP" so we need go reset the choice
            # before exiting the function or else we'll get mistype() called upon exiting
            # to the original function.

            options_string = '' # empty string to accumulate strings from options list
            i = 0

            # For loop code below will reformat options from ["Option1","Option2"] to [Option1/Option2]
            # so when it's printed out it's looks nicer.
            for item in options:

                # if item isn't the last item in options add it to list with a /
                # EX: [Option1/]
                if i + 1 < len(options):
                    options_string += item + '/'

                # if item is the last item in options add it to list without a /
                # EX: [Option1/Option2]
                elif i + 1 == len(options):
                    options_string += item
                i += 1

            # Reformats options_string from Option1/Option2 to [Option1/Option2]
            options_string_formatted = '[' + options_string + ']'

            while choice not in options:
                print("Your current choices are:")
                print(options_string_formatted)
                choice1 = input('>')
                choice = choice1.upper()
        return choice
    # A function meant for the player to be able to check there inventory or health
    # at anytime through the enter function.
    def help_command():
        # Names that could be used to access the players inventory or health.
        inventory_names = ['INV', 'INVENTORY', "2"]
        health_names = ['HEALTH', '1']
        all_names = [health_names + inventory_names]

        # User enters what they want to check and the input is saved as check1.
        # check1 is then converted to check with the user input string converted
        # to all upper cases to standardize responses.
        check1 = input("What do you wish to check? \n[Health/Inventory] \n>")
        check = check1.upper()

        # Checking to see if check is in inventory_names or health_names.
        # If not the while loop will tell them there input was not a valid
        # choice and ask for another input. The player will only be able to
        # escape the loop by inputting a name in inventory names or health_names.
        while check not in health_names and check not in inventory_names:
            print("Not an option")
            check1 = input("What do you wish to check? \n[Health/Inventory] \n>")
            check = check1.upper()
            print(check)

        # The player input was either health_names or inventory names and
        # but now we need to see if the input was for health or inventory.
        if check in health_names:
            Player.show_health(player)
        elif check in inventory_names:
            Player.show_inv(player)

        # This move varible is only to give the user a second to read their
        # health or inventory before returning to the game. move varible is
        # not used for anything else.
        move = input('[Press enter to continue]\n')

    # Function used when the player enters an input that is not an option.
    # Prints out a string saying 'I don't know that'.
    def mistype():
        idk = "\nI don't know that\n"
        print(line + idk + line)

    # Function used to just print a line. Used to make things look more formatted.
    def lb():
        print(line)

    # Function for starting the game. We acquire the players name here and
    # send them to the desert function.
    def start():
        lb()
        print("** WELCOME TO ADVENTURE **")
        lb()
        name = input("What's your name? \n > ")
        print("Welcome " + name + "!\n")
        print("Type 'help' anytime to access player commands\n")
        desert()

    # Staring point. Can travel to Cactus and Vulture from here.
    # Most of these location function work the same. Look at the
    # comments in the cactus() function for more in depth comments.
    def desert():
        # options list of where the user can travel. This is used with the while
        # loop a few lines down to check if the user enter a valid option.
        options = ['CACTUS', 'VULTURE']
        print("You are in a desert. \nWhere do you want to go?")
        print("[Cactus/Vulture]")
        choice = enter(options)
        while choice not in options:
            if choice != help_caps:
                mistype()
            print(where_to)
            print("[Cactus/Vulture]")
            choice = enter(options)
        if choice == 'CACTUS':
            cactus()
        elif choice == 'VULTURE':
            vulture()

    # Location with a cactus. I explain how these location functions work
    # in depth with comments in this cactus function. Most of these location
    # functions work the similarly to each other so this one will be in depth
    # while others like vulture() will only have minimal or needed comments.
    #
    # Player ideally takes the fruit and gives it to the vulture in the get_key function in order
    # to not take damage.
    def cactus():
        print('You walk up to the cactus')

        # Checking for fruit int in items_grabbed list. If the player had already taken the fruit it will print
        # out a cactus with no fruit. If the player hasn't taken the fruit yet the cactus will
        # appear with fruit on it. This is to make sure the player doesn't come back after picking
        # the fruit to find a cactus with fruit still on it. And to make sure the player can't take
        # more then one fruit.
        if cactus_fruit not in items_grabbed:
            options = ['YES', 'NO']
            print(cactus_with_fruit)
            print("The cactus is tall with fruit blooming! Do you pick up the fruit?")
            print('[Yes/No]')
            # The enter function is ran asking the user for input. Choice is returned
            # to the in enter and the returned value is set equal to choice in this function.
            choice = enter(options)

            # If the player enters an input not in cactus_options they enter this while loop
            # until they enter and option in cactus_options AKA "Yes" or "No".
            while choice not in options:
                mistype()
                print("The cactus is tall with fruit blooming! Do you pick up the fruit?")
                print('[Yes/No]')
                choice = enter(options)

            # If the player enters "Yes" a line prints saying they picked up the fruit
            # and the fruit is added to player.inventory and items_grabbed list.
            # The fruit is added to the items_grabbed list to ensure if the user returns to the cactus
            # location they will not be shown the cactus with fruit or given the option
            # to pick more fruit.
            if choice == 'YES':
                print("You pick up the fruit!")
                player.inventory.append(cactus_fruit)
                items_grabbed.append(cactus_fruit)
            elif choice == 'NO':
                print("You leave the fruit alone")

        # Checks the items_grabbed list to see if the fruit has already been grabbed by the player.
        # if so it prints out the cactus with no fruit. Sends the player out of the if elif statement and
        # onto the rest of the function asking where the player wants to travel to next.
        elif cactus_fruit in items_grabbed:
            print(cactus_without_fruit)
            print("The cactus has no more fruit on it")

        # Asking the player where they want to go to next.
        options = ['DESERT', 'VULTURE']
        print("Where do you want to go? \n[Desert/Vulture]")
        choice = enter(options)
        while choice not in options:
            mistype()
            print(where_to)
            print('[Desert/Vulture]')
            choice = enter(options)
        if choice == 'DESERT':
            desert()
        elif choice == 'VULTURE':
            vulture()

    # Vulture location. Checks to see if you have the key already from the vulture.
    # if the player doesnt have the key in items_grabbed list they are sent to the
    # get_key() function to retrieve the key. If they have already grabbed the key
    # they are given a travel choice to the house(to use the key) or back to the desert.
    def vulture():
        if key not in items_grabbed:
            get_key()
        options = ['HOUSE', 'DESERT']
        print('Where do you wish to go now?')
        print('[House/Desert]')
        choice = enter(options)
        while choice not in options:
            print(choice)
            mistype()
            print(where_to)
            print('[House/Desert]')
            choice = enter(options)
        if choice == 'HOUSE':
            house()
        elif choice == 'DESERT':
            desert()

    # Player is sent here from vulture() if they have not already obtained the key.
    # Player should always be sent here before entering the rest of the vulture function.
    # The key can be obtained from the vulture by fighting it or giving it the cactus
    # fruit.
    def get_key():
        options = ['FIGHT', 'GIVE FRUIT']
        print('you walk up to a large vulture standing over bones \n'
              'the bird has a key around its neck. What do you wish to do?')
        if cactus_fruit in player.inventory:
            print('[Fight/Give fruit]')
            choice = enter(options)
        elif cactus_fruit not in player.inventory:
            print('[Fight]')
            choice = enter(options)
        while choice not in options:
            if cactus_fruit in player.inventory:
                mistype()
                print('[Fight/Give fruit]')
                choice = enter(options)
            elif cactus_fruit not in player.inventory:
                mistype()
                print('[Fight]')
                choice = enter(options)

        # Checking choice
        if choice == 'FIGHT':

            # Player loses 1 health, flavor text prints and show_health is ran to
            # show the player they lost 1 health.
            player.health += -1
            print('You punch the bird but hurt your hand in the process \n'
                  'you grab the key from the bird')
            Player.show_health(player)

            # adding key both the inventory list and items_grabbed list
            player.inventory.append(key)
            items_grabbed.append(key)

        elif choice == 'GIVE FRUIT':
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
                get_key()

    # House location that the key from the vulture location can be used at.
    # Locations that can be accessed from here are is only the inside of the
    # house.
    def house():
        options = ['USE KEY', 'USEKEY', 'KEY', 'OPEN', 'UNLOCK']
        print("You walk up the house and find a locked door")
        if key in player.inventory:
            print('[Use Key]')
            choice = enter(options)
            while choice not in options:
                mistype()
                print("What do you want to do?")
                print('[Use Key]')
                choice = enter(options)
            if choice in options:
                player.inventory.remove(key)
                inside_house()

        else:
            print(where_to)
            print("[Cactus/Vulture]")

    def inside_house():
        print("You are inside the house")
        choice = enter()

    start()



main()
