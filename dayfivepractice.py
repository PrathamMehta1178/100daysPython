student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total = 0
for height in student_heights:
    total += height
amtHeights = 0
for i in student_heights:
   amtHeights += 1

average = total / amtHeights
print(round(average)) 