def calculate_gpa(grades=None, grading_scale=None):

    grades = grades or []

    grading_scale = grading_scale or {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'F': 0.0
    }


    points = list(map(lambda g: grading_scale.get(g), grades))


    valid_points = list(filter(lambda x: x is not None, points))

    total_points = sum(valid_points)
    count = len(valid_points)

    gpa = total_points / max(count, 1)

    return round(gpa, 2)


def print_gpa_summary(student_name, gpa):

    print(f"Student: {student_name} | GPA: {gpa:.2f}")



student_grades = ['A', 'B+', 'A-', 'C', 'B', 'X']

gpa_result = calculate_gpa(grades=student_grades)

print_gpa_summary(student_name="Ali", gpa=gpa_result)
