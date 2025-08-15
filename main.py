import csv
from collections import defaultdict

# Grade to GPA conversion based on Stanford's 4.3 scale
grade_points = {
    "A+": 4.3, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "NP": 0.0, "L": 2.0
}


def calculate_gpa_first_attempt(csv_file_path):
    first_attempt = {}
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            course = row["Course Name"].strip()
            if course not in first_attempt:
                first_attempt[course] = row

    current_units = 0
    current_weighted_points = 0
    potential_units = 0
    potential_weighted_points = 0

    for course, row in first_attempt.items():
        grade = row["Grade"].strip().upper()
        taken = row.get("Taken", "Yes").strip().lower()
        try:
            units = float(row["Units"])
            if grade in grade_points:
                potential_units += units
                potential_weighted_points += grade_points[grade] * units
                if taken == "yes":
                    current_units += units
                    current_weighted_points += grade_points[grade] * units
            else:
                print(f"Skipping ungraded or non-GPA grade: {grade}")
        except ValueError:
            print(f"Invalid units for course {row['Course Name']}: {row['Units']}")
    current_gpa = current_weighted_points / current_units if current_units > 0 else 0.0
    potential_gpa = potential_weighted_points / potential_units if potential_units > 0 else 0.0
    return current_gpa, potential_gpa

def calculate_gpa_latest_attempt(csv_file_path):
    # Store only the latest attempt for each course
    latest_attempt = defaultdict(dict)
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            course = row["Course Name"].strip()
            latest_attempt[course] = row  # Last occurrence will be the latest

    current_units = 0
    current_weighted_points = 0
    potential_units = 0
    potential_weighted_points = 0

    for course, row in latest_attempt.items():
        grade = row["Grade"].strip().upper()
        taken = row.get("Taken", "Yes").strip().lower()
        try:
            units = float(row["Units"])
            if grade in grade_points:
                potential_units += units
                potential_weighted_points += grade_points[grade] * units
                if taken == "yes":
                    current_units += units
                    current_weighted_points += grade_points[grade] * units
            else:
                print(f"Skipping ungraded or non-GPA grade: {grade}")
        except ValueError:
            print(f"Invalid units for course {row['Course Name']}: {row['Units']}")

    current_gpa = current_weighted_points / current_units if current_units > 0 else 0.0
    potential_gpa = potential_weighted_points / potential_units if potential_units > 0 else 0.0
    return current_gpa, potential_gpa


if __name__ == "__main__":
    file_path = 'grades.csv'
    # 1 & 2: First attempt per course
    current_gpa_first, potential_gpa_first = calculate_gpa_first_attempt(file_path)
    print(f"Your current GPA (taken courses, first attempt): {current_gpa_first:.2f}")
    print(f"Your potential GPA (all courses, first attempt): {potential_gpa_first:.2f}")

    # 3 & 4: Only latest attempt per course
    current_gpa_latest, potential_gpa_latest = calculate_gpa_latest_attempt(file_path)
    print(f"Your current GPA (taken courses, only latest attempt): {current_gpa_latest:.2f}")
    print(f"Your potential GPA (all courses, only latest attempt): {potential_gpa_latest:.2f}")
