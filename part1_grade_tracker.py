# Raw Data
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Loop through each student
for student in raw_students:
    
    # Step 1: Clean name
    name = student["name"].strip().title()
    
    # Step 2: Convert roll number
    roll = int(student["roll"])
    
    # Step 3: Convert marks string to list
    marks_list = student["marks_str"].split(", ")
    marks = [int(m) for m in marks_list]
    
    # Step 4: Validate name
    words = name.split()
    valid = all(word.isalpha() for word in words)
    
    if valid:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")
    
    # Step 5: Print formatted profile
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

# Step 6: Special condition for roll 103
for student in raw_students:
    if int(student["roll"]) == 103:
        name = student["name"].strip().title()
        print("\nSpecial Output:")
        print(name.upper())
        print(name.lower())
#--------------------------------------------------------------

#task 2 

#----------------------------------------------------------------


        student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print(f"\nStudent: {student_name}")
print("------ Subject Report ------")

# Part 1: Print subjects with grades
for i in range(len(subjects)):
    m = marks[i]

    if 90 <= m <= 100:
        grade = "A+"
    elif 80 <= m <= 89:
        grade = "A"
    elif 70 <= m <= 79:
        grade = "B"
    elif 60 <= m <= 69:
        grade = "C"
    else:
        grade = "F"

    print(f"{subjects[i]} : {m} ({grade})")

# Part 2: Calculations
total = sum(marks)
average = round(total / len(marks), 2)

# Highest
max_marks = max(marks)
max_index = marks.index(max_marks)

# Lowest
min_marks = min(marks)
min_index = marks.index(min_marks)

print("\n------ Analysis ------")
print(f"Total Marks : {total}")
print(f"Average     : {average}")
print(f"Highest     : {subjects[max_index]} ({max_marks})")
print(f"Lowest      : {subjects[min_index]} ({min_marks})")

# Part 3: While loop for new entries
count = 0

while True:
    sub = input("\nEnter subject name (or type 'done' to stop): ")

    if sub.lower() == "done":
        break

    mark_input = input("Enter marks (0-100): ")

    # Validate input
    if not mark_input.isdigit():
        print("❌ Invalid input! Marks must be a number.")
        continue

    mark = int(mark_input)

    if mark < 0 or mark > 100:
        print("❌ Marks should be between 0 and 100.")
        continue

    # Add valid data
    subjects.append(sub)
    marks.append(mark)
    count += 1

# Final Output
new_average = round(sum(marks) / len(marks), 2)

print("\n------ Updated Report ------")
print(f"New subjects added : {count}")
print(f"Updated Average   : {new_average}")


#----------------------------------------------------------------

#task 3

#----------------------------------------------------------------

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
total_avg_sum = 0

topper_name = ""
topper_avg = 0

# Loop through students
for name, marks in class_data:
    
    avg = round(sum(marks) / len(marks), 2)
    total_avg_sum += avg

    # Pass / Fail
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    # Check topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    # Print row
    print(f"{name:<18} | {avg:^7} | {status}")

# Class average
class_avg = round(total_avg_sum / len(class_data), 2)

print("\n------ Summary ------")
print(f"Pass Students : {pass_count}")
print(f"Fail Students : {fail_count}")
print(f"Topper        : {topper_name} ({topper_avg})")
print(f"Class Average : {class_avg}")



#----------------------------------------------------------------

# task 4

#----------------------------------------------------------------

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip whitespace
clean_essay = essay.strip()
print("1. Clean Essay:")
print(clean_essay)

# Step 2: Title Case
print("\n2. Title Case:")
print(clean_essay.title())

# Step 3: Count 'python'
count = clean_essay.count("python")
print("\n3. Count of 'python':")
print(count)

# Step 4: Replace 'python'
replaced = clean_essay.replace("python", "Python 🐍")
print("\n4. After Replacement:")
print(replaced)

# Step 5: Split into sentences
sentences = clean_essay.split(". ")
print("\n5. Sentence List:")
print(sentences)

# Step 6: Print numbered sentences
print("\n6. Numbered Sentences:")
for i in range(len(sentences)):
    sentence = sentences[i]
    
    # Ensure sentence ends with '.'
    if not sentence.endswith("."):
        sentence += "."
    
    print(f"{i+1}. {sentence}")