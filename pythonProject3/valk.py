import math

while True:

    current_amount_str = input("How many orbs do you currently have?: ")
    current_amount = int(current_amount_str.replace(',', ''))

    amount_needed_str = input("How many orbs does the upgrade cost?: ")
    amount_needed = int(amount_needed_str.replace(',', ''))

    total_needed = amount_needed - current_amount

    orb_percentage_str = input("What percentage boost do you have?: ")
    orb_percentage = float(orb_percentage_str.replace(',', ''))
    real_percent = orb_percentage / 100

    reward_str = input("How many orbs do you get per Extermination (without boost)?: ")
    reward = int(reward_str.replace(',', ''))
    reward_total = (real_percent * reward) + reward
    orbs_needed = (math.ceil(total_needed / reward_total))

    tickets_have =  int(input("How many tickets do you currently have?: "))

    total_tickets_needed = orbs_needed - tickets_have

    print(f"You need {orbs_needed} orb tickets.")
    print(f"You are missing {total_tickets_needed} tickets.")

    restart = input("\nRestart? Y/N (N will exit.): ")

    if restart.upper() == 'Y':
        print("Restarting!\n")
    elif restart.upper() == 'N':
        exit()
    else:
        print("fuck u nigger")
        exit()



