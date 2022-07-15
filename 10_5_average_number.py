n = int(input())
sum_numbers = 0
counter = 0
while counter < n:
    number = int(input())
    sum_numbers += number
    counter += 1
average = sum_numbers / counter
print(f"{average:.2f}")
