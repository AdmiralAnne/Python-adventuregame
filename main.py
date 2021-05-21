print("Welcome to my New Game~ Adventure Island !")
name = input("What is your name? ")
age = int(input("what is your age? "))
health = 20

print(f"Hello {name}, Your are {age} years old !")\

if age >= 18:
    print("Your are old enough to play! ")
    ans = input("Do you want to play> (Yes/No) ").lower()
    if ans == "yes":
        print(
            f"The King of Yuvetia has asked for your help to find a lost treasure in the northern mountains. It is a dangerour mission but he Believer you are the best treasure hunter. You will begin your journery now. Good Luck Young, {name}"
        )
        print(f"Let's Play {name} \nyou have {health} health ! ")

        choice1 = input("You may pick a weapon(Sword/hammer)").lower()
        if choice1 == "sword" or choice1 == "hammer":
            print(
                f"Congratulations You have chosen the mighty {choice1} ! \nLet's head over the Lake!"
            )
            choice2 = input(
                "There's a lake in front of you. Would you like to go across it? or Around it? (around/across)"
            )
            if choice2 == "around":
                choice3 = input((
                    "You chose to go around the lake, Wise Choice. You may proceed~ \nThere's a wild boar ahead of you. Would you like to flee or Engage ?(flee/engage)"
                )).lower()
                if choice3 == "flee":
                    print(
                        "You decided to flee from the scene. You have lost 5 health while waiting in the rain."
                    )
                    health -= 5
                    print(f"you have {health} health remaining")
                    choice6 = input(
                        "The mother boar arrived at the scene. what will you do? (fight/fight)"
                    )
                    if choice6 == "fight":
                        print("You died fighting the mother boar")
                    else:
                        print("wrong choice my friend~ You died")
                elif choice3 == "engage":
                    print(
                        f"You used your {choice1} to enage the Wild Boar. \nCongratulations, you have successfully killed the Boar"
                    )
                    ans = input(
                        f"You have {health} health remaining.\nPress 1 to procees or 2 to abbandon quest(1 / 2) "
                    )
                    if ans == "1":
                        print(
                            f"Wise Choice {name}, Let's proceed to the mountains.\n\n"
                        )
                        choice4 = input(
                            "You can see the mountain ahead. Yould you like to use the stairs or Climb using the ropes? (stairs/ropes)"
                        ).lower()
                        print(f"you have chosen to climb using {choice4}\n")
                        if choice4 == "stairs":
                            print(
                                f"you have reached the top of the mountain. Untold Riches awaits you {name}!! \n One final Choice to decide your fate."
                            )
                            choice5 = input(
                                "Would you like to return the treasure to the king or Do you wan to keep The Treasure to your self? (king/self)"
                            ).lower()
                            if choice5 == "self":
                                print(
                                    f"The King's men arrived at the scene and saw you fleeing with the Treasure.\nYou were executed"
                                )
                                print(
                                    "---------------------T-h-e-------E-n-d------------------"
                                )
                            elif choice5 == "king":
                                print(
                                    f"You were loyal to the King, Young {name}, You have been rewarded handsomely."
                                )
                                print(
                                    "CONGRATULATIONS~ //////////   the end   /////////////// \n Made by @Marjiba_Jamir and @Samuel_Khongthau"
                                )
                        elif choice4 == "ropes":
                            print(
                                f"The ropes gave out, You lost your remaining health.\nYou died -------the end ---------"
                            )
                    elif ans == "2":
                        print(
                            f"You have decide to abbandon the quest.\nGoodbye {name}.\n-----------------------------T-h-e-----E-n-d--------------------------"
                        )
            elif choice2 == "across":
                health -= 20
                print(
                    f"you drowned and lost 20 health \nYou now have {health} health \n----------------Game Over--------------"
                )
            else:
                print("Invalid choice ...Game Has ended")
        else:
            print("Invalid Weapon Choice, You have been Executed ")
else:
    print("you are not old enough to play.. Sorry")
    print(
        "---------------------------------t-h-e---e-n-d-----------------------------"
    )
