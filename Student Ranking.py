import numpy as np
students = int(input("How many students you want to compare? "))
names = []
marks = []

for i in range(students):
    stu_name = input("Student name: ")
    stu_marks = int(input("Student marks: "))
    names.append(stu_name)
    marks.append(stu_marks)

# Convert marks list to a NumPy array
marks_array = np.array(marks)

# Analysis using NumPy
average = np.mean(marks_array)
highest = np.max(marks_array)
lowest = np.min(marks_array)

# Get names of highest and lowest scorers
highest_student = names[np.argmax(marks_array)]
lowest_student = names[np.argmin(marks_array)]

# Display the results
print("📊 Student Marks Analysis with NumPy")
print("Average Marks: ",round(average,2))
print("Highest Marks: ",highest,"(by",highest_student,")")
print("Lowest Marks: ",lowest,"(by",lowest_student,")")
