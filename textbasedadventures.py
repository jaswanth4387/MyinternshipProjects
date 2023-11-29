def get_player_name():
    return input("Enter your character's name: ")

def get_player_choice(prompt="Enter the number of your choice: "):
    try:
        choice = int(input(prompt))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_player_choice(prompt)

def introduce_characters(player_name):
    print(f"Welcome, {player_name}! You are a member of an elite team assembled by the Athens National Archaeological Museum.")
    print("The team is led by Dr. David Handerson, a senior archaeologist, and his assistant, Bruce Banner, a junior archaeologist.")
    print("Your fellow team members include Kaira Krishan, a translator of ancient languages, Hiegh Yen Chi, a navigator skilled in map reading, and Jack Ryan, a computer expert.")

def start_journey():
    print("\n** En Route to Angkor Wat **")
    print("The team boards a flight, embarking on a journey to Angkor Wat.")
    print("As the plane soars through the clouds, the team members engage in a conversation about their previous explorations.")

    # Team Conversation
    print("\n** Team Conversation **")
    print("Dr. Handerson: Remember our expedition in Machu Picchu, Bruce? The ancient architecture was fascinating.")
    print("Bruce Banner: Ah, yes! I'll never forget the intricate stonework. It's amazing how advanced they were.")
    print("Kaira Krishan: Machu Picchu was incredible, but I'm eager to decipher the unique inscriptions at Angkor Wat.")
    print("Jack Ryan: Speaking of decoding, remember that encrypted message in Petra? That was a challenge!")
    print("Hiegh Yen Chi: Petra was a navigational puzzle, but I've got a good feeling about our map readings in Angkor Wat.")
    print("Dr. Handerson: Each site has its mysteries. Let's apply our experiences to uncover the secrets of Angkor Wat.")
    print("Kaira Krishan: Agreed! Angkor Wat is known for its ancient language inscriptions. I'm excited to translate them.")
    print("Jack Ryan: Our skills complement each other. We make a great team!")

    # Journey Duration
    print("\nThe journey takes two days. The team arrives at the site, ready for their next archaeological adventure.")
    morning_journey()

def morning_journey():
    print("\n** Morning Journey **")
    print("The team gathers at the entrance of Angkor Wat, ready to embark on the morning exploration.")
    print("Dr. Handerson: Good morning, team! Let's open the puzzled door and begin our journey.")
    print("You approach the mysterious door, covered in intricate carvings and symbols.")
    print(f"{player_name}, how would you like to proceed?")
    print("1. Use ancient knowledge to decipher the symbols and open the door")
    print("2. Seek assistance from Kaira Krishan to translate the carvings")
    print("3. Let Jack Ryan attempt to hack into the door's mechanism")
    print("4. Analyze the structure of the door for any mechanical clues")

    choice = get_player_choice()

    if choice == 1:
        print("You use your knowledge of ancient symbols to decipher the carvings and successfully open the door.")
        print("\n** Team Conversation **")
        print(f"Dr. Handerson commends, '{player_name},Excellent work! Now, let's explore the chambers and uncover the secrets.'")
        print("The Team enters into temple and exploring the chambers")
        mysterious_chambers()
    elif choice == 2:
        print("You seek assistance from Kaira Krishan to translate the carvings and understand the door's mechanism.")
        print("\n** Team Conversation **")
        print("Kaira Krishan translates the symbols, revealing the door's secrets. Dr. Handerson says, 'Great teamwork! Let's proceed.'")
        print("The Team enters into temple and exploring the chambers")
        mysterious_chambers()
    elif choice == 3:
        print("You ask Jack Ryan to use his hacking skills to open the door's mechanism.")
        print("Jack Ryan: 'I'll give it a shot.' After a few moments, he successfully opens the door.")
        print("\n** Team Conversation **")
        print("Dr. Handerson nods, 'Impressive, Jack! Now, let's explore the chambers and uncover the secrets.'")
        print("The Team enters into temple and exploring the chambers")
        mysterious_chambers()
    elif choice == 4:
        print("You analyze the structure of the door, looking for any mechanical clues.")
        print("Bruce Banner: 'I can see how it's designed. I think I can unlock it.' He successfully opens the door.")
        print("\n** Team Conversation **")
        print("Dr. Handerson says, 'Well done, Bruce! Now, let's explore the chambers and uncover the secrets.'")
        print("The Team enters into temple and exploring the chambers")
        mysterious_chambers()
    else:
        print("Invalid choice. Please try again.")
        morning_journey()  # Restart the event if the choice is invalid.
        


