import csv

# Create student_marks.csv automatically
with open("student_marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Math", "Science", "English"])
    writer.writerow(["Aarav", 85, 90, 88])
    writer.writerow(["Diya", 78, 82, 80])
    writer.writerow(["Karan", 92, 89, 95])
    writer.writerow(["Meera", 75, 79, 83])
    writer.writerow(["Rohan", 88, 91, 87])

students = []

# Read the CSV file
with open("student_marks.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total = int(row["Math"]) + int(row["Science"]) + int(row["English"])
        average = total / 3

        row["Total_Marks"] = total
        row["Average"] = round(average, 2)

        students.append(row)

# Write updated data
with open("updated_student_marks.csv", "w", newline="") as file:
    fieldnames = students[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("Updated file created successfully!")

# Display updated records
for student in students:
    print(student)
