import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("Welcome Rookie at the main training center of the Avengers!")
    print_pause("My name is Vision and I will guide you throughout the day.")
    print_pause("To get your own Avengers Membership access to the facility, "
                "first you have to prove yourself!")
    print_pause("Please, follow me to the lobby!\n")
    print_pause("After following Vision, you find yourself in the huge lobby "
                "area with some new cadet and their mentors...")
    print_pause("...like Spiderman, Black Widow, or the Falcon.")
    print_pause("Vision stops in the center of the lobby "
                "and turns towards you.\n")
    print_pause("You need to go through some test and process, "
                "but I will be here if you need further help!")
    print_pause("Good luck!")


def first_room(items, villains):
    print_pause("You enter the Scanning room, where you have to check-in.")
    if "ID card" in items:
        print_pause("You already have your Cadet ID card, "
                    "nothing else to do here.\n")
        back_and_choose(items, villains)
    else:
        print_pause("Hawkeye welcomes you and asks you to "
                    "step in the scanning area.")
        print_pause("As you step on the footprints on the floor, "
                    "a machine starts whirling and quickly "
                    "scan your body, handprint and iris.")
        print_pause("After the scanning, you get your own "
                    "Cadet ID card from Hawkeye.\n")
        items.append("ID card")
        back_and_choose(items, villains)


def second_room(items, villains):
    print_pause("You enter the Theory test room, where Vanda welcomes you.")
    if "certificate" in items:
        print_pause("She checks your ID and your test results, and "
                    "because you passed, there is nothing else to do here.\n")
        back_and_choose(items, villains)
    else:
        print_pause("She asks for your ID to check it.")
        if "ID card" in items:
            print_pause("You handle your card to her.")
            print_pause("She takes a look at it, then gives you a "
                        "tablet to fill out the test.")
            print_pause("You sit down to a free table and start your test.")
            print_pause("After you finished, you handle the tablet to "
                        "Vanda for evaluation...\n")
            print_pause("She goes through all of your answers, "
                        "then turns towards you...\n")
            print_pause("Congratulations! You passed the test.")
            print_pause("Here is your certificate! Good luck with the rest!\n")
            items.append("certificate")
            back_and_choose(items, villains)
        else:
            print_pause("Unfortunately, you haven't got your ID card yet, "
                        "so can't fill out the test.\n")
            back_and_choose(items, villains)


def third_room(items, villains):
    print_pause("You enter the physical test room, "
                "where Iron Man welcomes you.")
    print_pause("He asks for your ID card to check it.")
    if "ID card" in items:
        print_pause("You handle your card to him and "
                    "he takes a quick look at it.")
        print_pause("Then he turns towards you:\n")
        print_pause("Did you pass the theory test?\n")
        if "certificate" in items:
            print_pause("You show your test result to him...\n")
            print_pause("Well done! You are ready for the last test.")
            print_pause("In the next simulation, you will have to "
                        "fight against a super-villain.")
            print_pause("You can choose a weapon to fight with, "
                        "but choose wisely!")
            print_pause("Are you ready?\n")
            print_pause("You take a deep breath and step aside the "
                        "table with the weapons on it.\n")
            print_pause("Get ready!\n")
            print_pause("3\n")
            print_pause("2\n")
            print_pause("1\n")
            boss_fight(items, villains)
            print_pause("The simulation ends and Iron Man "
                        "turns towards you.\n")
            print_pause("Congratulations! You did it with perfect results.")
            print_pause("You passed all your tests and earned the "
                        "membership acces ID.\n")
            print_pause("Welcome onboard Avenger!\n")
            print_pause("The End!\n\n")
        else:
            print_pause("After he realize you didn't do the theory test yet, "
                        "he kindly refuse the physical test.\n")
            back_and_choose(items, villains)
    else:
        print_pause("After he realize you didn't have your ID card yet, "
                    "he kindly refuse the physical test.\n")
        back_and_choose(items, villains)


