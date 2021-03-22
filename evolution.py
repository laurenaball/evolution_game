import time
import random


def print_pause(string, sec):
    print(string)
    time.sleep(sec)


def intro():
    print_pause("you open your eyes...", 2)
    print_pause("and find yourself in a field of grass up to your elbows", 3)
    print_pause("you are covered in a uniform material that allows you to"
                "sense the moving air", 4)
    print_pause("you look down to see why you are positioned such that your"
                "feet, hands, and bottom", 4)
    print_pause("are all on the ground...", 4)
    print_pause("...", 3)
    print_pause("you realize you are a cat", 4)


def valid_input(prompt, option1, option2, option3="1"):
    while True:
        response = input(prompt)
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_pause("i don't understand", 1)
    return response


def lick_fur(kitty_attributes):
    body = ["in between your toes", "on the back of your left paw", "on your "
            "shoulder", "around your ear"]
    feeling = ["different", "sticky", "weird", "dirty"]
    print_pause("you realize the fur " + random.choice(body) + " feels "
                + random.choice(feeling), 2)
    response = valid_input("would you like to stop and clean it? (yes/no)\n",
                           "yes", "no")
    if "yes" in response:
        time.sleep(1)
        print_pause("*licks fur*", 2)
        print_pause("...", 2)
        print_pause("ah, that feels much better", 2)
        if "dirty" in kitty_attributes:
            kitty_attributes.remove("dirty")
        if "clean" not in kitty_attributes:
            kitty_attributes.append("clean")
        return kitty_attributes
    if "no" in response:
        if "clean" in kitty_attributes:
            kitty_attributes.remove("clean")
        if "dirty" not in kitty_attributes:
            kitty_attributes.append("dirty")
            time.sleep(2)
        return kitty_attributes



def scratch():
    body = ["right ear", "left ear", "neck"]
    print_pause("your " + random.choice(body) + " itches", 2)
    response = valid_input("would you like to stop and scratch it? (yes/no)\n",
                           "yes", "no")
    if "yes" in response:
        time.sleep(2)
        print_pause("*scratches*", 3)


def hunting_practice(hunting_skill):
    animal = ["lizard", "snake", "cricket", "baby bird", "spider", "bug"]
    random_animal = random.choice(animal)
    print_pause("a wild " + random_animal + " appeared", 2)
    response = valid_input("would you like to try to catch it? (yes/no)\n",
                           "yes", "no")
    time.sleep(1)
    if "yes" in response:
        print_pause("\nyou pounce", 2)
        print_pause("...", 3)
        catch = random.randint(1, 3)
        if catch == 0: #change back to 1
            print_pause("it got away!", 2)
        else:
            print_pause("you caught a " + random_animal, 1)
            print_pause("yum! it is surprisingly delicious", 2)
            hunting_skill.append(random_animal)

            return hunting_skill



def through_grass():
    print_pause("\n...you continue walking through the grass", 3)
    return


def walking(kitty_attributes, hunting_skill):
    print_pause("\n...you walk through the grass", 2)
    itch = random.randint(1, 3)
    if itch == 1:
        scratch()
        through_grass()
    dirty = random.randint(1, 2)
    if dirty == 1:
        kitty_attributes = lick_fur(kitty_attributes)
        through_grass()
    hunting_practice(hunting_skill)
    through_grass()


def get_direction(kitty_attributes, hunting_skill):
    walking(kitty_attributes, hunting_skill)
    print_pause("you see a house and a forest", 2)
    response = valid_input("which would you like to walk toward? "
                           "(house/forest)\n", "house", "forest")
    print_pause("you turn towards the " + response, 3)
    walking(kitty_attributes, hunting_skill)
    if response == "house":
        approach_house(kitty_attributes, hunting_skill)
    if response == "forest":
        approach_forest(kitty_attributes, hunting_skill)


def approach_house(kitty_attributes, hunting_skill):
    if "domestic" in kitty_attributes:
        if "clean" in kitty_attributes:
            print_pause("the woman opens the door for you to come inside", 2)
            print_pause("congratulations! you have won the game of evolution",
                        2)
            game_over()
        else:
            print_pause("the woman comes to pet you", 2)
            print_pause("but she won't let you inside because you are dirty",
                        3)
            print_pause("you get up to go wonder around", 2)
    if "mean" in kitty_attributes:
        print_pause("the door is closed and no one is outside", 3)
    if "undecided" in kitty_attributes:
        print_pause("you have reached the house", 2)
        print_pause("a woman comes out to pet you and brings you food", 2)
        print_pause("you decide she looks trusting", 2)
        print_pause("you eat the food and let her pet you", 3)
        print_pause("\nshe touches your stomach", 3)
        print_pause("\nwhat do you do?", 2)
        response = str(valid_input("  1. bite her and run away\n"
                                   "  2. allow it, but provide a gentle"
                                   " warning that you are displeased\n"
                                   "  3. allow it, you feel safe with her\n"
                                   "(1, 2 or 3)\n", "1", "2", "3"))
        time.sleep(3)
        if response == "1":
            kitty_attributes.append("mean")
            kitty_attributes.remove("undecided")
        if response == "2":
            print_pause("you think to yourself", 1)
            print_pause("\"that wasn't so bad\"", 2)
            print_pause("you get up to go wonder around", 4)
        if response == "3":
            print_pause("you think to yourself", 1)
            print_pause("\"that was pretty nice\"", 3)
            print_pause("you get up to go wonder around", 4)
            kitty_attributes.append("domestic")
            kitty_attributes.remove("undecided")
    get_direction(kitty_attributes, hunting_skill)


def approach_forest(kitty_attributes, hunting_skill):
    print_pause("you enter the forest", 2)
    print_pause("the trees block out the sun and your view of the house", 2)
    if len(hunting_skill) > 2:
        print_pause("you have failed to outsmart evolution. you live in the "
                    "woods. happy hunting", 2)
        game_over()
    else:
        print_pause("you see a juicy looking bug scurry by", 2)
        print_pause("you try to catch it but it disappears too quickly", 2)
        print_pause("you are not skilled enough to find food here yet", 3)
        print_pause("you are hungry", 3)
        print_pause("you better keep wondering around in the grass...", 4)
        get_direction(kitty_attributes, hunting_skill)


def game_over():
    print_pause("\nGAME OVER", 2)
    response = valid_input("would you like to play again? (y/n)\n", "y", "n")
    if "y" == response:
        play_game()
    if "n" == response:
        quit()


def play_game():
    hunting_skill = []
    kitty_attributes = ["undecided"]
    # intro()
    get_direction(kitty_attributes, hunting_skill)


play_game()
