import random

def start_at_hogwarts():
    print("Welcome to Hogwarts!")
    print("You find yourself standing in the courtyard of the magical school, surrounded by towering castle walls.")
    print("As you ponder your next move, you notice three intriguing locations:")
    print("1. The Forbidden Forest")
    print("2. Hagrid's Hut")
    print("3. The Quidditch Pitch")
location = input("choose a number: ")

if location == "1":
    def explore_forbidden_forest():
        print("\nYou enter the Forbidden Forest, the air thick with mystery and danger.")
    print("Soon, you encounter a group of centaurs blocking your path.")
    choice = input("Do you attempt to reason with the centaurs? (yes/no): ").lower()
    if choice == "yes":
        print("The centaurs are impressed by your bravery and allow you to pass safely.")
        print("You continue deeper into the forest and find a hidden clearing where a unicorn grazes peacefully.")
        print("Congratulations! You've successfully navigated the Forbidden Forest.")
    elif choice == "no":
        print("The centaurs take offense to your defiance and chase you out of the forest.")
        print("You narrowly escape, but your adventure at the Forbidden Forest ends here.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

def explore_hagrids_hut():
    print("\nYou make your way to Hagrid's Hut, the warm glow of the fire beckoning you inside.")
    print("Hagrid welcomes you with open arms and offers you a cup of tea.")
    print("During your conversation, he mentions a hidden chamber within the castle.")
    choice = input("Do you ask Hagrid for more information about the chamber? (yes/no): ").lower()
    if choice == "yes":
        print("Hagrid reveals the location of the chamber and gives you a map to find it.")
        print("You leave Hagrid's Hut with a sense of excitement, ready to uncover the chamber's secrets.")
    elif choice == "no":
        print("You thank Hagrid for his hospitality and leave his hut.")
        print("As you wander the grounds, you can't shake the feeling that you've missed out on something important.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

def explore_quidditch_pitch():
    print("\nYou head to the Quidditch Pitch, where students are gearing up for a practice match.")
    print("The captain of your house team approaches you and offers you a chance to join in the game.")
    choice = input("Do you accept the captain's offer and play in the match? (yes/no): ").lower()
    if choice == "yes":
        print("You join the match and showcase your flying skills, scoring several goals for your team.")
        print("Your impressive performance earns you praise from your teammates and housemates.")
        print("Congratulations! You've won the Quidditch match.")
    elif choice == "no":
        print("You decline the offer to play and watch the match from the sidelines.")
        print("As you observe, you feel a sense of regret for not seizing the opportunity to participate.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

def main():
    start_at_hogwarts()
    while True:
        choice = input("\nWhich location will you visit? (1/2/3): ")
        if choice == "1":
            explore_forbidden_forest()
            break
        elif choice == "2":
            explore_hagrids_hut()
            break
        elif choice == "3":
            explore_quidditch_pitch()
            break
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")

if __name__ == "__main__":
    main()
