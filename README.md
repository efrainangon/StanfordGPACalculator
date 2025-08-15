# Stanford GPA Calculator

This is a simple Python script to calculate your current and potential GPA using Stanford's 4.3 scale. It supports retaken courses and shows GPA for both first and latest attempts per course. THIS CURRENTLY DOES NOT SUPPORT C/NC CLASSES AND I WILL MAKE A UI SOON.

## Features
- Calculates GPA using first attempt and latest attempt for each course
- Handles retaken courses (latest attempt replaces previous grade)
- Supports custom unit values and grades

## How to Use
1. **Clone or download this repository.**
2. **Edit `grades.csv`** with your courses. Example format:

```
Course Name,Units,Grade,Taken,Retake
MATH20,3,B-,yes,no
CS103,5,B-,yes,no
CS103,5,A+,yes,yes  # Retaken example
```
- `Taken`: "yes" if you've completed the course, "no" if not
- `Retake`: "yes" if this is a retake, otherwise "no"

3. **Run the script:**

```sh
python main.py
```

You will see four GPA calculations:
- Current GPA (taken courses, first attempt)
- Potential GPA (all courses, first attempt)
- Current GPA (taken courses, only latest attempt)
- Potential GPA (all courses, only latest attempt)

## Requirements
- Python 3.x
- No external packages required

## Example Output
```
Your current GPA (taken courses, first attempt): 2.98
Your potential GPA (all courses, first attempt): 3.53
Your current GPA (taken courses, only latest attempt): 3.70
Your potential GPA (all courses, only latest attempt): 3.70
```

## License
MIT
