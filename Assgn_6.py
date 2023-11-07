#############################################################################################
#Assgn_6 Ryan Murphy #Create a list of Students, their test grades, and a list of letter grades 
#Enter 5 student names 
#Input the 4 test scores to the each student in the student list 
#Then average the 4 test scores that each student recieved 
#Create the test scores by the percent the correspond to #Include that scores cannot be higher than 100 and lower than 0 
#Finally print the students average test score to their letter grade ############################################################################################ 
StudentList = []#creates a list of students 
TestAverages = []#creates a list of the test averages 
GradeList = []#create a list for the letter grades 
for Students in range(5):#range of 5 students
  Student = input("Enter A Student Name: ")#input statement for student 
  StudentList.append(Student)#adds a student to the student list 
  Percent = []#creates a list of test scores for each student
  for Tests in range(4):#makes a range of 4 test scores per student 
    score = float(input("Enter {}'s Test Score {}: ".format(Student,Tests+1)))#floats the students test score and formats the print 
    while score < 0 or score > 100:#while statement for a invalid input 
      score = float(input("Invalid Input\nEnter {}'s test score {}: ".format(Student,Tests+1)))#prints Invalid Input then repeats the test score option 
    Percent.append(score)#adds test score to test score list 
  TestAverages.append(sum(Percent) / 4)#averages the 4 test scores for each student 
  if TestAverages[-1] >= 90:#if score is greater than 90 print A 
    GradeList.append('A')#adds A to the grade list for the student 
  elif TestAverages[-1] >= 80:#if score is greater than 80 print B 
    GradeList.append('B')#adds B to the grade list for the student 
  elif TestAverages[-1] >= 70:#if score is greater than 70 print C 
    GradeList.append('C')#adds C to the grade list for the student 
  elif TestAverages[-1] >= 60:#if score is greater than 60 print D  
    GradeList.append('D')#adds C to the grade list for the student
  else:#if none of the options above print F 
    GradeList.append('F')#adds F to the grade list for the student 
print('{:30s}{:10s}{:10s}'.format('Name','Average','Grade'))#format prints Name, Average, and Grade 
for Students in range(5):#prints the range of the 5 students 
  print('{:30s}{:<10g}{:10s}'.format(StudentList[Students],TestAverages[Students],GradeList[Students]))#format prints the Students in order of their name input, then their test score average, then their Grade letter
