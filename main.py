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

    def rating_stud(self):
        self.all_sum = []
        self.all_len = []
        
        for self.value in self.grades.values():
            self.all_sum.append(sum(self.value))
            self.all_len.append(len(self.value))
        try:     
            return round(sum(self.all_sum)/sum(self.all_len), 2)
        except: 
            return round(sum(self.all_sum)/1, 2)

    def __str__(self):

        try:
            return f'Имя: {self.name} \nФамилия: {self.surname} \
                \nСредняя оценка за домашние задания: {self.rating_stud()} \
                \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \
                \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        except: 
            return f'Имя: {self.name} \nФамилия: {self.surname} \
                \nСредняя оценка за домашние задания:  \
                \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \
                \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        if self.rating_stud() < other.rating_stud():
            return f'{other.name} имеет средний балл выше: {other.rating_stud()}, а {self.name} ниже: {self.rating_stud()}' 
        elif self.rating_stud() > other.rating_stud():
            return f'{other.name} имеет средний балл ниже: {other.rating_stud()}, а {self.name} выше: {self.rating_stud()}'
        else: 
            return f'{other.name} и {self.name} имеют одинаковый средний балл: {self.rating_stud()}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_mentors = {}
    
    def rating_lect(self):
        self.all_sum = []
        self.all_len = []
          
        for self.value in self.grades_mentors.values():
            self.all_sum.append(sum(self.value))
            self.all_len.append(len(self.value)) 
        try: return round(sum(self.all_sum)/sum(self.all_len), 2)
        except: return round(sum(self.all_sum)/1, 2)
    
    def __str__(self):

        try: return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.rating_lect()}'
        except: return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: '

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        if self.rating_lect() < other.rating_lect():
            return f'{other.name} имеет средний балл выше: {other.rating_lect()}, а {self.name} ниже: {self.rating_lect()}'
        elif self.rating_lect() > other.rating_lect(): 
            return f'{other.name} имеет средний балл ниже: {other.rating_lect()}, а {self.name} выше: {self.rating_lect()}'
        else: return f'{other.name} и {self.name} имеют одинаковый средний балл: {self.rating_lect()}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} '
    
 

# Студенты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

some_student = Student('Vitya', 'Petrov', 'your_gender')
some_student.courses_in_progress += ['OOP']
some_student.courses_in_progress += ['Python'] 


# Лекторы
some_lecturer = Lecturer('Bob', 'Netologiev')
some_lecturer.courses_attached += ['OOP']
some_lecturer.courses_attached += ['Python']  # это

some_lecturer_1 = Lecturer('Artem', 'Fanagoriev')
some_lecturer_1.courses_attached += ['OOP']
some_lecturer_1.courses_attached += ['Python']

        # Оценки лектору
best_student.rate_lecture(some_lecturer, 'Python', 5)
best_student.rate_lecture(some_lecturer, 'Python', 5)
best_student.rate_lecture(some_lecturer, 'Python', 5)


some_student.rate_lecture(some_lecturer_1, 'Python', 10)
some_student.rate_lecture(some_lecturer_1, 'Python', 10)
some_student.rate_lecture(some_lecturer_1, 'Python', 10)

# Проверяющие
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']
cool_mentor.courses_attached += ['OOP']

cool_mentor_1 = Reviewer('Tom', 'Ivanov')
cool_mentor_1.courses_attached += ['Python']
cool_mentor_1.courses_attached += ['OOP']

        # Оценки студенту
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor_1.rate_hw(some_student, 'Python', 5)
cool_mentor_1.rate_hw(some_student, 'Python', 5)
cool_mentor_1.rate_hw(some_student, 'Python', 10)
 

student_list = [best_student, some_student]
lecturer_list = [some_lecturer, some_lecturer_1]

def course_rating(course, person_list):
    for stud in person_list:
        
        if course in stud.grades:
            print (f'У {stud.name} средний балл по теме {course} составляет: {stud.rating_stud()}')
        else: print(f'У {stud.name} данный курс не найден')

def course_rating_1(course, person_list):
    for stud in person_list:
        
        if course in stud.grades_mentors:
            print (f'У {stud.name} средний балл по теме {course} составляет: {stud.rating_lect()}')
        else: print(f'У {stud.name} данный курс не найден')     


print('Оценки студентов:')
print(course_rating('Python', student_list))
print()
print('Оценки лекторов:')
print(course_rating_1('Python', lecturer_list))
print()
print()
print('\nУ проверяющих:')
print(cool_mentor)
print('\nУ лекторов:')
print(some_lecturer)
print('\nА у студентов так:')
print(best_student)
print()
print(some_lecturer.__lt__(some_lecturer_1))
print()
print(some_student.__lt__(best_student))