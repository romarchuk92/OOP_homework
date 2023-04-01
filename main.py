class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, mentor_lecture, course_lecture, grade_lecture):
        if isinstance(mentor_lecture, Lecturer) and course_lecture in self.courses_in_progress and course_lecture in mentor_lecture.courses_attached:
            if course_lecture in mentor_lecture.grades_mentors:
                mentor_lecture.grades_mentors[course_lecture] += [grade_lecture]
            else:
                mentor_lecture.grades_mentors[course_lecture] = [grade_lecture]
        else:
            return 'Ошибка'

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
       
        
class Lecturer(Mentor):
    grades_mentors = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
 

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 

best_mentor = Lecturer('Bob', 'Netologiev')
best_mentor.courses_attached += ['OOP']

just_student = Student ('Kolya', 'Ychebnikov', 'man')
just_student.courses_in_progress += ['OOP']

just_student.rate_lecture(best_mentor, 'OOP', 9)
just_student.rate_lecture(best_mentor, 'OOP', 9)
just_student.rate_lecture(best_mentor, 'OOP', 10)

print(best_student.grades)
print(best_mentor.grades_mentors)