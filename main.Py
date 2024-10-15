

import csv

def main():
    # Load dataset using csv module
    students = []
    with open('students_complete.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            students.append(row)
    
    # Displays the first few records.
    print("First few records of the dataset:")
    for student in students[:5]:
        print(student)

    # Sorts by Math Score using selection sort (descending).
    sorted_math = selection_sort_desc(students[:], key='Math Score')
    print("\nTop records sorted by Math Score (descending):")
    for record in sorted_math[:5]:
        print(record)

    # Sorts by Reading Score using insertion sort (ascending).
    sorted_reading = insertion_sort_asc(students[:], key='Reading Score')
    print("\nTop records sorted by Reading Score (ascending):")
    for record in sorted_reading[:5]:
        print(record)

    # Linear search by Student ID.
    student_id = input("\nEnter Student ID to find their scores: ")
    student_record = linear_search_by_id(students, student_id)
    if student_record:
        print(f"\nRecord for Student ID {student_id}:")
        print(student_record)
    else:
        print(f"\nNo record found for Student ID {student_id}.")

    # Binary search by Reading Score.
    target_score = float(input("\nEnter Reading Score to search for a student: "))
    result = binary_search_by_reading_score(sorted_reading, target_score)
    if result:
        print(f"\nRecord for Reading Score {target_score}:")
        print(result)
    else:
        print(f"\nNo student found with Reading Score {target_score}.")

    # Calculates and displays average scores per grade.
    calculate_average_scores(students)

    # Calculates and displays pass rates.
    calculate_pass_rates(students)


def selection_sort_desc(students, key):
    n = len(students)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if float(students[j][key]) > float(students[max_idx][key]):
                max_idx = j
        students[i], students[max_idx] = students[max_idx], students[i]
    return students

def insertion_sort_asc(students, key):
    for i in range(1, len(students)):
        key_value = students[i]
        j = i - 1
        while j >= 0 and float(key_value[key]) < float(students[j][key]):
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_value
    return students

def linear_search_by_id(students, student_id):
    for student in students:
        if student['Student ID'] == student_id:
            return student
    return None

def binary_search_by_reading_score(students, target_score):
    low, high = 0, len(students) - 1
    while low <= high:
        mid = (low + high) // 2
        if float(students[mid]['Reading Score']) == target_score:
            return students[mid]
        elif float(students[mid]['Reading Score']) < target_score:
            low = mid + 1
        else:
            high = mid - 1
    return None

def calculate_average_scores(students):
    grade_scores = {}
    for student in students:
        grade = student['Grade']
        if grade not in grade_scores:
            grade_scores[grade] = {'reading_sum': 0, 'math_sum': 0, 'count': 0}
        grade_scores[grade]['reading_sum'] += float(student['Reading Score'])
        grade_scores[grade]['math_sum'] += float(student['Math Score'])
        grade_scores[grade]['count'] += 1
    
    print("\nAverage Reading and Math Scores by Grade:")
    for grade, scores in grade_scores.items():
        avg_reading = scores['reading_sum'] / scores['count']
        avg_math = scores['math_sum'] / scores['count']
        print(f"Grade {grade}: Average Reading Score = {avg_reading:.2f}, Average Math Score = {avg_math:.2f}")

def calculate_pass_rates(students):
    grade_pass_rates = {}
    for student in students:
        grade = student['Grade']
        if grade not in grade_pass_rates:
            grade_pass_rates[grade] = {'reading_passed': 0, 'math_passed': 0, 'count': 0}
        if float(student['Math Score']) >= 70:
            grade_pass_rates[grade]['math_passed'] += 1
        if float(student['Reading Score']) >= 70:
            grade_pass_rates[grade]['reading_passed'] += 1
        grade_pass_rates[grade]['count'] += 1

    print("\nPass percentage by Grade (70+):")
    for grade, rates in grade_pass_rates.items():
        math_pass_rate = (rates['math_passed'] / rates['count']) * 100
        reading_pass_rate = (rates['reading_passed'] / rates['count']) * 100
        print(f"Grade {grade}: Math Pass Rate = {math_pass_rate:.2f}%, Reading Pass Rate = {reading_pass_rate:.2f}%")

main()
