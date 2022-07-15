detergent_bottles = int(input())
command = input()
counter = 0
number_dishes = 0
number_pots = 0
detergent_available_ml = detergent_bottles * 750
detergent_needed_ml = 0
while command != "End":
    cutlery = int(command)
    counter += 1
    if counter % 3 == 0:
        number_pots += cutlery
    else:
        number_dishes += cutlery
    detergent_needed_ml = number_pots * 15 + number_dishes * 5
    if detergent_available_ml < detergent_needed_ml:
        missing_detergent_ml = detergent_needed_ml - detergent_available_ml
        print(f"Not enough detergent, {missing_detergent_ml} ml. more necessary!")
        break
    command = input()
if detergent_available_ml >= detergent_needed_ml:
    leftover_detergent_ml = detergent_available_ml - detergent_needed_ml
    print(f"Detergent was enough!")
    print(f"{number_dishes} dishes and {number_pots} pots were washed.")
    print(f"Leftover detergent {leftover_detergent_ml} ml.")