def mysterious_chambers():
    print("\n** Mysterious Chambers **")
    print("You enter a chamber filled with strange symbols and artifacts. Kaira Krishan, the language translator, examines the inscriptions.")
    print("As Dr. David Handerson examines a rare flower, toxic fumes are released, rendering him unconscious.")

    # Event: Dr. Handerson's Unconsciousness
    print("\n** Dr. Handerson's Unconsciousness **")
    print("Dr. Handerson collapses, overcome by the toxic fumes from the rare flower.")
    print(f"{player_name}, what will you do?")
    print("1. Administer basic first aid to Dr. Handerson")
    print("2. Signal Bruce Banner to analyze the toxic fumes and find an antidote")
    print("3. Take the lead and explore the chamber on your own")
    print("4. Seek guidance from Kaira Krishan on dealing with the toxic exposure")

    choice = get_player_choice()

    if choice == 1:
        print("You administer basic first aid to Dr. Handerson, trying to stabilize him.")
        print("\n** Team Conversation **")
        print("Kaira Krishan suggests, 'Let's find an antidote quickly. We need Dr. Handerson back on his feet.'")
        find_antidote()
    elif choice == 2:
        print("You signal Bruce Banner to analyze the toxic fumes and find an antidote.")
        print("\n** Team Conversation **")
        print("Bruce Banner takes charge of the situation, 'I'll analyze the fumes and find an antidote. You explore the chamber.'")
        explore_chamber(player_name)
    elif choice == 3:
        print("You decide to take the lead and explore the chamber on your own.")
        explore_chamber(player_name)
    elif choice == 4:
        print("You seek guidance from Kaira Krishan on dealing with the toxic exposure.")
        print("\n** Team Conversation **")
        print("Kaira Krishan advises, 'While Bruce analyzes the fumes, let's explore the chamber cautiously.'")
        explore_chamber(player_name)
    else:
        print("Invalid choice. Please try again.")

def find_antidote():
    print("While Kaira Krishan tends to Dr. Handerson, you search for an antidote within the chamber.")
    print("You discover a hidden compartment with ancient herbs that can neutralize the toxins.")
    print("\n** Team Conversation **")
    print("Kaira Krishan says, 'Good find! Let's administer the antidote to Dr. Handerson and proceed with caution.'")
    administer_antidote()

def administer_antidote():
    print("You administer the antidote to Dr. Handerson, who gradually regains consciousness.")
    print("\n** Team Conversation **")
    print("Dr. Handerson, now recovering, says, 'Thank you, {player_name}. Let's continue our exploration with caution.'")
    explore_chamber(player_name)
    


def explore_chamber(player_name):
     print("With Dr. Handerson recovered, the team continues to explore the mysterious chamber.")
     print("You come across ancient artifacts and carvings that hint at the temple's rich history.")
     print(f"there are two passages!{player_name} what will we do?")
     print("1. Explore the left passage.")
     print("2. Explore the right passage.")
     print("3. End the exploration.")

     while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            explore_left_passage_after_trap(player_name)
        elif choice == '2':
            explore_right_passage(player_name)
        elif choice == '3':
            print("Ending the exploration.")
            ending_successful_discovery()
              # Exit the loop and end the exploration
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")

def explore_left_passage_after_trap(player_name):
    print("\nAfter successfully disarming the trap in the left passage, the team enters a chamber.")
    print("This chamber is adorned with ancient inscriptions in a language you've studied.")
    print(f"{player_name}, this seems to be an opportunity to use your knowledge of ancient languages.")
    
    # Event: Exploring Ancient Language
    print("\n** Exploring Ancient Language **")
    print("1. Take the time to decipher the inscriptions")
    print("2. Ask Kaira Krishan for assistance")
    print("3. Document the inscriptions for later analysis")


    choice = get_player_choice()

    if choice == 1:
        print("You decide to take the time to decipher the inscriptions.")
        print("The ancient language reveals historical details about the temple, providing valuable insights.")
        print("You discovered some valuable information about the temple")
        print(f"{player_name}! What will we do now?")
        print("1. Let's explore the other passage")
        print("2. Return to camp")
        a=input()
        print("enter the choice:",a)
        if a == '1':
            print("Let's explore the right passage also.")
            explore_right_passage(player_name)
        elif a == '2':
            print("Let's return to camp.")
            ending_successful_discovery()
            
        else:
            print("Invalid input! Choose 1 or 2.")

        
        # Continue the story or introduce more events...

        # After a successful choice, offer options to the player
        
    elif choice == 2:
        print("You ask Kaira Krishan for assistance in deciphering the inscriptions.")
        print("\n** Team Conversation **")
        print("Kaira Krishan helps in decoding the language, uncovering hidden meanings in the inscriptions.")
        # Continue the story or introduce more events...

        # After a successful choice, offer options to the player
        print("1. Let's explore the other passage")
        print("2. Return to camp")
        a=input()
        print("enter the choice:",a)
        if a == '1':
            print("Let's explore the right passage also.")
            explore_right_passage(player_name)
        elif a == '2':
            print("Let's return to camp.")
            ending_successful_discovery()
            
        else:
            print("Invalid input! Choose 1 or 2.")

    elif choice == 3:
        print("You choose to document the inscriptions for later analysis by the team.")
        print("This information could be useful in future explorations.")
        print("a creature attacked your team and jack ryan death")
        
        # Continue the story or introduce more events...

        # After a successful choice, offer options to the player
        ending_tragic_outcome()
    
    else:
        print("Invalid choice. Please try again.")
        explore_left_passage_after_trap(player_name)  # Restart the event if the choice is invalid.


