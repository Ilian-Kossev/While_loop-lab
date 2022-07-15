student_name = input()
year_number = 0
total_grade = 0
bad_grade_year = 0
average_grade = 0
while year_number < 12:
    year_number += 1
    yearly_grade = float(input())
    total_grade += yearly_grade
    average_grade = total_grade / year_number
    if yearly_grade < 4:
        print(f"{student_name} has been excluded at {year_number} grade")
        break
    elif year_number == 12:
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
