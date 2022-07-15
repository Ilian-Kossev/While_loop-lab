n = int(input())
sum_numbers = 0

for number in range(1, n + 1):
    digit = int(input())
    sum_numbers += digit
average = sum_numbers / n
print(f"{average:.2f}")

