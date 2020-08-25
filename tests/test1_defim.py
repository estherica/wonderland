import time

def marketing_menu():
    print("---------------------------------------------------------------------\nWelcome to the app for calculating your social media marketing budget\n---------------------------------------------------------------------")
    num = int(input("Please, enter your budget in dollars... "))
    time.sleep(1)
    print("\nYour total budget is " + str(num) + "$ that is " + str(num * 3.4) + " NIS.")
    num1 = int(input("\nHow many days would you like your Facebook campaign to last? "))
    time.sleep(1)
    num2 = int(input("\nHow many days would you like your Instagram campaign to last? "))
    time.sleep(1)
    budget = (num1 * 100) + (num2 * 50)
    budget_nis = budget * 3.4
    budget_tax = budget_nis + (budget_nis / 100 * 17)
    print("\nYour purchase price is " + str(budget) + "$ that is " + str(budget_nis) + " NIS.")
    time.sleep(1)
    print("Your purchase price with tax is " + str(budget_tax) + " NIS")
    if budget_tax > num * 3.4:
        time.sleep(1)
        print("\nThere is not enough money on your account to pay for the service. \nPlease add another " + str(budget_tax - (num * 3.4)) + " NIS.")
    else:
        time.sleep(1)
        print("\nSuccessful. The balance in your account is " + str((num * 3.4) - budget_tax))
    time.sleep(1)
    print("----------------------\nThank you and goodbye!")