def get_human_choice():
    human_choice = int(input("Enter you choice 0-6: "))
    while(human_choice not in range(0, 7)):
        print("Invalid Input")
        human_choice = int(input("Enter you choice 0-6: "))
    return human_choice