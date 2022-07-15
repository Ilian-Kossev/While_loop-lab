target_sum = int(input())
command = input()
counter = 0
cash_transfer = 0
average_cash_transfer = 0
counter_cash_transfer = 0
card_transfer = 0
average_card_transfer = 0
counter_card_transfer = 0
total_income = 0
while command != "End":
    transferred_money = int(command)
    counter += 1
    if counter % 2 == 1:
        cash_transfer += transferred_money
        counter_cash_transfer += 1
        if transferred_money > 100:
            cash_transfer -= transferred_money
            counter_cash_transfer -= 1
            print(f"Error in transaction!")
        else:
            print(f"Product sold!")
    else:
        card_transfer += transferred_money
        counter_card_transfer += 1
        if transferred_money < 10:
            card_transfer -= transferred_money
            counter_card_transfer -= 1
            print(f"Error in transaction!")
        else:
            print(f"Product sold!")
    total_income = card_transfer + cash_transfer
    if total_income >= target_sum:
        average_cash_transfer = cash_transfer / counter_cash_transfer
        average_card_transfer = card_transfer / counter_card_transfer
        print(f"Average CS: {average_cash_transfer:.2f}")
        print(f"Average CC: {average_card_transfer:.2f}")
        break
    command = input()
if total_income < target_sum:
    print("Failed to collect required money for charity.")


