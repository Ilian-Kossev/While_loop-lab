width = int(input())
length = int(input())
height = int(input())
command = input()
total_volume_flat = width * length * height
volume_boxes = 0
difference = 0
while command != "Done":
    number_boxes = int(command)
    volume_boxes += number_boxes
    difference = volume_boxes - total_volume_flat
    if volume_boxes > total_volume_flat:
        print(f"No more free space! You need {difference} Cubic meters more.")
        break
    command = input()
if difference < 0:
    print(f"{abs(difference)} Cubic meters left.")



