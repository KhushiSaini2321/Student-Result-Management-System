#STUDENT RESULT MANAGEMENT SYSTEM
#list of all students
Students = []
n = int(input("Number of students : "))
for i in range(n):
 print("Enter details of Student :- ")
 name = input("Enter student name : ")
 roll_no = int(input("Enter student roll_no : "))
 #list of marks
 marks = []
 for j in range(5):
    mark = int(input(f"Eneter marks of student : {j+1}: "))
    marks.append(mark)

#calculatetotal and average
total = sum(marks)
average = total/len(marks)
# calculate percentage
percentage =  (sum(marks) / (len(marks)*100)) * 100
# calculate grade
if percentage > 90:
  Grade = "A"
elif percentage > 80:
   Grade = "B"
elif percentage > 70:
   Grade = "C"
elif percentage > 60:
   Grade = "D"
elif percentage > 50:
   Grade = "E"
elif percentage > 40:
   Grade = "F"
else :
   Grade = "FAIL"
#creat student dictionary
Student = {
    "name" : name,
    "roll_no" : roll_no,
    "marks" : marks,
    "total" : total,
    "average" : average,
    "percentage" : percentage,
    "Grade" : Grade
}
# Append dictionary to list
Students.append(Student)

#print student record
print("\n all student record")
# select student to save
search_roll = int(input("\nEnter roll number of student to save : "))
found = False
for s in Students:
    if s["roll_no"] == search_roll:
        found = True
# Write a file
with open("student.txt","w") as file:
  for s in Students:
    file.write(f"name : {s['name']}\n")
    file.write(f"roll_no : {s['roll_no']}\n")
    file.write(f"marks : {s['marks']}\n")
    file.write(f"total : {s['total']}\n")
    file.write(f"average : {s['average']}\n")
    file.write(f"percentage : {s['percentage']}\n")
    file.write(f"Grade : {s['Grade']}\n")
    break
if not found:
   print("\n student not found")




    