def boss_fight(items, villains):
    boss = random.choice(villains)
    print_pause("Suddenly " + boss + " appears in the middle of the "
                "training room and immediately attacks you.")
    if boss == "Thanos":
        print_pause("Which weapon will you choose to fight against him:\n")
        weapon = input("a. Captain's shield\n"
                       "b. Stormbreaker\n"
                       "c. Iron Man's suit\n").lower()
        if weapon == "a":
            print_pause("You quickly grab the shield and run towards Thanos.")
            print_pause("Unfortunately, he destroys your shield with "
                        "his blade and defeat you.")
            print_pause("You failed the test, but due to your test results, "
                        "Iron Man gives you another chance and "
                        "restart the simulation.\n")
            boss_fight(items, villains)
        elif weapon == "b":
            print_pause("You quickly grab Thor's stormbreaker "
                        "and run towards Thanos.")
            print_pause("He tries to use his infinity stones, but you are "
                        "quicker and with one slash, you defeat him.")
        elif weapon == "c":
            print_pause("You quickly put on Iron Man's suit and "
                        "run towards Thanos.")
            print_pause("Unfortunately, he destroys your suit with "
                        "his blade and defeat you.")
            print_pause("You failed the test, but due to your test results, "
                        "Iron Man gives you another chance and "
                        "restart the simulation.\n")
            boss_fight(items, villains)
        else:
            print_pause("Please choose from the avaliable weapons!")
            print_pause("The simulation reboots itself.")
            boss_fight(items, villains)
    elif boss == "Ultron":
        print_pause("Which weapon will you choose to fight against him:\n")
        weapon = input("a. Captain's shield\n"
                       "b. Stormbreaker\n"
                       "c. Iron Man's suit\n").lower()
        if weapon == "a":
            print_pause("You quickly grab the shield and run towards Ultron.")
            print_pause("Unfortunately, he blasts your shield out from "
                        "your hand and defeat you.")
            print_pause("You failed the test, but due to your test results, "
                        "Iron Man gives you another chance and "
                        "restart the simulation.\n")
            boss_fight(items, villains)
        elif weapon == "b":
            print_pause("You quickly grab Thor's stormbreaker and "
                        "run towards Ultron.")
            print_pause("Unfortunately, he blasts your weapon out from "
                        "your hand and defeat you.")
            print_pause("You failed the test, but due to your test results, "
                        "Iron Man gives you another chance and "
                        "restart the simulation.\n")
            boss_fight(items, villains)
        elif weapon == "c":
            print_pause("You quickly put on Iron Man's suit and "
                        "run towards Ultron.")
            print_pause("He tries to blast you, but you are quicker "
                        "and defeat him with all your rockets.")
        else:
            print_pause("Please choose from the avaliable weapons!")
            print_pause("The simulation reboots itself.")
            boss_fight(items, villains)
    elif boss == "Red Skull":
        print_pause("Which weapon will you choose to fight against him:\n")
        weapon = input("a. Captain's shield\n"
                       "b. Stormbreaker\n"
                       "c. Iron Man's suit\n").lower()
        if weapon == "a":
            print_pause("You quickly grab the shield and run "
                        "towards Red Skull.")
            print_pause("He tries to shoot you with his special gun, but you "
                        "reflect back the blast to him and defeat him.")
        elif weapon == "b":
            print_pause("You quickly grab Thor's stormbreaker and "
                        "run towards Red Skull.")
            print_pause("Unfortunately, he blasts your weapon out from "
                        "your hand and defeat you.")
            print_pause("You failed the test, but due to your test results, "
                        "Iron Man gives you another chance and "
                        "restart the simulation.\n")
            boss_fight(items, villains)
        elif weapon == "c":
            print_pause("You quickly put on Iron Man's suit and run "
                        "towards Red Skull.")
            print_pause("Unfortunately, he blasts your suit with his "
                        "special gun and defeat you.")
            print_pause("You failed the test, but due to your test results, "
                        "Iron Man gives you another chance and "
                        "restart the simulation.\n")
            boss_fight(items, villains)
        else:
            print_pause("Please choose from the avaliable weapons!")
            print_pause("The simulation reboots itself.")
            boss_fight(items, villains)


def back_and_choose(items, villains):
    print_pause("You head back to Vision in the main lobby.")
    choose_room(items, villains)


def choose_room(items, villains):
    print_pause("Vision points to the three doors at the other "
                "end of the lobby.")
    print_pause("Each door leads to another room. Please choose, "
                "where would you like to go:")
    room = input("1. Scanning\n"
                 "2. Theory test\n"
                 "3. Physical test\n")
    if room == "1":
        first_room(items, villains)
    elif room == "2":
        second_room(items, villains)
    elif room == "3":
        third_room(items, villains)
    else:
        print_pause("Please press the correct number!\n")
        choose_room(items, villains)


def play_again():
    again = input("Would you like to play again? Yes or No?\n").lower()
    if again == "yes":
        play_game()
    elif again == "no":
        print_pause("Thank you for the game!")
    else:
        play_again()


def play_game():
    items = []
    villains = ["Thanos", "Ultron", "Red Skull"]
    intro()
    choose_room(items, villains)
    play_again()


play_game()
