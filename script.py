# https://www.codecademy.com/courses/learn-python-3/lessons/data-types/exercises/review

# This link was helpful
# https://discuss.codecademy.com/t/how-can-i-access-pieters-grade-after-it-has-been-added/465238/33

class Student:
  students_count = 0
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = []
    self.results = ''
    Student.students_count += 1
    self.student_id = Student.students_count

  # def __repr__(self):
  #   return str(self.print_grades())
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
# better to have .score then we dont need print_grades method entirely!!
      # self.grades.append(grade.score)
  

  # using this method to access self.grades!!
  def print_grades(self):
    grade_list = []
    for grade in self.grades:
        # print(grade.score)
        grade_list.append(grade.score)
    return grade_list


  def get_average(self):
    total = 0
    # print(self.print_grades())
    for i in self.print_grades():
      total += i
    return total / len(self.print_grades())
  
  def get_attendance(self, date, present):
    self.attendance.append({
      'date': date,
      'present': present
    })

    return self.attendance

  def final_result(self, grade):
    if type(grade) is Grade:      
      self.results = grade.is_passing()
      return self.results

    #     def add_grade(self, grade):
    # if type(grade) is Grade:
    #   self.grades.append(grade)


class Grade:
  minimum_passing = 65
  grade_count = 0
  def __init__(self, score):
    self.score = score
    self.achieve = ''
    Grade.grade_count += 1
    self.grade_id = Grade.grade_count
  
  def __repr__(self):
    return str(self.achieve)

  def is_passing(self):
    if self.score >= self.minimum_passing:
      self.achieve = "Passed"
      return self.achieve
    else:
      self.achieve = "Failed"
      return self.achieve
  
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
print("pieter id: ", pieter.student_id) # 3
print("roger id: ", roger.student_id) # 1

pieter_100 = pieter.add_grade(Grade(100))
pieter_75 = pieter.add_grade(Grade(75))
pieter_80 = pieter.add_grade(Grade(80))


sandro_35 = sandro.add_grade(Grade(30))
sandro_30 = sandro.add_grade(Grade(35))
sandro_40 = sandro.add_grade(Grade(40))

roger_89 = roger.add_grade(Grade(89))
roger_88 = roger.add_grade(Grade(88))
roger_87 = roger.add_grade(Grade(87))
print(Grade.grade_count)

print(pieter.print_grades())
print(sandro.print_grades())
print(roger.print_grades())



print(pieter.get_average())
print(sandro.get_average())
print(roger.get_average())


pieter.get_attendance('22/03/2022', True)
pieter.get_attendance('01/01/2022', False)
print(pieter.attendance)


pieter_average_results = pieter.get_average()
pieter_pass_or_fail = pieter.final_result(Grade(pieter_average_results))
# print('jdsf', pieter_pass_or_fail)

sandro_average_results = sandro.get_average()
sandro_pass_or_fail = sandro.final_result(Grade(sandro_average_results))
# print('jdsf', sandro_pass_or_fail)


roger_average_results = pieter.get_average()
roger_pass_or_fail = roger.final_result(Grade(roger_average_results))
# print('jdsf', roger_pass_or_fail)


print("Pieter", pieter.results)
print("Sandro", sandro.results)
print("Roger", roger.results)