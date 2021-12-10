# Jacob Hershberger
# Lord of the Rings CLI Game
# Module 6 Project DIRECTION submission
import json
import Locations
import time
# import sleep

current_location = {}

# to expedite gameplay, set these values to 0
sleep_time = 0  # 3
short_sleep_time = 0 # 1
long_sleep_time = 0 # 6

def arrive_new_location(location):
    location_data = Locations.location_data()                
    return location_data[location]

def get_greeting(current_location):
    time.sleep(sleep_time)
    print('\nplease wait...\n\n\n\n')
    time.sleep(long_sleep_time)
    print(f'Welcome to {current_location["Location"]}\n{current_location["Description"]}\n')


def welcome_to_the_game():
    print("Welcome to the Lord of the Rings CLI Game. Your goal is to help Frodo and Sam destroy the ring of power.\n\nThe way you change directions is simple. Enter 'North' if you want to go north. Enter 'South' if you want to go south.\n\nAt some locations, you will have the ability to pick up various items that are crucial in your quest. You'll need to pick up these items in order to destroy the One Ring. To pick up an item, press y/n when prompted.\nTo view existing items, type 'Items' and all items you have accumulated will display\n\nEnjoy the game!\n\n")


def display_items(items_in_room):
    time.sleep(long_sleep_time)
    if len(items_in_room) > 0:
        print(f'\nHooray, it looks like there are {len(items_in_room)} items available for you here in {current_location["Location"]}')
        for items in items_in_room:
            print(f' --{items}')
            available_items.append(items)

    else:
        print(f'\nThere are no items for you in {current_location["Location"]}')


def pickup_items(available_items, items_held):
    for item in available_items:

        if item not in items_held:
            item_validated = False
            while item_validated == False:
                time.sleep(short_sleep_time)
                pickup_item = input(f'\nWould you like to include {item} in your quest? y/n ')
                pickup_item = pickup_item.lower()

                time.sleep(short_sleep_time)
                if pickup_item == 'y' or pickup_item == 'n':
                    if pickup_item == 'y':
                        # add item to collection
                        items_held.append(item)
                        print(f'\n{item} has been added. You now have the following to assist you in your quest')
                        for my_items in items_held:
                            print(f'    {my_items}')
                        item_validated = True
                    else:
                        print(f'\nYou have chosen not to include {item} on your quest. Let us hope you made the correct decision.')
                        item_validated = True
                else:
                    print(f'\nYou have entered {pickup_item}. please enter y/n')
        else:
            print(f'\nIt looks like you already have {item} joining you on your quest :)')
    return available_items
    
game = True
if __name__ == "__main__":
    welcome_to_the_game()
    # get initial location 
    location_data = Locations.location_data()
    first_location = list(location_data.keys())
    first_location = first_location[0]
    current_location = arrive_new_location(first_location)

    items_held = []

    # print greeting
    while game:
        get_greeting(current_location)


        # Display available items
        available_items = []
        display_items(current_location["Items"])



        # TODO Pick up items
        pickup_items(available_items, items_held)


        # Ask where they would like to go next
        time.sleep(sleep_time)
        print('\n\nAlas, it is time for you to move on in your quest to destroy the One Ring. Where would you like to go next?')
        loc_dir_validations = []
        loc_choice_validations = []

        for direction,new_location in current_location['Directions'].items(): 
            time.sleep(sleep_time)
            print(f' --{direction} to {new_location}')
            loc_dir_validations.append(direction)
            loc_choice_validations.append(new_location)



        # request and validate new direction choice
        location_validated = False
        while location_validated == False:
            time.sleep(short_sleep_time)
            new_location_choice = input('\nI would like to go: ')

            if new_location_choice.capitalize() in loc_dir_validations:
                # print('location validated :)')
                # TODO validate items for specific rooms
                print(f'Now heading {new_location_choice.capitalize()} towards {current_location["Directions"][new_location_choice.capitalize()]}')
                current_location = arrive_new_location(current_location["Directions"][new_location_choice.capitalize()])
                location_validated = True

                # Validate new room villian
                if current_location["Villian"]:
                    time.sleep(sleep_time)
                    print(f'\n\n{current_location["Lose_Description"]}\n\n')
                    time.sleep(sleep_time)
                    print('GAME OVER!!!\n\n')
                    game = False
                    location_validated = True
                elif current_location["Win"]:
                    print('\nCongratulations!!!! You have successfully destroyed the One Ring\n\nYou will now sail off into the west with Gandalf, Elrond, Bilbo and a whole host of other Elves that you do not know :)')
                    game = False
                    location_validated = True

                # Check if items are required to enter the next room
                elif len(current_location['Items_required']) > 0:
                    time.sleep(sleep_time)
                    for required_item in current_location['Items_required']:
                        if required_item not in items_held:
                            time.sleep(sleep_time)
                            print(f'\n\nMISSING ITEMS - GAME OVER!\n\nYou are missing {required_item} which is sorely needed at this point of your quest, and as a result you are unable to progress to {current_location["Location"]}.\nYOU HAVE FAILED in your quest to destroy the One Ring and all hope has subsequently faded')
                            game = False
                            location_validated = True
                            break

                # print(current_location)
            elif new_location_choice.lower() == 'exit':
                time.sleep(sleep_time)
                game = False
                location_validated = True
                print('Game Over')
                break
            elif new_location_choice.lower() == 'items':
                print(f'Your items are')
                for item in items_held:
                    print(item)
                break
            else:
                print(f'Where are you going??? {new_location_choice} is not a valid choice {loc_dir_validations}')


    