def explore_right_passage(player_name):
    print("\nThe team decides to explore the right passage of the temple.")
    print("As you proceed, you encounter a room filled with mechanisms, and suddenly, an attack is triggered!")

    # Event: Defending Against Attacking Mechanism
    print("\n** Defending Against Attacking Mechanism **")
    print("The mechanisms come to life, launching projectiles toward the team.")
    print(f"{player_name}, what will you do?")
    print("1. Take cover behind nearby structures")
    print("2. Signal Jack Ryan to analyze and counter the attacking mechanism")
    print("3. Attempt to disable the mechanisms using ancient knowledge")
    print("4. Coordinate with the team to dodge the incoming projectiles")

    choice = get_player_choice()

    if choice == 1:
        print("You quickly take cover behind nearby structures, avoiding the projectiles.")
        print("The team follows your lead, and the attack subsides.")
        # Continue the story or introduce more events...
        print("1. Let's explore the other passage")
        print("2. Return to camp")
        a=input()
        print("enter the choice:",a)
        if a == '1':
            print("Let's explore the left passage also.")
            explore_left_passage_after_trap(player_name)

        elif a == '2':
            print("Let's return to camp.")
            ending_successful_discovery()
            
        else:
            print("Invalid input! Choose 1 or 2.")

    elif choice == 2:
        print("You signal Jack Ryan to analyze and counter the attacking mechanism.")
        print("\n** Team Conversation **")
        print("Jack Ryan successfully analyzes the mechanism and devises a countermeasure.")
        print("1. Let's explore the other passage")
        print("2. Return to camp")
        a=input()
        print("enter the choice:",a)
        if a == '1':
            print("Let's explore the left passage also.")
            explore_left_passage_after_trap(player_name)

        elif a == '2':
            print("Let's return to camp.")
            ending_successful_discovery()
            
        else:
            print("Invalid input! Choose 1 or 2.")

    
        # Continue the story or introduce more events...
    elif choice == 3:
        print("You attempt to disable the mechanisms using your knowledge of ancient technology.")
        print("The mechanisms are successfully deactivated, preventing further attacks.")
        print("1. Let's explore the other passage")
        print("2. Return to camp")
        a=input()
        print("enter the choice:",a)
        if a == '1':
            print("Let's explore the left passage also.")
            explore_left_passage_after_trap(player_name)

        elif a == '2':
            print("Let's return to camp.")
            ending_successful_discovery()
            
        else:
            print("Invalid input! Choose 1 or 2.")

    
        # Continue the story or introduce more events...
    elif choice == 4:
        print("You coordinate with the team to dodge the incoming projectiles.")
        print("Although some team members are grazed, the coordinated effort minimizes injuries.")
        print("Bruce lost his leg due to incoming projectiles.")
        ending_tragic_outcome()
        # Continue the story or introduce more events...
    else:
        print("Invalid choice. Please try again.")
        explore_right_passage()  # Restart the event if the choice is invalid.

def explore_both_passages(player_name):
    print("\nCongratulations, the team has successfully explored both the left and right passages!")
    print("The mysteries of Angkor Wat have been unveiled, and your archaeological discoveries will be remembered.")
    ending_successful_discovery()
    ending()
   

def ending_successful_discovery():
    print("\n** Successful Discovery Ending **")
    print("The team successfully navigated the challenges of Angkor Wat.")
    print("Your archaeological discoveries are groundbreaking, and your team's efforts are applauded worldwide.")
    print("You've unlocked the ancient mysteries of the temple, leaving a lasting legacy in the field of archaeology.")
    
    
def ending_tragic_outcome():
    print("\n** Tragic Outcome Ending **")
    print("Despite your team's best efforts, not everyone made it back from Angkor Wat.")
    print("The challenges of the temple were formidable, and the losses are deeply felt.")
    print("Your journey ends with a sense of sorrow, and the mysteries of Angkor Wat remain shrouded in darkness.")

def ending():
    print("\n** End of the Adventure **")
    print("The day is over, and the team returns to the camp.")
    
    # Check if all team members are alive
    if all_team_members_alive():
        print("Congratulations! You and your team successfully navigated the challenges of Angkor Wat.")
        print("The mysteries of the temple have been unveiled, and your archaeological discoveries will be remembered.")
        ending_successful_discovery()
    else:
        print("Unfortunately, not all team members made it back. The challenges of Angkor Wat took a toll.")
        print("Reflecting on the events, you realize that there were traps and challenges that the team couldn't overcome.")
        ending_tragic_outcome()
        def all_team_members_alive():
    # Check if all team members are alive
    # You need to implement the actual logic here based on your game
    # For example, if you have a list of team members and their statuses (alive or not), you can check that.
    # For now, it returns True, so you need to replace this with your logic.
         return True



# Main execution starts here
player_name = get_player_name()
introduce_characters(player_name)
start_journey()
mysterious_chambers()


# Continue with the rest of your code...

# Ending function call
# Ending function call
if all_team_members_alive():  # Add your condition based on the game logic
    ending_successful_discovery()
else:
    ending_tragic_outcome()

ending()
