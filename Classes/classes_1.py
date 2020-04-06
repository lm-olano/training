class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      pass
  def get_average(self):
    total = 0
    for grade in self.grades:
      total += grade.score
    return total/len(self.grades)
  def add_attendance(self,date):
    self.attendance[date] = True
  def check_attendance(self, date):
    attended = False
    if date in self.attendance.keys():
      if self.attendance[date]:
        attended = True
    return attended

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  def is_passing(self):
    is_pass = False
    if self.score >= self.minimum_passing:
      is_pass = True
    return is_pass

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

grade100 = Grade(100)
grade20 = Grade(20)
grade50 = Grade(50)

pieter.add_grade(grade100)
pieter.add_grade(grade100)
pieter.add_grade(grade100)
pieter.add_grade(grade20)

print(pieter.get_average())

sandro.add_attendance("02/04/2020")
print(sandro.check_attendance("02/04/2020"))
print(sandro.check_attendance("10/04/2020"))
