command = input()
total_money = 0
while command != "NoMoreMoney":
    money = float(command)
    if money < 0:
        print("Invalid operation!")
        break
    else:
        total_money += money
        print(f"Increase: {money:.2f}")
    command = input()
print(f"Total: {total_money:.2f}")


